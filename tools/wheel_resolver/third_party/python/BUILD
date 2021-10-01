package(
    default_visibility = ["PUBLIC"],
    python_wheel_repo = "https://get.please.build/third_party/python/py3",
)

pip_library(
    name = "distlib",
    version = "0.3.2",
)

pip_library(
    name = "packaging",
    version = "21.0",
    deps = [
        ":pyparsing",
    ]
)

pip_library(
    name = "pyparsing",
    version = "2.4.7",
)

pip_library(
    name = "wheel-filename",
    version = "1.3.0",
)

pip_library(
    name = "docutils",
    version = "0.17.1",
)

pip_library(
    name = "bleach",
    version = "4.1.0",
    licences = ["..."],
    deps = [
        ":six",
        ":webencodings",
    ]
)

pip_library(
    name = "webencodings",
    version = "0.5.1",
)

pip_library(
    name = "six",
    version = "1.16.0",
)

pip_library(
    name = "argparse",
    version = "1.4.0",
)
