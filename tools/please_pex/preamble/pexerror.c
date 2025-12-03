/*
 * pexerror.c implements a simple error reporting mechanism.
 *
 * Errors are singly-linked lists (of type err_t) whose nodes (of type errmsg_t) are strings
 * containing diagnostic messages. This allows for the formation of a Go-like error chain, with
 * diagnostic messages becoming progressively more specific as the tail of the list is approached.
 */

#include <errno.h>
#include <stdlib.h>
#include <string.h>
#include <sysexits.h>

#include "pexerror.h"
#include "util.h"

/*
 * err_from_str returns an error from the given diagnostic message.
 */
err_t *err_from_str(const char *msg) {
    err_t *err = NULL;

    MALLOC(err, err_t, 1);
    *err = (err_t){ 0 };
    SLIST_INIT(err);

    return err_wrap(msg, err);
}

/*
 * err_from_errno returns an error from the given diagnostic message that wraps another error
 * whose diagnotic message is derived from the current value of errno.
 *
 * This function is used to report the failure of a system call or library function. Because errno
 * doesn't indicate which system call or library function encountered the error, the diagnostic
 * message passed in msg typically includes the name of the system call or library function.
 *
 * Note that err_from_errno doesn't check that the value of errno is significant; it is therefore
 * the responsibility of the caller to ensure that a system call or library function that sets
 * errno has actually returned a value indicating failure before calling err_from_errno.
 */
err_t *err_from_errno(const char *msg) {
    err_t *err = err_from_str(strerror(errno));

    return err_wrap(msg, err);
}

/*
 * err_wrap creates an error from the given diagnostic message, using it to wrap the given error,
 * and then returns the newly-created error.
 */
err_t *err_wrap(const char *msg, err_t *wrapped) {
    errmsg_t *first = SLIST_FIRST(wrapped);
    errmsg_t *errmsg = NULL;
    size_t len = strlen(msg);

    if (wrapped == NULL) {
        fprintf(stderr, "err_wrap called with null value for wrapped");
        exit(EX_SOFTWARE);
    }

    MALLOC(errmsg, errmsg_t, 1);
    errmsg->msg = msg;
    errmsg->len = len;
    errmsg->flen = len + (first == NULL ? 0 : 2 + first->flen); // 2 extra bytes for ": " separator

    SLIST_INSERT_HEAD(wrapped, errmsg, wrapped);

    return wrapped;
}

/*
 * err_str extracts the diagnostic messages from the given error chain and formats them as a
 * null-terminated string. Messages are included in the returned string in the order in which they
 * appear in the error chain, with successive errors delimited by ": ".
 */
char *err_str(err_t *err) {
    errmsg_t *errmsg = NULL;
    char *catmsg = NULL;
    size_t i = 0;

    errmsg = SLIST_FIRST(err);
    MALLOC(catmsg, char, errmsg->flen + 1); // 1 extra byte for trailing null

    SLIST_FOREACH(errmsg, err, wrapped) {
        strncpy(catmsg + i, errmsg->msg, errmsg->len);
        i += errmsg->len;
        // Don't append ": " to the final error in the list.
        if (errmsg->len != errmsg->flen) {
            strcpy(catmsg + i, ": ");
            i += 2;
        }
    }

    catmsg[i] = 0;

    return catmsg;
}
