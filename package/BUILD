subinclude("//build_defs:release_file", "//build_defs:archs")

release_files = {
    "please_pex": "//tools/please_pex",
    "wheel_resolver": "//tools/wheel_resolver",
}

filegroup(
    name = "release_files",
    srcs = [
        release_file(name, target, arch)
        for name, target in release_files.items()
        for arch in SUPPORTED_ARCHS
    ],
    labels = ["hlink:plz-out/package"],
)

