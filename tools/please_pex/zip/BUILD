subinclude("///go//build_defs:go")

go_library(
    name = "zip",
    srcs = ["writer.go"],
    visibility = [
        "//tools/jarcat:all",
        "//tools/please_pex/pex",
    ],
    deps = [
        # "//src/fs",
        "//third_party/go:go-logging.v1",
        "//third_party/go:testify",
    ],
)

go_test(
    name = "writer_test",
    srcs = ["writer_test.go"],
    data = [
        "test_data",
        "test_data_2",
        "test_data_3",
    ],
    deps = [
        ":zip",
    ],
)
