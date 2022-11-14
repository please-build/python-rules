subinclude(
    "//build_defs:multiversion_wheel",
    "//build_defs:python",
)

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

python_wheel(
    name = "tensorflow",
    licences = ["Apache 2.0"],
    test_only = True,
    version = "2.6.0",
    deps = [
        ":absl",
        ":astunparse",
        ":flatbuffers",
        ":gast",
        ":google-pasta",
        ":grpcio",
        ":keras_applications",
        ":keras_preprocessing",
        ":numpy",
        ":opt_einsum",
        ":protobuf",
        ":termcolor",
        ":typing_extensions",
        ":wrapt",
    ],
)

python_wheel(
    name = "flatbuffers",
    test_only = True,
    version = "2.0",
)

python_wheel(
    name = "astunparse",
    test_only = True,
    version = "1.6.3",
)

python_wheel(
    name = "typing_extensions",
    package_name = "typing-extensions",
    outs = ["typing_extensions.py"],
    test_only = True,
    version = "3.10.0.2",
)

python_wheel(
    name = "xmlrunner",
    package_name = "unittest_xml_reporting",
    version = "1.11.0",
    deps = [":six"],
)

pip_library(
    name = "six",
    version = "1.14.0",
)

python_wheel(
    name = "requests",
    hashes = [
        "43999036bfa82904b6af1d99e4882b560e5e2c68e5c4b0aa03b655f3d7d73fee",
    ],
    version = "2.23.0",
    deps = [
        ":certifi",
        ":chardet",
        ":idna",
        ":urllib3",
    ],
)

python_wheel(
    name = "certifi",
    hashes = ["017c25db2a153ce562900032d5bc68e9f191e44e9a0f762f373977de9df1fbb3"],
    version = "2019.11.28",
)

python_wheel(
    name = "chardet",
    hashes = ["fc323ffcaeaed0e0a02bf4d117757b98aed530d9ed4531e3e15460124c106691"],
    version = "3.0.4",
)

python_wheel(
    name = "idna",
    hashes = ["a068a21ceac8a4d63dbfd964670474107f541babbd2250d61922f029858365fa"],
    version = "2.9",
)

python_wheel(
    name = "urllib3",
    hashes = ["2f3db8b19923a873b3e5256dc9c2dedfa883e33d87c690d9c7913e1f40673cdc"],
    version = "1.25.8",
)

python_wheel(
    name = "colorlog",
    hashes = ["732c191ebbe9a353ec160d043d02c64ddef9028de8caae4cfa8bd49b6afed53e"],
    version = "4.1.0",
)

python_wheel(
    name = "dateutil",
    package_name = "python_dateutil",
    hashes = ["5179fabb692e3ec5a6e994eb9a72a6f4498f19106774672fd7e664a7aa9f49c3"],
    test_only = True,  # Not used by plz itself.
    version = "2.4.0",
    deps = [":six"],
)

python_wheel(
    name = "protobuf",
    outs = ["google"],
    version = "3.19.4",
    deps = [":six"],
)

if is_platform(
    arch = "amd64",
    os = "linux",
):
    urls = [
        "https://files.pythonhosted.org/packages/0d/ef/8735875a8dc09e1c4e484a5436c8b4148731b70daccc6f203c50b05e7505/coverage-6.5.0-cp37-cp37m-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl",
        "https://files.pythonhosted.org/packages/bd/a0/e263b115808226fdb2658f1887808c06ac3f1b579ef5dda02309e0d54459/coverage-6.5.0-cp38-cp38-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl",
        "https://files.pythonhosted.org/packages/6b/f2/919f0fdc93d3991ca074894402074d847be8ac1e1d78e7e9e1c371b69a6f/coverage-6.5.0-cp39-cp39-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl",
        "https://files.pythonhosted.org/packages/3c/7d/d5211ea782b193ab8064b06dc0cc042cf1a4ca9c93a530071459172c550f/coverage-6.5.0-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl",
        "https://files.pythonhosted.org/packages/6a/63/8e82513b7e4a1b8d887b4e85c1c2b6c9b754a581b187c0b084f3330ac479/coverage-6.5.0-cp311-cp311-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl",
    ]
