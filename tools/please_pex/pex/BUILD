subinclude("///go//build_defs:go")

go_library(
    name = "pex",
    srcs = ["pex.go"],
    resources = glob(["**/*.py"]) + [":preamble"],
    visibility = [
        "//tools/please_pex:all",
    ],
    deps = [
        "//tools/please_pex/preamble:preamble_go",
        "//tools/please_pex/zip",
    ],
)

genrule(
    name = "preamble",
    srcs = ["//tools/please_pex/preamble"],
    outs = ["preamble"],
    cmd = "cp $SRCS $OUTS",
)
