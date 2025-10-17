subinclude("//build_defs:archs")

_tools = {
    "please_pex": "//tools/please_pex",
    "wheel_resolver": "//tools/wheel_resolver",
}

def release_file(name:str, version:str, file_target:str, arch:str):
    return genrule(
        name = f"{name}_{arch}",
        srcs = [f"///{arch}" + canonicalise(file_target)],
        outs = [f"{name}-{version}-{arch}"],
        cmd = "mv $SRC $OUT",
    )

for tool, package in _tools.items():
    subinclude(f"{package}:version")
    filegroup(
        name = f"{tool}_release_files",
        srcs = [
            release_file(tool, VERSION, package, arch)
            for arch in SUPPORTED_ARCHS
        ],
        labels = [f"hlink:plz-out/package/{tool}"],
    )
