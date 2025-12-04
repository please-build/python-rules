_PLEASE_PEX_VERSION = "3.0.1"

remote_file(
    name = "please_pex",
    url = f"https://github.com/please-build/python-rules/releases/download/please_pex-v{_PLEASE_PEX_VERSION}/please_pex-{_PLEASE_PEX_VERSION}-{CONFIG.OS}_{CONFIG.ARCH}",
    hashes = [
        "4f3f18bae50653efac7d2f86fffbe4611f58af2fe5a53cbd7906fa69016a6a90",  # darwin_amd64
        "456cb9256cbc08eb8a39698ac4c3ebea2478c8e181c03fd2ed6eb153cc111f16",  # darwin_arm64
        "b4843318d2ee1bd639b44ca1003845445fe5d561711772ffcfe1fb31ae387ff4",  # freebsd_amd64
        "f1d3aa335af9e5058f90d25dfd473ceb01bb88a5e3ee1ffaceec047e5983ae6b",  # linux_amd64
        "a460892f2c9466bec1f06407b049e783f62e7868e229e089672efeafeb4c0379",  # linux_arm64
    ],
    binary = True,
    visibility = ["PUBLIC"],
)
