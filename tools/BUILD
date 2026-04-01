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

_WHEEL_RESOLVER_VERSION = "2.0.0"

remote_file(
    name = "wheel_resolver",
    url =
    f"https://github.com/please-build/python-rules/releases/download/wheel_resolver-v{_WHEEL_RESOLVER_VERSION}/wheel_resolver-{_WHEEL_RESOLVER_VERSION}-{CONFIG.OS}_{CONFIG.ARCH}",
    hashes = [
        "b48315ec1c6670faf7feb2a532a4d0cb104a03113525ef1799062d7576f66b36",  # darwin_amd64
        "70db6d2eb18ab915f555824a8f29fe0909bcf87db0b583a5d6ad3156a54a034a",  # darwin_arm64
        "d47802282b4acf1669a1d69531c69eb2dd3f0f069fd8e59d0c9aff946f7aff44",  # freebsd_amd64
        "6aa0304bde5ab5f68d3415fd8761f6684f5c88835791b0dbd12f909120d797c6",  # linux_amd64
        "09e340203aa88d4e9de7f61b044d1f29fb688abf3c8b7547f80ad6ca3e441495",  # linux_arm64
    ],
    binary = True,
    visibility = ["PUBLIC"],
)
