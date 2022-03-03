subinclude("//build_defs:python")

go_binary(
    name = "please_pex",
    srcs = ["pex_main.go"],
    deps = [
        "//third_party/go:cli-init",
        "//third_party/go:go-logging.v1",
        "//tools/please_pex/pex",
    ],
    visibility = ["PUBLIC"],
)

python_test(
    name = "pex_test",
    srcs = ["pex_test.py"],
)

python_test(
    name = "pex_import_test",
    srcs = ["pex_import_test.py"],
    deps = [
        "//third_party/python:dateutil",
        "//third_party/python:requests",
    ],
)
