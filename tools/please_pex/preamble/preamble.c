#include <errno.h>
#include <unistd.h>

#include "cJSON.h"
#include "log.h"
#include "path.h"
#include "pexerror.h"
#include "queue.h"
#include "util.h"
#include "zip.h"

#define JSON_STRING(x) (cJSON_IsString(x) && (x)->valuestring != NULL)
#define JSON_STRLEN(x) strlen((x)->valuestring)

#define PREAMBLE_CONFIG_PATH ".bootstrap/PLZ_PREAMBLE_CONFIG"

/*
 * init_log configures log.c to log initially at error level and to include the current date and
 * time (but not source location) in log messages.
 */
static void init_log() {
    // In the early stages of the preamble, default to LOG_ERROR (although everything will be fatal
    // until we're in a position to call set_log_verbosity anyway, so this is more of a formality).
    log_set_level(LOG_ERROR);

    log_set_time_format("%Y-%m-%d %H:%M:%S");
}

/*
 * parse_log_level returns the log.c logging level represented by the given string, or -1 if the
 * given string does not represent a known logging level. It is the inverse of the string_log_level
 * function.
 */
static int parse_log_level(char *level) {
    if (level == NULL) {
        return -1;
    } else if (STREQ(level, "trace")) {
        return LOG_TRACE;
    } else if (STREQ(level, "debug")) {
        return LOG_DEBUG;
    } else if (STREQ(level, "info")) {
        return LOG_INFO;
    } else if (STREQ(level, "warn")) {
        return LOG_WARN;
    } else if (STREQ(level, "error")) {
        return LOG_ERROR;
    } else if (STREQ(level, "fatal")) {
        return LOG_FATAL;
    } else {
        return -1;
    }
}

/*
 * string_log_level returns a stringified representation of the given log.c logging level. It is
 * equivalent to log.c's log_level_string function, except it returns lower-case text.
 */
static char *string_log_level(int level) {
    if (level == LOG_TRACE) {
        return "trace";
    } else if (level == LOG_DEBUG) {
        return "debug";
    } else if (level == LOG_INFO) {
        return "info";
    } else if (level == LOG_WARN) {
        return "warn";
    } else if (level == LOG_ERROR) {
        return "error";
    } else if (level == LOG_FATAL) {
        return "fatal";
    }
    return "";
}

/*
 * set_log_verbosity sets log.c's logging level based on the value of the PLZ_PEX_PREAMBLE_VERBOSITY
 * environment variable, falling back to the default logging level set in the .pex preamble
 * configuration if PLZ_PEX_PREAMBLE_VERBOSITY does not have a recognised value (and falling back
 * further to "error" if the .pex preamble configuration also does not contain a recognised value).
 */
static void set_log_verbosity(const cJSON *config) {
    char *env_verbosity = getenv("PLZ_PEX_PREAMBLE_VERBOSITY");
    int level = parse_log_level(env_verbosity);
    const cJSON *json_verbosity = NULL;

    if (level == -1) {
        json_verbosity = cJSON_GetObjectItemCaseSensitive(config, "verbosity");
        if (!JSON_STRING(json_verbosity) || (level = parse_log_level(json_verbosity->valuestring)) == -1) {
            level = LOG_ERROR;
        }

        if (env_verbosity != NULL) {
            log_error("Unknown logging level '%s'; defaulting to '%s'", env_verbosity, string_log_level(level));
        }
    }

    log_set_level(level);
}

/*
 * get_config reads and parses the .pex preamble configuration, a JSON-encoded file at
 * .bootstrap/PLZ_PREAMBLE_CONFIG in the zip archive, and stores it in config. It returns NULL on
 * success and an error on failure.
 */
