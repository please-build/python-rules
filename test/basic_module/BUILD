subinclude("//build_defs:python")

python_library(
    name = "library",
    srcs = ["library.py"],
)

python_test(
    name = "library_test",
    srcs = ["library_test.py"],
    deps = [":library"],
)
