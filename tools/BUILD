subinclude("//build_defs:version")

version(name = "version")

TOOLS_VERSION = "1.4.0"

remote_file(
    name = "please_pex",
    url = f"https://github.com/please-build/python-rules/releases/download/tools-v{TOOLS_VERSION}/please_pex-{TOOLS_VERSION}-{CONFIG.OS}_{CONFIG.ARCH}",
    hashes = [
        "171d950d477bbedce427c95bd4f695a738b2f3e50eff86f1f69d9edfcc957bc6", # please_pex-1.4.0-darwin_amd64
        "00c8fbdb50ec056283aeacd6e987d30bd574e3c276be61973bbc4456db3ad421", # please_pex-1.4.0-darwin_arm64
        "760f6686fcd7e1c0852806faf8a099d9ce84daa24f940cb0984a8e86a217f76e", # please_pex-1.4.0-freebsd_amd64
        "1660607eb3e6a91dd1acfcb614f086379a2cac02cc29528d1a89aff16224d73f", # please_pex-1.4.0-linux_amd64
        "d9b75cf9364890ceda0adebdea4db8562ebab80dd896fadf100fbb5aaf107dae", # please_pex-1.4.0-linux_arm64
    ],
    binary = True,
    visibility = ["PUBLIC"],
)
