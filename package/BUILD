subinclude("//tools:version", "//build_defs:archs", "///go//build_defs:go")

release_files = {
    "please_pex": "//tools/please_pex",
    "wheel_resolver": "//tools/wheel_resolver",
}

def release_file(name:str, file_target:str, arch:str):
    return genrule(
        name = f"{name}_{arch}",
        srcs = [f"///{arch}" + canonicalise(file_target)],
        outs = [f"{name}-{VERSION}-{arch}"],
        cmd = "mv $SRC $OUT",
    )

filegroup(
    name = "release_files",
    srcs = [
        release_file(name, target, arch)
        for name, target in release_files.items()
        for arch in SUPPORTED_ARCHS
    ],
    labels = ["hlink:plz-out/package"],
)

