package(
    python = {
        "TEST_RUNNER": "test.custom_runner.runner.run",
        "TESTRUNNER_DEPS": "@self//test/custom_runner:runner",
    },
)

python_test(
    name = "custom_runner_test",
    srcs = ["custom_runner_test.py"],
)
