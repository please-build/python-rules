subinclude("//build_defs:multiversion_wheel")

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
    }
)

python_wheel(
    name = "xmlrunner",
    package_name = "unittest_xml_reporting",
    hashes = ["4ba8380f99daf6fe951dea05f05977bc4129ca71da8303971b05e7e8ce917f97"],
    version = "1.11.0",
    deps = [":six"],
)

python_wheel(
    name = "six",
    outs = ["six.py"],
    hashes = ["43a5af1176750c6100480a370863422642afdad3f2f3191298af951c4f4f6080"],
    version = "1.14.0",
)

python_wheel(
    name = "requests",
    hashes = [
        "7e6a997b42711956d686dee0d70147cf3b3642c15bcc92e92519eb127e3b7f7c",
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
    hashes = ["4b5b9b468d636e6377a274c1f38dcb1a83592604e903110f372a0df427937a20"],
    version = "2019.11.28",
)

python_wheel(
    name = "chardet",
    hashes = ["ba7fb63d251415bb1734efebcfc455774a29a3dc14df0f6d034fb28d29bdae23"],
    version = "3.0.4",
)

python_wheel(
    name = "idna",
    hashes = ["59e58591cbcf013ada32c9b5a3ba4e685665c28c478e58daaca10a3ab099ce2b"],
    version = "2.9",
)

python_wheel(
    name = "urllib3",
    hashes = ["47a4b1a45db1de13ed07255fa450ef0fe1cb1e6fd44d4577f6e6ad13f4bf987a"],
    version = "1.25.8",
)

python_wheel(
    name = "colorlog",
    hashes = ["bab0dcf03e070e892eb24b7f09dec4f7cbde01a210c64a9f87a51d61c0cc4795"],
    version = "4.1.0",
)

python_wheel(
    name = "dateutil",
    package_name = "python_dateutil",
    hashes = [
        "94234e68e7cf65f3ab564cc4016451f6027feddc3a02bd922dfb5489569efcfc",
    ],
    test_only = True,  # Not used by plz itself.
    version = "2.4.0",
    deps = [":six"],
)

python_wheel(
    name = "protobuf",
    outs = ["google"],
    version = "3.12.2",
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

python_multiversion_wheel(
    name = "coverage",
    urls = urls,
    version = "5.5",
)

python_wheel(
    name = "attrs",
    outs = ["attr"],
    hashes = ["ddca8fa00b22a7fd62d6c323eb02b18bd6f01f2b52b4ed50c142827767f510de"],
    version = "19.3.0",
)

python_wheel(
    name = "pluggy",
    hashes = ["2314ad55aac0e64ef27539f7361210aa1ee8b4a601df531588667930f589e3e0"],
    version = "0.13.1",
    deps = [":importlib_metadata"],
)

python_wheel(
    name = "importlib_metadata",
    outs = [
        "importlib_metadata",
        "importlib_metadata-1.5.0.dist-info",
    ],
    hashes = ["1f82ea14a86b67b3e813967184170f34e5f6513ef1ecced1be9ceff504e9817e"],
    patch = "importlib_metadata.patch",
    version = "1.5.0",
    deps = [":zipp"],
)

python_wheel(
    name = "zipp",
    outs = ["zipp.py"],
    hashes = ["a3c5b6e577e84790c3fe4ac440b6d8acd3262bec76e89bdaa9e2ae6e80bdd586"],
    version = "3.1.0",
)

python_wheel(
    name = "py",
    hashes = ["d8293c54e3874bfd9ed890bb4d65dae6078b15553e458691b9e7bc1440b88043"],
    version = "1.8.1",
)

python_wheel(
    name = "funcsigs",
    hashes = ["83f5f538df41456b089a81b1abfe555610767e0d66bf713ecdfc407cdc21c961"],
    version = "1.0.2",
)

pip_library(
    name = "pkg_resources",
    package_name = "setuptools",
    hashes = ["99066f1746e7488d9dfd2549ba8dadd13aecd78a207312adba600352d0678c0c"],
    version = "57.0.0",
)

pip_library(
    name = "packaging",
    hashes = ["d51acb3f5b8e7b35d34c04a5a284da70dab9f2120b6f4dd6b11b89374483a213"],
    version = "21.0",
    deps = [
        ":pyparsing",
    ],
)

pip_library(
    name = "pyparsing",
    version = "2.4.7",
)

python_wheel(
    name = "more_itertools",
    hashes = ["d47a527c30c860b0dd5c50548214f4e4a9464bb576477980fb9b9a54b66a98b8"],
    version = "8.2.0",
)

python_wheel(
    name = "pytest",
    outs = [
        "_pytest",
        "pytest",
    ],
    hashes = ["cb1b6342414fa7649bcb4596248f82fc34b0c1dcc709072c1d1456c9288654b9"],
    version = "5.4.3",
    deps = [
        ":attrs",
        ":funcsigs",
        ":more_itertools",
        ":packaging",
        ":pkg_resources",
        ":pluggy",
        ":py",
        ":six",
    ],
)

python_wheel(
    name = "behave",
    outs = [
        "behave",
    ],
    hashes = ["ba833cd2e30ec590f794d5ca39a4fb598ac623a0e566418f6d3245fb5c5dc527"],
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
    hashes = ["846dc21590052bbc27a3d7fe16511cc0eac466fce711e46d543af23709b7bb8e"],
    version = "1.15.0",
)

python_wheel(
    name = "parse_type",
    hashes = ["78ac7bf899d97ed64c433e0bd919f8374fe8fee148fe240f61ceee596e1abe4b"],
    version = "0.5.2",
)

python_wheel(
    name = "traceback2",
    hashes = ["eeacf7e8ccd8ab8e150648613a305c87c1b9ae2e2d56b45b517db0ad4eef7464"],
    licences = ["PSF"],
    version = "1.4.0",
)

python_wheel(
    name = "enum34",
    outs = ["enum"],
    hashes = ["c6a6e303100059d0079c60a4cffdeac09eccfeb826e40507285d1ad5558b0395"],
    version = "1.1.9",
)

python_wheel(
    name = "win_unicode_console",
    hashes = ["6dae3f3f83ff396b3e603b29e9af364387c6c31e229864ff6eec5350d353432f"],
    version = "0.5",
)

python_wheel(
    name = "colorama",
    hashes = ["4bce685ba74e3e8ee0f83b85e313d45c7408c29a523c0535809bb3f341c2494f"],
    version = "0.4.3",
)

python_wheel(
    name = "absl",
    package_name = "absl_py",
    hashes = ["75496a0389de88af171d43181aef60a4c0a240664630a072821a60eddd0a6768"],
    version = "0.9.0",
    deps = [":six"],
)

python_wheel(
    name = "portalocker",
    hashes = ["10cc527c840b49c4f0d2762da9077d15eb1f194de030471b09650a6814d0badc"],
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

