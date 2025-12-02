#include <libgen.h>
#include <unistd.h>

#if defined(__linux__)
#include <limits.h>
#include <sys/stat.h>
#elif defined(__APPLE__)
#include <mach-o/dyld.h>
#elif defined(__FreeBSD__)
#include <sys/stat.h>
#include <sys/sysctl.h>
#endif

#include "log.h"
#include "path.h"
#include "pexerror.h"
#include "util.h"

#ifdef __linux__

/*
 * get_path_max returns the maximum length of a relative path name when the given path is the
 * current working directory (although the path need not actually be a directory, or even exist).
 */
static int get_path_max(char *path) {
    int path_max = pathconf(path, _PC_PATH_MAX);

    if (path_max <= 0) {
        // PATH_MAX may be defined in <limits.h>, but this is not a POSIX requirement. If it isn't
        // defined, fall back to 4096 (as recommended by Linux's realpath(3) man page).
#ifdef PATH_MAX
        path_max = PATH_MAX;
#else
        path_max = 4096;
#endif
    }

    return path_max;
}

/*
 * get_link_path resolves the symbolic link at the path lpath and stores the link's destination path
 * in rpath. It returns NULL on success and an error on failure.
 */
static err_t *get_link_path(char *lpath, char **rpath) {
    struct stat sb = { 0 };
    int slen = 0;
    int rlen = 0;
    err_t *err = NULL;

    // Get the length of lpath's destination path so we can allocate a buffer of that length for
    // readlink to write to (plus one byte, so we can determine whether readlink has truncated the
    // path it writes, and also for the trailing null we'll append to the path afterwards). If lpath
    // is a magic symlink (in which case sb.st_size is 0), assume the destination path is PATH_MAX
    // bytes long - it's an overestimate, but at least the buffer will be large enough for readlink
    // to safely write to.
    if (lstat(lpath, &sb) == -1) {
        err = err_from_errno("lstat");
        goto end;
    }
    slen = (sb.st_size == 0 ? get_path_max(lpath) : sb.st_size) + 1;

    MALLOC(*rpath, char *, slen);

    if ((rlen = readlink(lpath, (*rpath), slen)) == -1) {
        err = err_from_errno("readlink");
        goto end;
    }
    // If readlink filled the buffer, it truncated the destination path it wrote. In this case, the
    // value is untrustworthy, so we're better off not using it.
    if (slen == rlen) {
        err = err_from_str("readlink truncated destination path");
        goto end;
    }

    // Otherwise, add the trailing null to the destination path that readlink omitted.
    (*rpath)[rlen] = 0;

end:
    if (err != NULL) {
        FREE(*rpath);
    }

    return err;
}

#endif /* __linux__ */

/*
 * get_pex_dir stores the path to the .pex file in pex_dir. It returns NULL on success and an error
 * on failure.
 */
err_t *get_pex_dir(char **pex_dir) {
    char *exe_path = NULL;
    char *exe_dir = NULL;
    err_t *err = NULL;

#if defined(__linux__)
    if ((err = get_link_path("/proc/self/exe", &exe_path)) != NULL) {
        err = err_wrap("get_link_path", err);
        goto end;
    }
#elif defined(__APPLE__)
    uint32_t len = 0;

    // Call _NSGetExecutablePath once to find out how long the executable path is, then again after
    // we've allocated that much memory to store it.
    _NSGetExecutablePath(NULL, &len);
    MALLOC(exe_path, char, len);
    if (_NSGetExecutablePath(exe_path, &len) != 0) {
        err = err_from_str("_NSGetExecutablePath failure");
        goto end;
    }
#elif defined(__FreeBSD__)
    int mib[4] = {CTL_KERN, KERN_PROC, KERN_PROC_PATHNAME, -1};
    size_t len = 0;

    // Call sysctl once to find out how long the executable path is, then again after we've
    // allocated that much memory to store it.
    if (sysctl(mib, NELEMS(mib), NULL, &len, NULL, 0) == -1) {
        err = err_from_errno("sysctl lookup");
        goto end;
    }
    MALLOC(exe_path, char, len);
    if (sysctl(mib, NELEMS(mib), exe_path, &len, NULL, 0) == -1) {
        err = err_from_errno("sysctl write");
        goto end;
    }
#else
#error "Unsupported operating system"
#endif

    exe_dir = dirname(exe_path);
    if (((*pex_dir) = strdup(exe_dir)) == NULL) {
        err = err_from_errno("strdup");
        goto end;
    }

end:
    FREE(exe_path);

    return err;
}

