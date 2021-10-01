python_test(
    name = "lib_test",
    srcs = ["test.py"],
    deps = ["//tools/wheel_resolver/src/wheel_tags:tags"],
)

python_test(
    name = "cross_compile_test",
    srcs = ["cross_compile_test.py"],
    deps = ["//tools/wheel_resolver/src/wheel_tags:tags"],
    labels = ["manual"],
)

python_test(
    name = "e2e_test",
    srcs = ["e2e_tests.py"],
    deps = ["//tools/wheel_resolver/src/e2e_test:e2e_test"],
)
