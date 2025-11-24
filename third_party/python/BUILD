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
    name = "xmlrunner",
    package_name = "unittest_xml_reporting",
    licences = ["BSD-2-Clause"],
    version = "3.2.0",
)

python_wheel(
    name = "six",
    outs = ["six.py"],
    licences = ["MIT"],
    hashes = ["8abb2f1d86890a2dfb989f9a77cfcfd3e47c2a354b01111771326f8aa26e0254"],
    version = "1.16.0",
)

python_wheel(
    name = "requests",
    hashes = [
        "43999036bfa82904b6af1d99e4882b560e5e2c68e5c4b0aa03b655f3d7d73fee",
    ],
    licences = ["Apache-2.0"],
    test_only = True,
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
    licences = ["MPL-2.0"],
    hashes = ["017c25db2a153ce562900032d5bc68e9f191e44e9a0f762f373977de9df1fbb3"],
    test_only = True,
    version = "2019.11.28",
)

python_wheel(
    name = "chardet",
    hashes = ["fc323ffcaeaed0e0a02bf4d117757b98aed530d9ed4531e3e15460124c106691"],
    licences = ["LGPL-2.1-only"],
    test_only = True,
    version = "3.0.4",
)

python_wheel(
    name = "idna",
    hashes = ["a068a21ceac8a4d63dbfd964670474107f541babbd2250d61922f029858365fa"],
    licences = ["BSD-3-Clause"],
    test_only = True,
    version = "2.9",
)

python_wheel(
    name = "urllib3",
    hashes = ["0ed14ccfbf1c30a9072c7ca157e4319b70d65f623e91e7b32fadb2853431016e"],
    licences = ["MIT"],
    test_only = True,
    version = "1.26.20",
)

python_wheel(
    name = "dateutil",
    package_name = "python_dateutil",
    hashes = ["961d03dc3453ebbc59dbdea9e4e11c5651520a876d0f4db161e8674aae935da9"],
    test_only = True,  # Not used by plz itself.
    licences = ["BSD-3-Clause"],
    version = "2.8.2",
    deps = [":six"],
)

python_wheel(
    name = "protobuf",
    outs = ["google"],
    licences = ["BSD-3-Clause"],
    version = "3.19.4",
    deps = [":six"],
)

_coverage_version = "7.11.3"

_coverage_tags = {
    "darwin_amd64": {
        "macosx_10_9_x86_64": [
            ["cp310", "cp310"],
            ["cp311", "cp311"],
        ],
        "macosx_10_13_x86_64": [
            ["cp312", "cp312"],
            ["cp313", "cp313"],
            ["cp313", "cp313t"],
        ],
        "macosx_10_15_x86_64": [
            ["cp314", "cp314"],
            ["cp314", "cp314t"],
        ],
    },
    "darwin_arm64": {
        "macosx_11_0_arm64": [
            ["cp310", "cp310"],
            ["cp311", "cp311"],
            ["cp312", "cp312"],
            ["cp313", "cp313"],
            ["cp313", "cp313t"],
            ["cp314", "cp314"],
            ["cp314", "cp314t"],
        ],
    },
    "linux_amd64": {
        "manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64": [
            ["cp310", "cp310"],
            ["cp311", "cp311"],
            ["cp312", "cp312"],
            ["cp313", "cp313"],
            ["cp313", "cp313t"],
            ["cp314", "cp314"],
            ["cp314", "cp314t"],
        ],
        "musllinux_1_2_x86_64": [
            # The SOABI used by musl-linked Python 3.10 interpreters is "x86_64-linux-gnu", making it
            # indistinguishable from the SOABI used by glibc-linked interpreters (and causing file name
            # collisions for the tracer shared object in the multi-arch wheel). Because of this, we aren't
            # able to provide native-speed tracing support for musl-linked Python 3.10 interpreters.
            ["cp311", "cp311"],
            ["cp312", "cp312"],
            ["cp313", "cp313"],
            ["cp313", "cp313t"],
            ["cp314", "cp314"],
            ["cp314", "cp314t"],
        ],
    },
    "linux_arm64": {
        "manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64": [
            ["cp310", "cp310"],
            ["cp311", "cp311"],
            ["cp312", "cp312"],
            ["cp313", "cp313"],
            ["cp313", "cp313t"],
            ["cp314", "cp314"],
            ["cp314", "cp314t"],
        ],
        "musllinux_1_2_aarch64": [
            # The SOABI used by musl-linked Python 3.10 interpreters is "x86_64-linux-gnu", making it
            # indistinguishable from the SOABI used by glibc-linked interpreters (and causing file name
            # collisions for the tracer shared object in the multi-arch wheel). Because of this, we aren't
            # able to provide native-speed tracing support for musl-linked Python 3.10 interpreters.
            # interpreters.
            ["cp311", "cp311"],
            ["cp312", "cp312"],
            ["cp313", "cp313"],
            ["cp313", "cp313t"],
            ["cp314", "cp314"],
            ["cp314", "cp314t"],
        ],
    },
    # There are no pre-built architecture-specific wheels for FreeBSD, so fall back to the pure-Python one.
    # This means that native-speed tracing support is unavailable on FreeBSD.
    "other": {
        "any": [
            ["py3", "none"],
        ],
    },
}

