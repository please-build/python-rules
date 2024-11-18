subinclude("//build_defs:version")

version(name = "version")

TOOLS_VERSION = "1.5.4"

remote_file(
    name = "please_pex",
    url = f"https://github.com/please-build/python-rules/releases/download/tools-v{TOOLS_VERSION}/please_pex-{TOOLS_VERSION}-{CONFIG.OS}_{CONFIG.ARCH}",
    hashes = [
        "f8c19359244f2470c6832a5ba6b19ae43cd5482be305b3a0177b44c02ab46121",  # please_pex-1.5.4-darwin_amd64
        "4a64e768e4620182457feeb8cd7f5707efacc404b7af41d46996e56d467fbed1",  # please_pex-1.5.4-darwin_arm64
        "bc0cddb71e3d16607f9e6fcb0fd7465e2863720c5659fc8fdf2d69311a083043",  # please_pex-1.5.4-freebsd_amd64
        "6396b005313a29326a610e9de20e87a25670131dafcf5018be85f23c3a31f8d9",  # please_pex-1.5.4-linux_amd64
        "85f5d0096008021cea952b51f839d8a3689040a2fd2e3d46b06e3da8314a3f5e",  # please_pex-1.5.4-linux_arm64
    ],
    binary = True,
    visibility = ["PUBLIC"],
)

# This target is only intended for use during plugin development. Its only purpose is to break the
# mutual dependency between please_pex and the python_wheels in the bootstrap pex, which prevents
# PexTool from being set to //tools/please_pex in order to test changes to please_pex.
#
# See .plzconfig.tool_test for more details.
filegroup(
    name = "please_pex_dev",
    srcs = ["please_pex_dev"],
    binary = True,
    labels = ["manual"],
    visibility = ["PUBLIC"],
)
