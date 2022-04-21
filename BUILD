subinclude("//build_defs:version")

version(name = "version")

remote_file(
    name = "please",
    url = f"https://get.please.build/{CONFIG.OS}_{CONFIG.ARCH}/{CONFIG.PLZ_VERSION}/please_{CONFIG.PLZ_VERSION}",
    binary = True,
    test_only = True,
    visibility = ["PUBLIC"],
)



