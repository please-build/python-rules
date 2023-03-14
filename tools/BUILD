subinclude("//build_defs:version")

version(name = "version")

TOOLS_VERSION = "1.1.0"

remote_file(
    name = "please_pex",
    url = f"https://github.com/please-build/python-rules/releases/download/tools-v{TOOLS_VERSION}/please_pex-{TOOLS_VERSION}-{CONFIG.HOSTOS}_{CONFIG.HOSTARCH}",
    hashes = [
        "6e022add5cc4c6b16e309909b44d63b21beb480576a8d7e00e64b556825d141d", # linux_amd64
        "cd88d726e832815d56fba86ab1c58904eb14c5eb86f71fdba7a61aee0a5656bb", # linux_arm64
        "11652bfae931930c1dc7e870f4ff5656ce33df2ef288d39fac4afdb98d73f626", # darwin_amd64
        "9d78d85f47552f124e36420de7b68a2cab79b32b9c8dbd49ce3bac2e7db17bc5", # darwin_arm64
        "702bd7ea28aa312c8e3584db1e22bfec557f8dc9227c54f94aca8f555c8f8014", # freebsd_amd64
    ],
    binary = True,
    visibility = ["PUBLIC"],
)
