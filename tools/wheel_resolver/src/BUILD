subinclude("//build_defs:python")

python_binary(
    name = "resolve",
    main = "resolve.py",
    visibility = ["PUBLIC"],
    deps = [
        "//third_party/python:argparse",
        "//third_party/python:distlib",
        "//third_party/python:packaging",
        "//tools/wheel_resolver/src/wheel_tags:tags",
    ],
)