python_multiversion_wheel(
    name = "coverage",
    urls = [
        f"https://files.pythonhosted.org/packages/{python}/c/coverage/coverage-{_coverage_version}-{python}-{abi}-{platform}.whl"
        for platform, t in _coverage_tags.get(f"{CONFIG.OS}_{CONFIG.HOSTARCH}", _coverage_tags.get("other")).items()
        for python, abi in t
    ],
    licences = ["Apache-2.0"],
    version = _coverage_version,
)

python_wheel(
    name = "pluggy",
    hashes = ["d89c696a773f8bd377d18e5ecda92b7a3793cbe66c87060a6fb58c7b6e1061f7"],
    licences = ["MIT"],
    version = "1.3.0",
)

python_wheel(
    name = "py",
    hashes = ["607c53218732647dff4acdfcd50cb62615cedf612e72d1724fb1a0cc6405b378"],
    licences = ["MIT"],
    version = "1.11.0",
)

python_wheel(
    name = "packaging",
    hashes = [],
    licences = [
        "Apache-2.0",
        "BSD-2-Clause",
    ],
    version = "24.1",
)

pip_library(
    name = "wheel_filename",
    licences = ["MIT"],
    version = "1.3.0",
)

python_wheel(
    name = "pytest",
    outs = [
        "_pytest",
        "pytest",
    ],
    hashes = ["1d881c6124e08ff0a1bb75ba3ec0bfd8b5354a01c194ddd5a0a870a48d99b002"],
    licences = ["MIT"],
    version = "7.4.2",
    deps = [
        ":colorama",
        ":exceptiongroup",
        ":iniconfig",
        ":packaging",
        ":pluggy",
        # Not a formal dependency, but pytest uses this version instead of its vendorised copy if it
        # is installed, and the hack that makes the vendorised copy work doesn't play nicely with
        # pex archives - see https://github.com/pytest-dev/pytest/pull/10396
        ":py",
        ":tomli",
    ],
)

python_wheel(
    name = "exceptiongroup",
    hashes = ["343280667a4585d195ca1cf9cef84a4e178c4b6cf2274caef9859782b567d5e3"],
    licences = [
        "MIT",
        "PSF-2.0",
    ],
    version = "1.1.3",
)

python_wheel(
    name = "iniconfig",
    licences = ["MIT"],
    version = "1.1.1",
)

