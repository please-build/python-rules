subinclude("//build_defs:python")

package(
    python = {
        "TEST_RUNNER": "pytest",
        "TESTRUNNER_DEPS": "//third_party/python:pytest_bootstrap",
    },
)

python_library(
    name = "inc",
    srcs = ["inc.py"],
)

python_library(
    name = "relative_imports",
    srcs = glob(["relative_imports/*"]),
)

python_test(
    name = "test_relative_imports",
    srcs = ["test_relative_imports.py"],
    deps = [
        ":relative_imports",
    ],
)

python_test(
    name = "pytest_test",
    srcs = ["test_runner.py"],
    deps = [":inc"],
)

python_test(
    name = "test_pytest_unicode",
    srcs = ["test_pytest_unicode.py"],
)
