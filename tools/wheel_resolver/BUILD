subinclude("//build_defs:python")

python_binary(
    name = "wheel_resolver",
    main = "resolve.py",
    deps = [
        "//third_party/python:argparse",
        "//third_party/python:distlib",
        "//third_party/python:packaging",
        "//tools/wheel_resolver/wheel_tags:tags",
    ],
    visibility = ["PUBLIC"],
)
