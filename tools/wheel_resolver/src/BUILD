package(
    default_visibility = ["PUBLIC"],
    python_wheel_name_scheme = [
        "{url_base}/{package_name}-{version}-${{OS}}_${{ARCH}}.whl",
        "{url_base}/{package_name}-{version}.whl",
        "https://files.pythonhosted.org/packages/py3/{initial}/{package_name}/{package_name}-{version}-py3-none-any.whl",
        "https://files.pythonhosted.org/packages/py2.py3/{initial}/{package_name}/{package_name}-{version}-py2.py3-none-any.whl",
    ],
    python_wheel_repo = "https://get.please.build/third_party/python/py3",
)

python_binary(
    name = "resolve",
    main = "resolve.py",
    deps = [
        "//src/tags:tags",
        "//third_party/python:argparse",
    ],
)
