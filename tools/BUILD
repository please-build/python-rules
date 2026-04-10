_PLEASE_PEX_VERSION = "3.0.2"

remote_file(
    name = "please_pex",
    url = f"https://github.com/please-build/python-rules/releases/download/please_pex-v{_PLEASE_PEX_VERSION}/please_pex-{_PLEASE_PEX_VERSION}-{CONFIG.OS}_{CONFIG.ARCH}",
    hashes = [
        "b9049a96aaead27f83e713d4d9f60b2b9a30411c7479722bec0e67254016b4a9",  # darwin_amd64
        "ba5868b241dc136509d827db6a6a65b71a5b9d003f9dbf439777467d5cd3ebd5",  # darwin_arm64
        "26f8624d81036f3672a2280e6937b04ef1a54ebde041f61e5b34b6837df24817",  # freebsd_amd64
        "1ee0046ed5c2a8b3300a36510ac76dd15eb2b6e9dc494313eda698987467bcac",  # linux_amd64
        "a20e952208b421d12a4ebd5ef313cbe4ee740de51a975e739a758b30bc39cb9f",  # linux_arm64
    ],
    binary = True,
    visibility = ["PUBLIC"],
)