elif is_platform(
    arch = "amd64",
    os = "darwin",
):
    urls = [
        "https://files.pythonhosted.org/packages/61/a6/af54588e2091693026df94b09106ee10dcbcdc8c9b2c3989149e6e44a324/coverage-6.5.0-cp37-cp37m-macosx_10_9_x86_64.whl",
        "https://files.pythonhosted.org/packages/05/63/a789b462075395d34f8152229dccf92b25ca73eac05b3f6cd75fa5017095/coverage-6.5.0-cp38-cp38-macosx_10_9_x86_64.whl",
        "https://files.pythonhosted.org/packages/ea/52/c08080405329326a7ff16c0dfdb4feefaa8edd7446413df67386fe1bbfe0/coverage-6.5.0-cp39-cp39-macosx_10_9_x86_64.whl",
        "https://files.pythonhosted.org/packages/c4/8d/5ec7d08f4601d2d792563fe31db5e9322c306848fec1e65ec8885927f739/coverage-6.5.0-cp310-cp310-macosx_10_9_x86_64.whl",
        "https://files.pythonhosted.org/packages/50/cf/455930004231fa87efe8be06d13512f34e070ddfee8b8bf5a050cdc47ab3/coverage-6.5.0-cp311-cp311-macosx_10_9_x86_64.whl",
    ]
else:
    urls = [
        "https://files.pythonhosted.org/packages/6e/e6/b31a4b2aa9489da59b35ee0ea4259d6fe9b321a1eaa6492f19342d03d53b/coverage-6.5.0-pp36.pp37.pp38-none-any.whl",
    ]

python_multiversion_wheel(
    name = "coverage",
    urls = urls,
    version = "6.5.0",
)

pip_library(
    name = "attrs",
    version = "19.3.0",
)

pip_library(
    name = "pluggy",
    version = "0.13.1",
    licences = ["MIT"],
    deps = [":importlib_metadata"],
)

pip_library(
    name = "importlib_metadata",
    version = "1.5.0",
    deps = [":zipp"],
)

pip_library(
    name = "zipp",
    version = "3.1.0",
)

pip_library(
    name = "py",
    version = "1.8.1",
)

pip_library(
    name = "funcsigs",
    version = "1.0.2",
)

pip_library(
    name = "pkg_resources",
    package_name = "setuptools",
    version = "57.0.0",
)

pip_library(
    name = "packaging",
    version = "21.3",
    deps = [
        ":pyparsing",
    ],
)

pip_library(
    name = "wheel_filename",
    version = "1.3.0",
)

pip_library(
    name = "pyparsing",
    version = "2.4.7",
)

pip_library(
    name = "more_itertools",
    version = "8.2.0",
)

python_wheel(
    name = "exceptiongroup",
    version = "1.0.1",
)

python_wheel(
    name = "iniconfig",
    version = "1.1.1",
)

python_wheel(
    name = "tomli",
    version = "2.0.1",
)

pip_library(
    name = "pytest",
    version = "7.2.0",
    deps = [
        ":attrs",
        ":exceptiongroup",
        ":importlib_metadata",
        ":iniconfig",
        ":packaging",
        ":pkg_resources",
        ":pluggy",
        ":py",
        ":tomli",
    ],
)

pip_library(
    name = "behave",
    version = "1.2.6",
    deps = [
        ":colorama",
        ":enum34",
        ":parse",
        ":parse_type",
        ":six",
        ":traceback2",
        ":win_unicode_console",
    ],
)

pip_library(
    name = "parse",
    version = "1.15.0",
)

pip_library(
    name = "parse_type",
    version = "0.5.2",
)

pip_library(
    name = "traceback2",
    licences = ["PSF"],
    version = "1.4.0",
)

