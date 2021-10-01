python_test(
    name = "lib_test",
    srcs = ["test.py"],
    deps = ["//src/tags:tags"],
)

python_test(
    name = "cross_compile_test",
    srcs = ["cross_compile_test.py"],
    deps = ["//src/tags:tags"],
)

gentest(
    name = "six_with_version_test",
    test_cmd = "plz run //src:resolve -- --package six --version 1.16.0",
    no_test_output = True,
)

gentest(
    name = "tensorflow_no_version_test",
    test_cmd = "plz run //src:resolve -- --package tensorflow",
    no_test_output = True,
)

gentest(
    name = "list_of_archs_test",
    test_cmd = "plz run //src:resolve -- --package six --arch none any",
    no_test_output = True,
)
