subinclude("//build_defs:python")

python_test(
    name = "isolated_custom_runner_test",
    srcs = ["custom_runner_test.py"],
    test_runner = "test.custom_runner.runner.run",
    deps = [
        "//test/custom_runner:runner",
    ],
)