pip_library(
    name = "enum34",
    version = "1.1.9",
)

pip_library(
    name = "win_unicode_console",
    version = "0.5",
)

pip_library(
    name = "colorama",
    version = "0.4.3",
)

python_wheel(
    name = "absl",
    package_name = "absl_py",
    hashes = ["c106f6ef0ae86c1273b0858b40ee15b99fad1c223838387b9d11446a033bbcb1"],
    version = "0.9.0",
    deps = [":six"],
)

pip_library(
    name = "portalocker",
    version = "1.7.0",
)

pip_library(
    name = "numpy",
    test_only = True,
    version = "1.18.4",
    zip_safe = False,
)

pip_library(
    name = "keras_applications",
    test_only = True,
    version = "1.0.8",
    deps = [
        ":h5py",
    ],
)

pip_library(
    name = "opt_einsum",
    test_only = True,
    version = "3.2.1",
    deps = [
        ":numpy",
    ],
)

pip_library(
    name = "keras_preprocessing",
    test_only = True,
    version = "1.1.0",
    deps = [
        ":numpy",
        ":six",
    ],
)

pip_library(
    name = "grpcio",
    test_only = True,
    version = "1.32.0",
    deps = [
        ":six",
    ],
)

pip_library(
    name = "google-pasta",
    test_only = True,
    version = "0.2.0",
    deps = [
        ":six",
    ],
)

pip_library(
    name = "gast",
    test_only = True,
    version = "0.2.2",
)

pip_library(
    name = "astor",
    test_only = True,
    version = "0.8.1",
)

pip_library(
    name = "termcolor",
    test_only = True,
    version = "1.1.0",
)

pip_library(
    name = "wrapt",
    test_only = True,
    version = "1.12.1",
)

pip_library(
    name = "h5py",
    test_only = True,
    version = "2.10.0",
    deps = [
        ":numpy",
        ":six",
    ],
)

pip_library(
    name = "pytz",
    test_only = True,
    version = "2018.4",
)

pip_library(
    name = "pandas",
    test_only = True,
    version = "1.0.3",
    deps = [
        ":dateutil",
        ":numpy",
        ":pytz",
        ":six",
    ],
)

pip_library(
    name = "setuptools",
    test_only = True,
    version = "47.1.1",
)

pip_library(
    name = "scipy",
    test_only = True,
    version = "1.5.2",
    zip_safe = False,
    deps = [
        ":numpy",
        ":setuptools",
    ],
)

pip_library(
    name = "googleapis_common_protos",
    package_name = "googleapis-common-protos",
    test_only = True,
    version = "1.52.0",
    deps = [
        ":protobuf_pip",
    ],
)

pip_library(
    name = "protobuf_pip",
    package_name = "protobuf",
    test_only = True,
    version = "3.12.2",
    deps = [
        ":setuptools",
        ":six",
    ],
)

pip_library(
    name = "progress",
    version = "1.5",
)

pip_library(
    name = "cx_oracle",
    package_name = "cx-Oracle",
    version = "8.2.1",
)

pip_library(
    name = "argparse",
    version = "1.4.0",
)

pip_library(
    name = "distlib",
    version = "0.3.2",
)

pip_library(
    name = "debugpy",
    licences = ["MIT"],
    version = "1.5.0",
)

filegroup(
    name = "unittest_bootstrap",
    srcs = [
        ":coverage",
        ":portalocker",
        ":six",
        ":xmlrunner",
    ],
)

filegroup(
    name = "pytest_bootstrap",
    srcs = [
        ":attrs",
        ":exceptiongroup",
        ":importlib_metadata",
        ":iniconfig",
        ":packaging",
        ":pkg_resources",
        ":pluggy",
        ":py",
        ":pytest",
        ":tomli",
        ":zipp",
    ],
)

filegroup(
    name = "behave_bootstrap",
    srcs = [
        ":behave",
        ":parse",
        ":parse_type",
        ":six",
    ],
)