python_wheel(
    name = "behave",
    outs = [
        "behave",
    ],
    hashes = ["ebda1a6c9e5bfe95c5f9f0a2794e01c7098b3dde86c10a95d8621c5907ff6f1c"],
    licences = ["BSD-2-Clause"],
    version = "1.2.6",
    deps = [
        ":colorama",
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
    licences = ["MIT"],
    version = "1.15.0",
)

python_wheel(
    name = "parse_type",
    hashes = ["089a471b06327103865dfec2dd844230c3c658a4a1b5b4c8b6c16c8f77577f9e"],
    licences = ["MIT"],
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
    licences = ["MIT"],
    version = "0.5",
)

python_wheel(
    name = "colorama",
    hashes = ["7d73d2a99753107a36ac6b455ee49046802e59d9d076ef8e47b61499fa29afff"],
    licences = ["BSD-3-Clause"],
    version = "0.4.3",
)

python_wheel(
    name = "absl",
    package_name = "absl_py",
    hashes = ["c106f6ef0ae86c1273b0858b40ee15b99fad1c223838387b9d11446a033bbcb1"],
    licences = ["Apache-2.0"],
    version = "0.9.0",
    deps = [":six"],
)

python_wheel(
    name = "portalocker",
    hashes = ["874d6063c6ceb185fe4771da41b01872d2c56d292db746698f8ad7bf1833c905"],
    licences = ["BSD-3-Clause"],
    version = "1.7.0",
)

pip_library(
    name = "google-pasta",
    test_only = True,
    licences = ["Apache-2.0"],
    version = "0.2.0",
    deps = [
        ":six",
    ],
)

pip_library(
    name = "setuptools",
    test_only = True,
    licences = ["MIT"],
    version = "47.1.1",
)

pip_library(
    name = "googleapis_common_protos",
    package_name = "googleapis-common-protos",
    test_only = True,
    licences = ["Apache-2.0"],
    version = "1.52.0",
    deps = [
        ":protobuf_pip",
    ],
)

pip_library(
    name = "protobuf_pip",
    package_name = "protobuf",
    test_only = True,
    licences = ["BSD-3-Clause"],
    version = "3.12.2",
    deps = [
        ":setuptools",
        ":six",
    ],
)

pip_library(
    name = "progress",
    licences = ["ISC"],
    version = "1.5",
)

pip_library(
    name = "distlib",
    licences = ["PSF-2.0"],
    version = "0.3.8",
)

python_wheel(
    name = "debugpy",
    hashes = ["f058c204341fd7ff800ee0edafc106ca0fb1c9857e8a8895a6e04cca3ddcb7bf"],
    licences = ["MIT"],
    version = "1.5.0",
)

python_wheel(
    name = "tomli",
    hashes = ["939de3e7a6161af0c887ef91b7d41a53e7c5a1ca976325f429cb46ea9bc30ecc"],
    licences = ["MIT"],
    version = "2.0.1",
)

# This is the minimum set of third-party packages required for the built-in test runners to work
# with "plz test" and "plz cover". All built-in test runners should include this as a source.
python_library(
    name = "test_bootstrap",
    deps = [
        ":coverage",
        ":portalocker",
    ],
)

python_library(
    name = "unittest_bootstrap",
    deps = [
        ":test_bootstrap",
        ":xmlrunner",
    ],
)

python_library(
    name = "pytest_bootstrap",
    deps = [
        ":pytest",
        ":test_bootstrap",
    ],
)

python_library(
    name = "behave_bootstrap",
    deps = [
        ":behave",
        ":test_bootstrap",
    ],
)

# Note: this is used by //test:distribution_metadata_test as an example of a module that contains
# distribution metadata. The importlib.metadata API should be able to identify the version of the
# module from the contents of its .dist-info directory. The choice of module isn't that important,
# and is fairly arbitrary - it just happens to be widely-used, written in pure Python, and has no
# dependencies.

python_wheel(
    name = "pygments",
    outs = [
        "pygments",
        "pygments-2.18.0.dist-info",
    ],
    hashes = ["b8e6aca0523f3ab76fee51799c488e38782ac06eafcf95e7ba832985c8e7b13a"],
    licences = ["BSD-2-Clause"],
    test_only = True,
    version = "2.18.0",
    visibility = [
        "//test:distribution_metadata_test",
    ],
)

# Note: this package is used for //test:name_scheme_test as an example of something using a list of
# name schemes
python_wheel(
    name = "click",
    hashes = [],
    licences = ["BSD-3-Clause"],
    version = "8.1.7",
    deps = [],
)

# Note: this package is used for //test:name_scheme_test as an example of something using a single
# string name scheme.
python_wheel(
    name = "click-log",
    package_name = "click_log",
    outs = ["click_log"],
    hashes = [],
    licences = ["MIT"],
    name_scheme = "{url_base}/ae/5a/4f025bc751087833686892e17e7564828e409c43b632878afeae554870cd/{package_name}-{version}-py2.py3-none-any.whl",
    repo = "https://files.pythonhosted.org/packages",
    version = "0.4.0",
    deps = [],
)

pip_library(
    name = "confluent-kafka",
    licences = ["Apache-2.0"],
    version = "2.6.1",
    test_only = True,
    zip_safe = False,
)
