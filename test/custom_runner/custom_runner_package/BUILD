package(
    python = {
        "TEST_RUNNER": "test.custom_runner.runner.run",
        "TEST_RUNNER_BOOTSTRAP": "//test/custom_runner:runner",
    },
)

python_test(
    name = "custom_runner_test",
    srcs = ["custom_runner_test.py"],
)
