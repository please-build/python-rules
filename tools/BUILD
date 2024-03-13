subinclude("//build_defs:version")

version(name = "version")

TOOLS_VERSION = "1.2.1"

remote_file(
    name = "please_pex",
    url = f"https://github.com/please-build/python-rules/releases/download/tools-v{TOOLS_VERSION}/please_pex-{TOOLS_VERSION}-{CONFIG.OS}_{CONFIG.ARCH}",
    hashes = [
        "ed45827dfee333a4ce664a5482d4868fee34d0108634a7ab6022b0d270bbd8cc", # linux_amd64
        "9e25438fa199063e189cfb28ada30aa2d37276d3643dd62a0bf14c07213bb2b2", # linux_arm64
        "ccb7cb58dd7df88f7a50ee0f5490c3a7990142f010107a93233f08903b6a1f2f", # darwin_amd64
        "969f1477b66aef94653699ecd5f386fc0499e6631a0aad6fd3e5d9eb96dd34ac", # darwin_arm64
        "0d22f1687d9cf7edc19a7d1f475d6449020c8ca33de4fac2a2b105e71e17a6e1", # freebsd_amd64
    ],
    binary = True,
    visibility = ["PUBLIC"],
)
