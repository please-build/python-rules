subinclude("//build_defs:version")

version(name = "version")

v = CONFIG.PLZ_VERSION.lstrip(">=")

remote_file(
    name = "please",
    binary = True,
    test_only = True,
    url = f"https://get.please.build/{CONFIG.OS}_{CONFIG.ARCH}/{v}/please_{v}",
    visibility = ["PUBLIC"],
)

export_file(
    name = "plzconfig",
    src = ".plzconfig",
    test_only = True,
    visibility = [
        "//test:python-rules",
    ],
)
