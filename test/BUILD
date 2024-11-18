subinclude("//build_defs:python", "///shell//build_defs:shell")

package(
    default_visibility = ["PUBLIC"],
    python = {
        "WHEEL_REPO": "https://get.please.build/third_party/python/py3",
        "WHEEL_NAME_SCHEME": [
            "{url_base}/{package_name}-{version}-${{OS}}_${{ARCH}}.whl",
            "{url_base}/{package_name}-{version}.whl",
            "https://files.pythonhosted.org/packages/py3/{initial}/{package_name}/{package_name}-{version}-py3-none-any.whl",
            "https://files.pythonhosted.org/packages/py2.py3/{initial}/{package_name}/{package_name}-{version}-py2.py3-none-any.whl",
        ],
    },
)

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
        "py2",
        "py3",
    ],
)

python_test(
    name = "python3_coverage_test",
    srcs = ["python_coverage_test.py"],
    labels = ["py3"],
    deps = [":python_coverage"],
)

python_test(
    name = "unittest_unicode_test",
    srcs = ["unittest_unicode_test.py"],
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

plz_e2e_test(
    name = "correct_labels_on_pip_libary_non_zip_safe",
    cmd = "plz query print -f labels //third_party/python:pyyaml",
    expected_output = "expected_labels_on_pyyaml.txt",
    labels = ["py3"],
    deps = ["//third_party/python:pyyaml"],
)

plz_e2e_test(
    name = "correct_labels_on_pip_libary_zip_safe",
    cmd = "plz query print -f labels //third_party/python:grpcio",
    expected_output = "expected_labels_on_grpcio.txt",
    labels = ["py3"],
    deps = ["//third_party/python:grpcio"],
)

# Test that python_wheel targets can have name_scheme as a list or a string

python_test(
    name = "name_scheme_test",
    srcs = ["name_scheme_test.py"],
    labels = [
        "py3",
    ],
    deps = [
        "//third_party/python:click",
        "//third_party/python:click-log",
    ],
)

python_test(
    name = "distribution_metadata_test",
    srcs = ["distribution_metadata_test.py"],
    deps = [
        "//third_party/python:google-pasta",
        "//third_party/python:pygments",
    ],
)

# This test need only run in the GitHub Actions workflow - it is skipped outside this environment.
python_test(
    name = "ci_test",
    srcs = ["ci_test.py"],
)

python_test(
    name = "interpreter_not_included_test",
    srcs = ["interpreter_not_included_test.py"],
)

python_test(
    name = "module_dir_import_test",
    srcs = ["module_dir_import_test.py"],
    deps = [
        "//third_party/python:six",
    ],
)
