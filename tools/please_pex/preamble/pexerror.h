#ifndef __PEXERROR_H__

#define __PEXERROR_H__

#include "queue.h"

typedef struct errmsg_t {
    /*
     * len is the length of the diagnostic message stored in msg. It excludes the trailing null.
     */
    size_t len;

    /*
     * flen is the expected length of the error chain with this error at its head when it is
     * formatted by err_str. It is the length of the diagnostic message in this error plus the
     * lengths of the diagnostic messages stored in each of the errors wrapped by this error, with
     * an additional two bytes per wrapped error to account for the ": " separator that err_str
     * inserts between diagnostic messages.
     */
    size_t flen;

    /*
     * msg is a diagnostic message describing this error.
     */
    const char *msg;

    /*
     * wrapped is an error that is wrapped by this error.
     */
    SLIST_ENTRY(errmsg_t) wrapped;
} errmsg_t;

SLIST_HEAD(err_t, errmsg_t);

typedef struct err_t err_t;

err_t *err_from_str(const char *msg);
err_t *err_from_errno(const char *msg);
err_t *err_wrap(const char *msg, err_t *wrapped);
char *err_str(err_t *err);

#endif /* __PEXERROR_H__ */
