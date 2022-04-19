subinclude("//build_defs:version")

version(name = "version")

remote_file(
    name = "arcat",
    url = f"https://github.com/please-build/arcat/releases/download/v1.0.0/arcat-1.0.0-{CONFIG.HOSTOS}_{CONFIG.HOSTARCH}",
    hashes = ["6705304dde3cf358d7b8f5a034dfcc8242474b76d0e439b2f39a7a99f8612749"],
    binary = True,
    visibility = ["PUBLIC"],
)