static err_t *get_config(char *pex_path, const cJSON **config) {
    struct zip_t *zip = NULL;
    int ziperr = 0;
    char *configbuf = NULL;
    size_t configsize = 0;
    err_t *err = NULL;

    zip = zip_openwitherror(pex_path, 0, 'r', &ziperr);
    if (ziperr < 0) {
        err = err_wrap("open .pex", err_from_str(zip_strerror(ziperr)));
        goto end;
    }

    if ((ziperr = zip_entry_open(zip, PREAMBLE_CONFIG_PATH)) < 0) {
        err = err_wrap("open .pex configuration", err_from_str(zip_strerror(ziperr)));
        goto end;
    }

    if ((ziperr = (int)zip_entry_read(zip, (void **)&configbuf, &configsize)) < 0) {
        err = err_wrap("read .pex configuration", err_from_str(zip_strerror(ziperr)));
        goto end;
    }

    zip_entry_close(zip);
    zip_close(zip);

    if (((*config) = cJSON_ParseWithLength(configbuf, configsize)) == NULL) {
        err = err_wrap(
            "parse .pex configuration",
            err_wrap("JSON syntax error near", err_from_str(cJSON_GetErrorPtr()))
        );
        goto end;
    }

end:
    FREE(configbuf);

    return err;
}

/*
 * get_interpreter_args extracts the array of interpreter command line arguments from the value of
 * "interpreter_args" in the given .pex preamble configuration and stores them in the same order in
 * the tail queue given by args; it also stores the length of this queue in len. It returns NULL on
 * success and an error on failure.
 */
static err_t *get_interpreter_args(const cJSON *config, int *len, strlist_t **args) {
    const cJSON *json_args = NULL;
    const cJSON *json_arg = NULL;
    strlist_elem_t *arg = NULL;
    err_t *err = NULL;

    STAILQ_NEW(*args, strlist_t);

    json_args = cJSON_GetObjectItemCaseSensitive(config, "interpreter_args");
    if (json_args == NULL || cJSON_IsNull(json_args)) {
        log_debug("interpreter_args is null; no arguments added");
        goto end;
    } else if (!cJSON_IsArray(json_args)) {
        err = err_from_str("interpreter_args must be an array or null");
        goto end;
    }

    *len = cJSON_GetArraySize(json_args);
    if (*len == 0) {
        log_debug("interpreter_args is empty; no arguments added");
        goto end;
    }

    cJSON_ArrayForEach(json_arg, json_args) {
        if (!JSON_STRING(json_arg)) {
            err = err_from_str("elements in interpreter_args must be strings");
            goto end;
        }

        STAILQ_ENTRY_NEW(arg, strlist_elem_t);
        MALLOC(arg->str, char, JSON_STRLEN(json_arg) + 1);
        strcpy(arg->str, json_arg->valuestring);
        STAILQ_INSERT_TAIL(*args, arg, next);
        log_debug("Added argument from interpreter_args: %s", arg->str);
    }

end:
    if (err != NULL) {
        if (arg != NULL) {
            FREE(arg->str);
            FREE(arg);
        }

        if (*args != NULL) {
            while (!STAILQ_EMPTY(*args)) {
                arg = STAILQ_FIRST(*args);
                STAILQ_REMOVE_HEAD(*args, next);
                FREE(arg->str);
                FREE(arg);
            }
        }
    }

    return err;
}

/*
 * get_interpreters extracts the array of interpreter paths from the value of "interpreters" in the
 * given .pex preamble configuration and stores them in the same order in the tail queue given by
 * interps. It returns NULL on success and an error on failure.
 */
