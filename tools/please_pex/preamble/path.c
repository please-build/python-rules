#include <libgen.h>

#if defined(__APPLE__)
#include <mach-o/dyld.h>
#elif defined(__FreeBSD__)
#include <sys/stat.h>
#include <sys/sysctl.h>
#endif

#include "log.h"
#include "path.h"
#include "pexerror.h"
#include "util.h"

/*
 * get_pex_dir stores the path to the .pex file in pex_dir. It returns NULL on success and an error
 * on failure.
 */
err_t *get_pex_dir(char **pex_dir) {
    char *exe_path = NULL;
    char *exe_dir = NULL;
    err_t *err = NULL;

#if defined(__linux__)
    if ((exe_path = realpath("/proc/self/exe", NULL)) == NULL) {
        err = err_from_errno("realpath /proc/self/exe");
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
                (pex_len > tmp_len && pex_dir_realpath[tmp_len] == '/')
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
        err = err_from_str(".pex file is in neither a Please build environment nor a Please repo");
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
