subinclude("///cc//build_defs:c")

remote_file(
    name = "queue_h_upstream",
    out = "queue_upstream.h",
    url = "https://raw.githubusercontent.com/openbsd/src/f9d861d10df22eff555a4387e0151a3215209fd1/sys/sys/queue.h",
)

genrule(
    name = "queue_h_patched",
    srcs = [":queue_h_upstream"],
    outs = ["queue.h"],
    # On OpenBSD, sys/_null.h defines NULL if it isn't already defined. NULL is widely defined on the platforms we
    # support, so strip out this include to save ourselves another dependency.
    cmd = "grep -vFx '#include <sys/_null.h>' $SRCS > $OUTS",
)

c_library(
    name = "queue",
    hdrs = [":queue_h_patched"],
    includes = ["."],
    visibility = [
        "//tools/please_pex/preamble/...",
    ],
)
