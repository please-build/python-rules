subinclude("//build_defs:python")

python_binary(
    name = "strip_source",
    main = "strip_source.py",
    strip = True,
)

python_test(
    name = "strip_source_test",
    srcs = ["strip_source_test.py"],
    data = [":strip_source"],
    labels = ["py3"],
)

# Test that has no actual tests in it. Should still count as a pass.

# Test that the build rules accept a python_binary that has a rule as the main.
filegroup(
    name = "rule_main",
    srcs = ["rule_main.py"],
)

python_binary(
    name = "rule_main_pex",
    main = ":rule_main",
)

# Test that we don't generate coverage on running a test normally (because it's slower)
python_test(
    name = "_no_coverage_output_test",
    srcs = ["coverage_output_test.py"],
)

plz_e2e_test(
    name = "no_coverage_output_test",
    cmd = "plz test //test:_no_coverage_output_test",
    expect_file_doesnt_exist = "../../../bin/test/.test_coverage__no_coverage_output_test*",
    labels = ["python3"],
)

sh_test(
    name = "rule_main_test",
    src = "rule_main_test.sh",
    data = [":rule_main_pex"],
    labels = ["python3"],
)

# Test flags on python_test
python_test(
    name = "flags_test",
    srcs = ["flags_test.py"],
    flags = "--test_flag",
)

# Tests for a subtle case where python_test rules should get a pex when
# specified as data, but not when depending directly.
python_binary(
    name = "data_dep",
    main = "data_dep.py",
)

python_test(
    name = "data_dep_test",
    srcs = ["data_dep_test.py"],
    data = [":data_dep"],
    deps = [":data_dep"],
)

python_test(
    name = "data_dep_only_test",
    srcs = ["data_dep_only_test.py"],
    data = [":data_dep"],
)

python_library(
    name = "python_coverage",
    srcs = ["python_coverage.py"],
    labels = [
        "py3",
    ],
)

python_test(
    name = "python_coverage_test",
    srcs = ["python_coverage_test.py"],
    labels = ["py3"],
    deps = [":python_coverage"],
)

python_test(
    name = "unittest_unicode_test",
    srcs = ["unittest_unicode_test.py"],
)

python_test(
    name = "numpy_test",
    srcs = ["numpy_test.py"],
    labels = [
        "py3",
        "pip",
    ],
    deps = ["//third_party/python:numpy"],
)

python_test(
    name = "namespaced_packages_test",
    srcs = ["namespaced_packages_test.py"],
    labels = [
        "py3",
        "pip",
    ],
    deps = [
        "//third_party/python:googleapis_common_protos",
        "//third_party/python:protobuf_pip",
    ],
)

python_test(
    name = "pandas_test",
    srcs = ["pandas_test.py"],
    labels = [
        "py3",
        "pip",
    ],
    deps = ["//third_party/python:pandas"],
)

python_test(
    name = "scipy_test",
    srcs = ["scipy_test.py"],
    labels = [
        "py3",
        "pip",
    ],
    deps = ["//third_party/python:scipy"],
)

python_test(
    name = "worker_test",
    srcs = ["worker_test.py"],
    worker = "//test/workers:worker",
)

python_test(
    name = "importlib_metadata_test",
    srcs = ["importlib_metadata_test.py"],
    labels = [
        "py3",
        "pip",
    ],
    deps = ["//third_party/python:importlib_metadata"],
)

python_test(
    name = "data_dict_test",
    srcs = ["data_dict_test.py"],
    data = {"txt": ["data.txt"]},
    labels = ["py3"],
)

python_test(
    name = "cx_oracle_darwin_build_test",
    srcs = ["cx_oracle_darwin_build_test.py"],
    labels = [
        "py3",
        "pip",
    ],
    deps = ["//third_party/python:cx_oracle"],
)

# There's no wheel naming scheme in here so this
# will use the wheel_resolver tool
gentest(
    name = "simple_wheel_resolver_test",
    srcs = [":cryptography"],
    no_test_output = True,
    test_cmd = "true",
)

python_wheel(
    name = "cryptography",
    package_name = "cryptography",
    version = "35.0.0",
)

plz_e2e_test(
    name = "correct_labels_on_pip_library_non_zip_safe",
    cmd = "plz query print -f labels //third_party/python:numpy",
    expected_output = "expected_labels_on_numpy.txt",
    labels = ["py3"],
    deps = ["//third_party/python:numpy"],
)

plz_e2e_test(
    name = "correct_labels_on_pip_library_zip_safe",
    cmd = "plz query print -f labels //third_party/python:grpcio",
    expected_output = "expected_labels_on_grpcio.txt",
    labels = ["py3"],
    deps = ["//third_party/python:grpcio"],
)

python_test(
    name = "tensorflow_test",
    srcs = ["tensorflow_test.py"],
    labels = [
        "py3",
        "pip",
    ],
    deps = ["//third_party/python:tensorflow"],
)