/*
 * get_plz_bin_path stores the path to the directory containing Please's binary outputs in path. It
 * returns NULL on success and an error on failure.
 *
 * If the .pex file is running from within a Please build environment (which is assumed if PLZ_ENV
 * is defined in the environment), get_plz_bin_path returns the path to the build environment's root
 * directory (which is assumed to be the value of TMP_DIR in the environment, as created by Please).
 * Otherwise, get_plz_bin_path returns the path to the bin/ subdirectory within the plz-out/ directory
 * to which this .pex file belongs. If the .pex file does not exist within a plz-out/ directory
 * tree, get_plz_bin_path fails.
 */
err_t *get_plz_bin_path(char **path) {
    char *pex_dir = NULL;
    char *tmp_dir = NULL;
    char *pex_dir_realpath = NULL;
    char *tmp_dir_realpath = NULL;
    size_t pex_len = 0;
    size_t tmp_len = 0;
    err_t *err = NULL;

    if ((err = get_pex_dir(&pex_dir)) != NULL) {
        err = err_wrap("get_pex_dir", err);
        goto end;
    }

    if (getenv("PLZ_ENV") != NULL) {
        if ((tmp_dir = getenv("TMP_DIR")) == NULL) {
            // There are two circumstances under which this might happen: either if this is a Please
            // build environment but TMP_DIR was unset before the .pex file was executed, or if this
            // isn't a Please build environment and PLZ_ENV just happened to be set for some other
            // reason. The latter is more likely than the former (many build definitions rely on
            // TMP_DIR being defined, which would lead to much more breakage besides this function
            // failing) - therefore, optimise for the latter case.
            log_warn("PLZ_ENV is defined but TMP_DIR is not; assuming this is not a Please build environment");
            goto no_plz_env;
        }

        // Identify whether the .pex file exists inside the build environment.
        if ((pex_dir_realpath = realpath(pex_dir, NULL)) == NULL) {
            err = err_from_errno("realpath pex_dir");
            goto end;
        }
        if ((tmp_dir_realpath = realpath(tmp_dir, NULL)) == NULL) {
            err = err_from_errno("realpath tmp_dir");
            goto end;
        }

        pex_len = strlen(pex_dir_realpath);
        tmp_len = strlen(tmp_dir_realpath);

        if (
            strncmp(tmp_dir_realpath, pex_dir_realpath, tmp_len) == 0 &&
            (
                (pex_len == tmp_len) ||
                (pex_len - tmp_len >= 1 && pex_dir_realpath[tmp_len] == '/')
            )
        ) {
            if (((*path) = strdup(tmp_dir_realpath)) == NULL) {
                err = err_from_errno("strdup");
            }
            goto end;
        }
    }

no_plz_env:
    // Try searching the .pex file path component-wise for the last instance of "plz-out". If one is
    // found, assume the binary outputs are in the bin/ subdirectory within that directory. There's
    // no need to check now whether bin/ actually exists - if it doesn't, the call to execvp() later
    // will fail anyway.
    while (!STREQ(basename(pex_dir), "plz-out") && !STREQ(pex_dir, "/") && !STREQ(pex_dir, ".")) {
        pex_dir = dirname(pex_dir);
    }
    if (STREQ(pex_dir, "/") || STREQ(pex_dir, ".")) {
        // If we reached the left-most component in the path, the .pex file doesn't exist within a
        // plz-out/ directory tree.
        goto end;
    }
    MALLOC(*path, char, strlen(pex_dir) + strlen("/bin") + 1);
    if (sprintf(*path, "%s/bin", pex_dir) < 0) {
        err = err_from_errno("sprintf path");
    }

end:
    FREE(pex_dir_realpath);
    FREE(tmp_dir_realpath);

    return err;
}
