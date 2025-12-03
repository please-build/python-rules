#ifndef __UTIL_H__

#define __UTIL_H__

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sysexits.h>

#define STREQ(x, y) (strcmp((x), (y)) == 0)
#define STRPREFIX(s, pre) (strncmp(pre, s, strlen(pre)) == 0)

#define NELEMS(x) ((int)(sizeof(x) / sizeof((x)[0])))

#define MALLOC(ptr, type, size)                            \
    if (((ptr) = malloc(sizeof(type) * (size))) == NULL) { \
        perror("malloc");                                  \
        exit(EX_OSERR);                                    \
    }

#define FREE(x) if ((x) != NULL) { free(x); (x) = NULL; }

/*
 * STAILQ_NEW allocates memory for and initialises a singly-linked tail queue.
 */
#define STAILQ_NEW(headname, type) \
    MALLOC(headname, type, 1);     \
    (*headname) = (type){ 0 };     \
    STAILQ_INIT(headname);

/*
 * STAILQ_ENTRY_NEW allocates memory for and initialises an entry in a singly-linked tail queue.
 */
#define STAILQ_ENTRY_NEW(var, type) \
    MALLOC(var, type, 1); \
    (*var) = (type){ 0 };

typedef struct strlist_elem_t {
    char *str;
    STAILQ_ENTRY(strlist_elem_t) next;
} strlist_elem_t;

STAILQ_HEAD(strlist_t, strlist_elem_t);

typedef struct strlist_t strlist_t;

#endif /* !__UTIL_H__ */
