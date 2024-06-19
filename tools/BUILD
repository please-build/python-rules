subinclude("//build_defs:version")

version(name = "version")

TOOLS_VERSION = "1.2.2"

remote_file(
    name = "please_pex",
    url = f"https://github.com/please-build/python-rules/releases/download/tools-v{TOOLS_VERSION}/please_pex-{TOOLS_VERSION}-{CONFIG.OS}_{CONFIG.ARCH}",
    hashes = [
        "aeaebafa96e779786da90efc3f8f0871b086e66b618ecb028a62e471caf1bbda", # linux_amd64
        "f219d26e90468d90b79b2e286c7632f8475d9769e509dbffca394dbec18ea129", # linux_arm64
        "91a1355442be99becb15e3ea1ed4793dedd650c04a8a52e394d39ad516d4395e", # darwin_amd64
        "a358948639d428dd7db8bb86cfc1e2be79bcc1c0aae23b35f5fbc3066b7ac1ea", # darwin_arm64
        "799b6b505fc8c1f2b6c4a0ac8b2b44e2a9be8cb0bc1a5fb461848c56e7c28360", # freebsd_amd64
    ],
    binary = True,
    visibility = ["PUBLIC"],
)
