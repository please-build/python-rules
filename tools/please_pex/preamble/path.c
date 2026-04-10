#include <libgen.h>
#include <paths.h>
#include <unistd.h>

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
 * get_path_var stores the value of the PATH variable in path. It returns NULL on success and an
 * error on failure.
 *
 * The value of the PATH variable is taken to be the first non-empty value in the following list:
 * - The value of the PATH environment variable.
 * - The value of the C standard library's _CS_PATH configuration variable.
 * - The value of the C standard library's hardcoded default PATH variable.
 */
static err_t *get_path_var(char **path) {
    char *path_env = getenv("PATH");
    size_t len = 0;
    err_t *err = NULL;

    (*path) = NULL;

    if (path_env != NULL) {
        if (((*path) = strdup(path_env)) == NULL) {
            err = err_from_errno("strdup path_env");
        }
        goto end;
    }

    if ((len = confstr(_CS_PATH, NULL, 0)) != 0) {
        MALLOC(*path, char, len);
        if (confstr(_CS_PATH, *path, len) == 0) {
            err = err_from_errno("confstr write");
        }
        goto end;
    }

    MALLOC(*path, char, strlen(_PATH_DEFPATH) + 1); // 1 extra byte for trailing null
    strcpy(*path, _PATH_DEFPATH);

end:
    if (err != NULL) {
        FREE(*path);
    }

    return err;
}

/*
 * resolve_path resolves the given path and stores the resolved path in res_path. It returns NULL on
 * success and an error on failure.
 *
 * The given path is resolved as follows:
 * - If the path contains a "/" character, resolve_path returns a copy of the given path.
 * - If the path does not contain a "/" character, resolve_path treats it as a file name, and
 *   searches directories in the PATH variable from left to right for a file with that name,
 *   similarly to how a shell would. It returns the path to the first file it finds, which is
 *   relative if the current directory is present in PATH and the file was found in the current
 *   directory, or absolute otherwise.
 */
err_t *resolve_path(char *path, char **res_path) {
    char *path_dirs = NULL;
    char *dir_start = NULL;
    char *dir_end = NULL;
    size_t path_len = strlen(path);
    size_t dir_len = 0;
    err_t *err = NULL;

    (*res_path) = NULL;

    if (path_len == 0) {
        err = err_from_str("empty path name given");
        goto end;
    }

    // If the given path is a relative path containing a "/" or an absolute path, we don't need to
    // do any PATH searching - just return a copy of the path we were given.
    if (strchr(path, '/') != NULL) {
        if (((*res_path) = strdup(path)) == NULL) {
            err = err_from_errno("strdup path");
        }
        goto end;
    }

    if ((err = get_path_var(&path_dirs)) != NULL) {
        err = err_wrap("get PATH variable", err);
        goto end;
    }

    // Iterate over the directories in PATH:
    dir_end = path_dirs;
    do {
        // Point dir_end to the end of the next directory in PATH.
        for (dir_start = dir_end; *dir_end != 0 && *dir_end != ':'; dir_end++) {
            continue;
        }

        // Construct a candidate path by concatenating the next directory in PATH and the file name
        // we were given. Shells treat a zero-length directory name in PATH as shorthand for the
        // current working directory, in which case there's no need for any concatenation - the
        // candidate path can just be the (relative) file name we were given.
        if (dir_start == dir_end) {
            if (((*res_path) = strdup(path)) == NULL) {
                err = err_from_errno("strdup path");
                goto end;
            }
        } else {
            dir_len = dir_end - dir_start;
            MALLOC(*res_path, char, dir_len + 1 + path_len + 1); // 2 extra bytes for "/" separator and trailing null
            strncpy(*res_path, dir_start, dir_len);
            (*res_path)[dir_len] = '/';
            strcpy((*res_path) + dir_len + 1, path);
            (*res_path)[dir_len + 1 + path_len] = 0;
        }

        // If a file exists at this candidate path, stop searching PATH and return this path. We
        // don't check whether it is executable, only whether it exists - this replicates the
        // behaviour of (some) shells when they search PATH.
        if (access(*res_path, F_OK) == 0) {
            goto end;
        }

        FREE(*res_path);
    } while (*dir_end++ == ':');

    err = err_wrap("file not found in PATH", err_from_str(path));

end:
    FREE(path_dirs);

    if (err != NULL) {
        FREE(*res_path);
    }

    return err;
}

/*
 * get_pex_path stores the canonical absolute path to the .pex file in pex_path. It returns NULL on
 * success and an error on failure.
 */
err_t *get_pex_path(char **pex_path) {
    char *exe_path = NULL;
    err_t *err = NULL;

#if defined(__linux__)
    exe_path = "/proc/self/exe";
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

    if (((*pex_path) = realpath(exe_path, NULL)) == NULL) {
        err = err_from_errno("realpath");
        goto end;
    }
    log_debug("Canonical path of .pex file is %s", (*pex_path));

end:
#ifndef __linux__
    FREE(exe_path);
#endif

    if (err != NULL) {
        FREE(pex_path);
    }

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
 * tree, get_plz_bin_path stores NULL in path.
 */
err_t *get_plz_bin_path(char **path) {
    char *pex_path = NULL;
    char *pex_dir = NULL;
    char *tmp_dir = NULL;
    char *tmp_dir_realpath = NULL;
    size_t pex_dir_len = 0;
    size_t tmp_dir_len = 0;
    err_t *err = NULL;

    (*path) = NULL;

    if ((err = get_pex_path(&pex_path)) != NULL) {
        err = err_wrap("get_pex_path", err);
        goto end;
    }
    pex_dir = dirname(pex_path);

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
        if ((tmp_dir_realpath = realpath(tmp_dir, NULL)) == NULL) {
            err = err_from_errno("realpath tmp_dir");
            goto end;
        }

        pex_dir_len = strlen(pex_dir);
        tmp_dir_len = strlen(tmp_dir_realpath);

        if (
            strncmp(tmp_dir_realpath, pex_dir, tmp_dir_len) == 0 &&
            (
                (pex_dir_len == tmp_dir_len) ||
                (pex_dir_len > tmp_dir_len && pex_dir[tmp_dir_len] == '/')
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
        // plz-out/ directory tree - return NULL.
        goto end;
    }
    MALLOC(*path, char, strlen(pex_dir) + strlen("/bin") + 1);
    if (sprintf(*path, "%s/bin", pex_dir) < 0) {
        err = err_from_errno("sprintf path");
    }

end:
    FREE(pex_path);
    FREE(tmp_dir_realpath);

    return err;
}
