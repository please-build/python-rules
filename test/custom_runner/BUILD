subinclude("//build_defs:python")

python_library(
    name = "runner",
    srcs = ["runner.py"],
    visibility = ["//test/custom_runner/..."],
    deps = [
        "//third_party/python:coverage",
        "//third_party/python:pytest",
    ],
)
