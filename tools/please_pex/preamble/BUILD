subinclude(
    "///cc//build_defs:c",
    "///go//build_defs:go",
)

c_binary(
    name = "preamble",
    srcs = glob(["*.c"]),
    hdrs = glob(["*.h"]),
    compiler_flags = ["-std=c11"],
    defines = [
        # path.c relies on realpath(3)'s resolved_path == NULL feature, which was not standardised
        # until POSIX.1-2008:
        "_XOPEN_SOURCE=700",
    ],
    static = True,
    visibility = [
        "//tools/please_pex/pex:preamble",
    ],
    deps = [
        "///third_party/cc/cjson/cjson//:cjson",
        "///third_party/cc/kuba_zip/kuba_zip//:kuba_zip",
        "///third_party/cc/log_c/log_c//:log_c",
        "//third_party/cc/openbsd:queue",
    ],
)

go_library(
    name = "preamble_go",
    srcs = glob(["*.go"]),
    visibility = [
        "//tools/please_pex/pex",
        "//tools/please_pex:pex_main",
    ],
)
