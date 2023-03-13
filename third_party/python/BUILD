subinclude("//build_defs:python")

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
    version = "2.11.0",
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
        ":packaging",
        ":protobuf",
        ":requests",
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
    name = "dateutil",
    package_name = "python_dateutil",
    test_only = True,  # Not used by plz itself.
    version = "2.8.2",
    deps = [":six"],
)

python_wheel(
    name = "protobuf",
    outs = ["google"],
    version = "3.19.4",
    deps = [":six"],
)

pip_library(
    name = "coverage",
    version = "7.2.1",
)

pip_library(
    name = "attrs",
    version = "21.2.0",
)

pip_library(
    name = "pluggy",
    licences = ["MIT"],
    version = "0.13.1",
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

pip_library(
    name = "exceptiongroup",
    version = "1.1.1",
)

pip_library(
    name = "iniconfig",
    version = "2.0.0",
)

pip_library(
    name = "tomli",
    version = "2.0.1",
)

pip_library(
    name = "pytest",
    version = "7.2.2",
    deps = [
        ":attrs",
        ":exceptiongroup",
        ":iniconfig",
        ":packaging",
        ":pluggy",
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
    version = "1.23.4",
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
    version = "1.49.1",
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
    version = "3.7.0",
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
    version = "1.5.0",
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
    version = "1.9.2",
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
    name = "wcwidth",
    licences = ["MIT"],
    version = "0.2.6",
)

filegroup(
    name = "unittest_bootstrap",
    deps = [
        ":coverage",
        ":portalocker",
        ":six",
        ":xmlrunner",
    ],
)

filegroup(
    name = "pytest_bootstrap",
    deps = [
        ":attrs",
        ":coverage",
        ":funcsigs",
        ":importlib_metadata",
        ":more_itertools",
        ":packaging",
        ":pkg_resources",
        ":pluggy",
        ":py",
        ":pytest",
        ":six",
        ":wcwidth",
        ":zipp",
    ],
)

filegroup(
    name = "behave_bootstrap",
    deps = [
        ":behave",
        ":coverage",
        ":parse",
        ":parse_type",
        ":six",
    ],
)
