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
    version = "1.14.0",
)

python_wheel(
    name = "requests",
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
    version = "2019.11.28",
)

python_wheel(
    name = "chardet",
    version = "3.0.4",
)

python_wheel(
    name = "idna",
    version = "2.9",
)

python_wheel(
    name = "urllib3",
    version = "1.25.8",
)

python_wheel(
    name = "colorlog",
    version = "4.1.0",
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

if is_platform(
    arch = "amd64",
    os = "linux",
):
    urls = [
        "https://files.pythonhosted.org/packages/2f/19/4ebe9fe7006d46dd56eacd8cdc800b465590037bffeea17852520613cfaf/coverage-5.5-cp35-cp35m-manylinux2010_x86_64.whl",
        "https://files.pythonhosted.org/packages/42/37/a82863f91b41711203277ea286bc37915063f4d1be179ac34b591bf6d8a5/coverage-5.5-cp36-cp36m-manylinux2010_x86_64.whl",
        "https://files.pythonhosted.org/packages/16/e0/fc9f7bd9b84e6b41d0aad1a113e36714aac0c0a9b307aca5f9af443bc50f/coverage-5.5-cp37-cp37m-manylinux2010_x86_64.whl",
        "https://files.pythonhosted.org/packages/a4/3a/8f7b217265503eae2b0ea97e714e2709e1e84ee13cd3ca6abdff1e99e76c/coverage-5.5-cp38-cp38-manylinux2010_x86_64.whl",
        "https://files.pythonhosted.org/packages/a4/79/625f1ed5da2a69f52fb44e0b7ca1b470437ff502348c716005a98a71cd49/coverage-5.5-cp39-cp39-manylinux2010_x86_64.whl",
        "https://files.pythonhosted.org/packages/d4/3e/4f6451b8b09a1eb2d0e7f61a3d7019bd98d556fc5343378f76e8905b2789/coverage-5.5-cp310-cp310-manylinux1_x86_64.whl",
    ]
elif is_platform(
    arch = "amd64",
    os = "darwin",
):
    urls = [
        "https://files.pythonhosted.org/packages/9f/16/7e0972f8495f6a1b81cfa6579eead931d63dd445e8ecb3114b04a0e36af2/coverage-5.5-cp35-cp35m-macosx_10_9_x86_64.whl",
        "https://files.pythonhosted.org/packages/fd/2b/ab03276eb127f8ec7f1cf1499c77944321b125d89859ab51ee7d9f46475f/coverage-5.5-cp36-cp36m-macosx_10_9_x86_64.whl",
        "https://files.pythonhosted.org/packages/52/44/5df49f3b462a0f5818a2f6f206d6523ff21ff9b21c1eb2906f8a31aa321c/coverage-5.5-cp37-cp37m-macosx_10_9_x86_64.whl",
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
    version = "19.3.0",
)

python_wheel(
    name = "pluggy",
    version = "0.13.1",
    deps = [":importlib_metadata"],
)

python_wheel(
    name = "importlib_metadata",
    outs = [
        "importlib_metadata",
        "importlib_metadata-1.5.0.dist-info",
    ],
    patch = "importlib_metadata.patch",
    version = "1.5.0",
    deps = [":zipp"],
)

python_wheel(
    name = "zipp",
    outs = ["zipp.py"],
    version = "3.1.0",
)

python_wheel(
    name = "py",
    version = "1.8.1",
)

python_wheel(
    name = "funcsigs",
    version = "1.0.2",
)

python_wheel(
    name = "pkg_resources",
    package_name = "setuptools",
    version = "57.0.0",
)

python_wheel(
    name = "packaging",
    version = "20.1",
)

pip_library(
    name = "wheel_filename",
    version = "1.3.0",
)

python_wheel(
    name = "more_itertools",
    version = "8.2.0",
)

python_wheel(
    name = "pytest",
    outs = [
        "_pytest",
        "pytest",
    ],
    version = "7.1.3",
    deps = [
        ":attrs",
        ":funcsigs",
        ":more_itertools",
        ":packaging",
        ":pkg_resources",
        ":pluggy",
        ":py",
        ":six",
        ":wcwidth",
        ":iniconfig",
    ],
    entry_points="pytest:main",
)

python_wheel(
    name = "iniconfig",
    version = "1.1.1",
)

python_wheel(
    name = "wcwidth",
    version = "0.2.5",
)

python_wheel(
    name = "behave",
    outs = [
        "behave",
    ],
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
    entry_points = {
        "behave": "behave.__main__:main",
        "behave_test": "setuptools_behave:behave_test",
    }
)

python_wheel(
    name = "parse",
    outs = [
        "parse.py",
    ],
    version = "1.15.0",
)

python_wheel(
    name = "parse_type",
    version = "0.5.2",
)

python_wheel(
    name = "traceback2",
    licences = ["PSF"],
    version = "1.4.0",
)

python_wheel(
    name = "win_unicode_console",
    version = "0.5",
)

python_wheel(
    name = "enum34",
    outs = ["enum"],
    version = "1.1.9",
)

python_wheel(
    name = "colorama",
    version = "0.4.3",
)

python_wheel(
    name = "absl",
    package_name = "absl_py",
    version = "0.9.0",
    deps = [":six"],
)

python_wheel(
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
    licences = ["MIT"],
    version = "1.5.0",
)

python_wheel(
    name = "typing_extensions",
    outs = ["typing_extensions.py"],
    version = "4.4.0",
)

python_wheel(
    name = "mypy_extensions",
    outs = ["mypy_extensions.py"],
    version = "0.4.3",
)

python_wheel(
    name = "tomli",
    version = "2.0.1",
)

python_wheel(
    name = "mypy",
    version = "0.982",
    deps = [":typing_extensions", ":mypy_extensions", ":tomli"],
    binary=True,
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
        ":funcsigs",
        ":importlib_metadata",
        ":more_itertools",
        ":packaging",
        ":pkg_resources",
        ":pluggy",
        ":py",
        ":pytest",
        ":six",
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

if is_platform(
    arch = "amd64",
    os = "linux",
):
    urls = [
        "https://files.pythonhosted.org/packages/2f/19/4ebe9fe7006d46dd56eacd8cdc800b465590037bffeea17852520613cfaf/coverage-5.5-cp35-cp35m-manylinux2010_x86_64.whl",
        "https://files.pythonhosted.org/packages/42/37/a82863f91b41711203277ea286bc37915063f4d1be179ac34b591bf6d8a5/coverage-5.5-cp36-cp36m-manylinux2010_x86_64.whl",
        "https://files.pythonhosted.org/packages/16/e0/fc9f7bd9b84e6b41d0aad1a113e36714aac0c0a9b307aca5f9af443bc50f/coverage-5.5-cp37-cp37m-manylinux2010_x86_64.whl",
        "https://files.pythonhosted.org/packages/a4/3a/8f7b217265503eae2b0ea97e714e2709e1e84ee13cd3ca6abdff1e99e76c/coverage-5.5-cp38-cp38-manylinux2010_x86_64.whl",
        "https://files.pythonhosted.org/packages/a4/79/625f1ed5da2a69f52fb44e0b7ca1b470437ff502348c716005a98a71cd49/coverage-5.5-cp39-cp39-manylinux2010_x86_64.whl",
    ]
elif is_platform(
    arch = "amd64",
    os = "darwin",
):
    urls = [
        "https://files.pythonhosted.org/packages/9f/16/7e0972f8495f6a1b81cfa6579eead931d63dd445e8ecb3114b04a0e36af2/coverage-5.5-cp35-cp35m-macosx_10_9_x86_64.whl",
        "https://files.pythonhosted.org/packages/fd/2b/ab03276eb127f8ec7f1cf1499c77944321b125d89859ab51ee7d9f46475f/coverage-5.5-cp36-cp36m-macosx_10_9_x86_64.whl",
        "https://files.pythonhosted.org/packages/52/44/5df49f3b462a0f5818a2f6f206d6523ff21ff9b21c1eb2906f8a31aa321c/coverage-5.5-cp37-cp37m-macosx_10_9_x86_64.whl",
        "https://files.pythonhosted.org/packages/b6/26/b53bf0fef1b4bce6f7d61fef10fbf924d943987d4c9e53c394ecebff3673/coverage-5.5-cp38-cp38-macosx_10_9_x86_64.whl",
        "https://files.pythonhosted.org/packages/0d/8a/3b13c4e1f241a7083a4ee9986b969f0238f41dcd7a8990c786bc3b4b5b19/coverage-5.5-cp39-cp39-macosx_10_9_x86_64.whl",
    ]
else:
    urls = [
        "https://files.pythonhosted.org/packages/93/ac/02bc6a60304a8a58383386f7675f6ebae0d2f49f162dda318e57bd95c746/coverage-5.5-pp37-none-any.whl",
    ]

