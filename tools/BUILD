subinclude("//:version")

remote_file(
    name = "please_pex",
    url = f"https://github.com/please-build/python-rules/releases/download/v{VERSION}/please_pex-{VERSION}-{CONFIG.HOSTOS}_{CONFIG.HOSTARCH}",
    hashes = [
        "28abdae0d17ca666663563f9b874ddfae0c5209389271d933945003c0ce9d6ab",
        "3c621e8ff11301b64c7a0ca84ba23161fd5c777e4df82034060925f5106ee317",
        "917e6ff3591f6bca5cfc2a251f136c180d743856bee877dc18626cc135bbe7a0",
        "9c20d867ec1a1fcea85481d4a29ec80f8af5923fc06c7ad0057105918ec3e236",
        "ab3426a82ab4cb5c5b0a4979a4a3821eb10361726759e30ab5f2a1e7c09fc78e",
    ],
    binary = True,
    visibility = ["PUBLIC"],
)

remote_file(
    name = "arcat",
    url = f"https://github.com/please-build/arcat/releases/download/v1.0.0/arcat-1.0.0-{CONFIG.HOSTOS}_{CONFIG.HOSTARCH}",
    hashes = ["6705304dde3cf358d7b8f5a034dfcc8242474b76d0e439b2f39a7a99f8612749"],
    binary = True,
    visibility = ["PUBLIC"],
)