static err_t *get_interpreters(const cJSON *config, strlist_t **interps) {
    strlist_elem_t *interp = NULL;
    char *plz_bin_path = NULL;
    const cJSON *json_interps = NULL;
    const cJSON *json_interp = NULL;
    err_t *err = NULL;

    json_interps = cJSON_GetObjectItemCaseSensitive(config, "interpreters");
    if (!cJSON_IsArray(json_interps)) {
        err = err_from_str("interpreters must be an array");
        goto end;
    }

    if (cJSON_GetArraySize(json_interps) == 0) {
        err = err_from_str("interpreters must not be empty");
        goto end;
    }

    STAILQ_NEW(*interps, strlist_t);

    cJSON_ArrayForEach(json_interp, json_interps) {
        if (!JSON_STRING(json_interp)) {
            err = err_from_str("elements in interpreters must be strings");
            goto end;
        }

        STAILQ_ENTRY_NEW(interp, strlist_elem_t);

        if (STRPREFIX(json_interp->valuestring, "$PLZ_BIN_PATH/")) {
            if (plz_bin_path == NULL) {
                if ((err = get_plz_bin_path(&plz_bin_path)) != NULL) {
                    err = err_wrap("PLZ_BIN_PATH resolution failure", err);
                    goto end;
                }
                log_debug("Resolved $PLZ_BIN_PATH to %s", plz_bin_path);
            }

            // Replace "$PLZ_BIN_PATH" with the path to Please's binary outputs directory at the
            // start of the interpreter path.
            MALLOC(interp->str, char, strlen(plz_bin_path) + JSON_STRLEN(json_interp) - strlen("$PLZ_BIN_PATH") + 1); // 1 extra byte for trailing null
            strncpy(interp->str, plz_bin_path, strlen(plz_bin_path));
            strcpy(interp->str + strlen(plz_bin_path), json_interp->valuestring + strlen("$PLZ_BIN_PATH"));
        } else {
            MALLOC(interp->str, char, JSON_STRLEN(json_interp) + 1); // 1 extra byte for trailing null
            strcpy(interp->str, json_interp->valuestring);
        }

        STAILQ_INSERT_TAIL(*interps, interp, next);

        log_debug("Added interpreter to search path: %s", interp->str);
    }

end:
    FREE(plz_bin_path);

    if (err != NULL) {
        if (interp != NULL) {
            FREE(interp->str);
            FREE(interp);
        }

        if (*interps != NULL) {
            while (!STAILQ_EMPTY(*interps)) {
                interp = STAILQ_FIRST(*interps);
                STAILQ_REMOVE_HEAD(*interps, next);
                FREE(interp->str);
                FREE(interp);
            }
        }
    }

    return err;
}

int main(int argc, char **argv) {
    err_t *err = NULL;
    const cJSON *config = NULL;
    int config_args_len = 0;
    strlist_t *config_args = NULL;
    strlist_elem_t *config_arg = NULL;
    strlist_t *interps = NULL;
    strlist_elem_t *interp = NULL;
    char **interp_argv = NULL;
    int i = 0;

    init_log();

    if (argc == 0) {
        log_fatal("Failed to execute .pex preamble: argv is empty");
        return 1;
    }

    if ((err = get_config(argv[0], &config)) != NULL) {
        log_fatal("Failed to get .pex preamble configuration: %s", err_str(err));
        return 1;
    }

    set_log_verbosity(config);

    if ((err = get_interpreter_args(config, &config_args_len, &config_args)) != NULL) {
        log_fatal("Failed to get interpreter arguments from .pex preamble configuration: %s", err_str(err));
        return 1;
    }

    if ((err = get_interpreters(config, &interps)) != NULL) {
        log_fatal("Failed to get interpreters from .pex preamble configuration: %s", err_str(err));
        return 1;
    }

    // interp_argv is the array of arguments that will be passed to execvp():
    //
    // {
    //     interpreter,
    //     config_args[0],
    //     # ...
    //     config_args[n],
    //     argv[0],
    //     # ...
    //     argv[n],
    //     NULL
    // }
    MALLOC(interp_argv, char *, 1 + config_args_len + argc + 1);

    // The first element is the Python interpreter path, which is substituted in during each
    // execvp() invocation. The remaining elements are static for each execvp() invocation:
    // - the interpreter arguments from the .pex preamble configuration (if any);
    STAILQ_FOREACH(config_arg, config_args, next) {
        interp_argv[1 + i] = config_arg->str;
        i++;
    }
    // - the name of the currently-executing program (which is also the .pex file that the
    //   Python interpreter needs to execute) and the command line arguments given to this
    //   process (if any);
    for (i = 0; i < argc; i++) {
        interp_argv[1 + config_args_len + i] = argv[i];
    }
    // - NULL (the terminator for execvp()).
    interp_argv[1 + config_args_len + argc] = NULL;

    STAILQ_FOREACH(interp, interps, next) {
        interp_argv[0] = interp->str;

        log_debug("Attempting to execute interpreter %s", interp_argv[0]);

        execvp(interp_argv[0], interp_argv);
        if (errno == ENOENT) {
            // ENOENT isn't necessarily an error case (there are legitimate reasons for any given
            // interpreter not to exist), hence logging this at info level rather than error.
            log_info("%s does not exist or could not be executed", interp_argv[0]);
        } else {
            log_error("Failed to execute %s: %s", interp_argv[0], strerror(errno));
        }
    }

    log_fatal("Failed to execute any interpreters in the interpreter search path");

    return 1;
}
