subinclude("//build_defs:version")

version(name = "version")

TOOLS_VERSION = "1.3.2"

remote_file(
    name = "please_pex",
    url = f"https://github.com/please-build/python-rules/releases/download/tools-v{TOOLS_VERSION}/please_pex-{TOOLS_VERSION}-{CONFIG.OS}_{CONFIG.ARCH}",
    hashes = [
        "f5562504462f47de0e6026fb0e93f9b49bc8efda5d55313f0ef89c95216c07a4", # darwin_amd64
        "a77c053fe3d0a315510dbfe1f5d6d0971221a82a0dc1311403f492b6918d5296", # darwin_arm64
        "f87b5d633ace75548e188b4ea7a8b0e4f84ec8a364dd692900b216a281e76985", # freebsd_amd64
        "87900fbd31a84a7d3ed226bf431b22f5000730231102029eadae8aade090dd75", # linux_amd64
        "3bcfc1846bcbc2b7ccb221062c37b416b0ca9cd4deedac630bc89746f20d47d2", # linux_arm64
    ],
    binary = True,
    visibility = ["PUBLIC"],
)
