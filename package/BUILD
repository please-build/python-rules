export_file(
    name = "files",
    src = "files.build_defs",
    visibility = ["PUBLIC"],
)

subinclude(":files", "//build_defs:release_file", "//build_defs:archs")

filegroup(
    name = "release_files",
    srcs = [
        release_file(name, target, arch)
        for name, target in RELEASE_FILES.items()
        for arch in SUPPORTED_ARCHS
    ],
    labels = ["hlink:plz-out/package"],
)

