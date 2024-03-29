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
    name = "xmlrunner",
    package_name = "unittest_xml_reporting",
    version = "1.11.0",
    deps = [":six"],
)

python_wheel(
    name = "six",
    outs = ["six.py"],
    hashes = ["8f3cd2e254d8f793e7f3d6d9df77b92252b52637291d0f0da013c76ea2724b6c"],
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
    hashes = ["961d03dc3453ebbc59dbdea9e4e11c5651520a876d0f4db161e8674aae935da9"],
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

if is_platform(
    arch = "amd64",
    os = "linux",
):
    urls = [
        "https://files.pythonhosted.org/packages/a4/3a/8f7b217265503eae2b0ea97e714e2709e1e84ee13cd3ca6abdff1e99e76c/coverage-5.5-cp38-cp38-manylinux2010_x86_64.whl",
        "https://files.pythonhosted.org/packages/a4/79/625f1ed5da2a69f52fb44e0b7ca1b470437ff502348c716005a98a71cd49/coverage-5.5-cp39-cp39-manylinux2010_x86_64.whl",
        "https://files.pythonhosted.org/packages/d4/3e/4f6451b8b09a1eb2d0e7f61a3d7019bd98d556fc5343378f76e8905b2789/coverage-5.5-cp310-cp310-manylinux1_x86_64.whl",
    ]
elif is_platform(
    arch = "amd64",
    os = "darwin",
):
    urls = [
        "https://files.pythonhosted.org/packages/b6/26/b53bf0fef1b4bce6f7d61fef10fbf924d943987d4c9e53c394ecebff3673/coverage-5.5-cp38-cp38-macosx_10_9_x86_64.whl",
        "https://files.pythonhosted.org/packages/0d/8a/3b13c4e1f241a7083a4ee9986b969f0238f41dcd7a8990c786bc3b4b5b19/coverage-5.5-cp39-cp39-macosx_10_9_x86_64.whl",
        "https://files.pythonhosted.org/packages/6b/a2/43dd30964103a7ff1fd03392a30a5b08105bc85d1bafbfc51023a1bb4fd3/coverage-5.5-cp310-cp310-macosx_10_14_x86_64.whl",
    ]
else:
    urls = [
        "https://files.pythonhosted.org/packages/93/ac/02bc6a60304a8a58383386f7675f6ebae0d2f49f162dda318e57bd95c746/coverage-5.5-pp37-none-any.whl",
    ]

python_multiversion_wheel(
    name = "coverage",
    urls = urls,
    version = "5.5",
)

python_wheel(
    name = "attrs",
    outs = ["attr"],
    hashes = ["08a96c641c3a74e44eb59afb61a24f2cb9f4d7188748e76ba4bb5edfa3cb7d1c"],
    version = "19.3.0",
)

python_wheel(
    name = "pluggy",
    hashes = ["966c145cd83c96502c3c3868f50408687b38434af77734af1e9ca461a4081d2d"],
    version = "0.13.1",
    deps = [":importlib_metadata"],
)

python_wheel(
    name = "importlib_metadata",
    outs = [
        "importlib_metadata",
        "importlib_metadata-6.8.0.dist-info",
    ],
    hashes = ["3ebb78df84a805d7698245025b975d9d67053cd94c79245ba4b3eb694abe68bb"],
    version = "6.8.0",
    deps = [":zipp"],
)

python_wheel(
    name = "zipp",
    outs = ["zipp.py"],
    hashes = ["aa36550ff0c0b7ef7fa639055d797116ee891440eac1a56f378e2d3179e0320b"],
    version = "3.1.0",
)

python_wheel(
    name = "py",
    hashes = ["c20fdd83a5dbc0af9efd622bee9a5564e278f6380fffcacc43ba6f43db2813b0"],
    version = "1.8.1",
)

python_wheel(
    name = "packaging",
    hashes = ["170748228214b70b672c581a3dd610ee51f733018650740e98c7df862a583f73"],
    version = "20.1",
)

pip_library(
    name = "wheel_filename",
    version = "1.3.0",
)

python_wheel(
    name = "pytest",
    outs = [
        "_pytest",
        "pytest",
    ],
    entry_points = "pytest:main",
    hashes = ["130328f552dcfac0b1cec75c12e3f005619dc5f874f0a06e8ff7263f0ee6225e"],
    version = "7.2.2",
    deps = [
        ":attrs",
        ":colorama",
        ":exceptiongroup",
        ":importlib_metadata",
        ":iniconfig",
        ":packaging",
        ":pluggy",
        # This is a stealth dependency (see src/_pytest/compat.py):
        ":py",
        ":tomli",
    ],
)

python_wheel(
    name = "exceptiongroup",
    hashes = ["232c37c63e4f682982c8b6459f33a8981039e5fb8756b2074364e5055c498c9e"],
    version = "1.1.1",
)

python_wheel(
    name = "iniconfig",
    version = "1.1.1",
)

python_wheel(
    name = "behave",
    outs = [
        "behave",
    ],
    entry_points = {
        "behave": "behave.__main__:main",
        "behave_test": "setuptools_behave:behave_test",
    },
    hashes = ["ebda1a6c9e5bfe95c5f9f0a2794e01c7098b3dde86c10a95d8621c5907ff6f1c"],
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

python_wheel(
    name = "parse",
    outs = [
        "parse.py",
    ],
    hashes = ["2bb9c56c65bf609abbbef372bdcdd7b9c163745e7daf5e8217dba50a55850510"],
    version = "1.15.0",
)

python_wheel(
    name = "parse_type",
    hashes = ["089a471b06327103865dfec2dd844230c3c658a4a1b5b4c8b6c16c8f77577f9e"],
    version = "0.5.2",
)

python_wheel(
    name = "traceback2",
    hashes = ["8253cebec4b19094d67cc5ed5af99bf1dba1285292226e98a31929f87a5d6b23"],
    licences = ["PSF"],
    version = "1.4.0",
)

python_wheel(
    name = "win_unicode_console",
    hashes = ["7a7fb8bf98bcacb328d1f607065c0f89107c7e8f4b02caf12e5f02fb462512a6"],
    version = "0.5",
)

python_wheel(
    name = "enum34",
    outs = ["enum"],
    hashes = ["708aabfb3d5898f99674c390d360d59efdd08547019763622365f19e84a7fef4"],
    version = "1.1.9",
)

python_wheel(
    name = "colorama",
    hashes = ["7d73d2a99753107a36ac6b455ee49046802e59d9d076ef8e47b61499fa29afff"],
    version = "0.4.3",
)

python_wheel(
    name = "absl",
    package_name = "absl_py",
    hashes = ["c106f6ef0ae86c1273b0858b40ee15b99fad1c223838387b9d11446a033bbcb1"],
    version = "0.9.0",
    deps = [":six"],
)

python_wheel(
    name = "portalocker",
    hashes = ["874d6063c6ceb185fe4771da41b01872d2c56d292db746698f8ad7bf1833c905"],
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

python_wheel(
    name = "debugpy",
    hashes = ["f058c204341fd7ff800ee0edafc106ca0fb1c9857e8a8895a6e04cca3ddcb7bf"],
    licences = ["MIT"],
    version = "1.5.0",
)

python_wheel(
    name = "typing_extensions",
    outs = ["typing_extensions.py"],
    hashes = ["sha256: 16fa4864408f655d35ec496218b85f79b3437c829e93320c7c9215ccfd92489e"],
    version = "4.4.0",
)

python_wheel(
    name = "mypy_extensions",
    outs = ["mypy_extensions.py"],
    hashes = ["sha256: 090fedd75945a69ae91ce1303b5824f428daf5a028d2f6ab8a299250a846f15d"],
    version = "0.4.3",
)

python_wheel(
    name = "tomli",
    hashes = ["sha256: 939de3e7a6161af0c887ef91b7d41a53e7c5a1ca976325f429cb46ea9bc30ecc"],
    version = "2.0.1",
)

python_wheel(
    name = "mypy",
    binary = True,
    hashes = ["sha256: 1021c241e8b6e1ca5a47e4d52601274ac078a89845cfde66c6d5f769819ffa1d"],
    version = "0.982",
    deps = [
        ":mypy_extensions",
        ":tomli",
        ":typing_extensions",
    ],
)

# This is the minimum set of third-party packages required for the built-in test runners to work
# with "plz test" and "plz cover". All built-in test runners should include this as a source.
filegroup(
    name = "test_bootstrap",
    deps = [
        ":coverage",
        ":portalocker",
    ],
)

filegroup(
    name = "unittest_bootstrap",
    deps = [
        ":test_bootstrap",
        ":xmlrunner",
    ],
)

filegroup(
    name = "pytest_bootstrap",
    deps = [
        ":pytest",
        ":test_bootstrap",
    ],
)

filegroup(
    name = "behave_bootstrap",
    deps = [
        ":behave",
        ":test_bootstrap",
    ],
)
