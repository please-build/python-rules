subinclude("//build_defs:archs", "///go//build_defs:go")

go_toolchain(
    name = "toolchain",
    hashes = [
        "ecb3cecb1e0bcfb24e50039701f9505b09744cc4730a8b9fc512b0a3b47cf232",  # darwin-amd64
        "0db27ff8c3e35fd93ccf9d31dd88a0f9c6454e8d9b30c28bd88a70b930cc4240",  # darwin-arm64
        "16b0f6417350711c123b160fe33a8bc53e1ea8a4a9cf2f410b427e3ac14195a1",  # freebsd-amd64
        "6842c516ca66c89d648a7f1dbe28e28c47b61b59f8f06633eb2ceb1188e9251d",  # linux-amd64
        "38ac33b4cfa41e8a32132de7a87c6db49277ab5c0de1412512484db1ed77637e",  # linux-arm64
    ],
    install_std = False,
    architectures = SUPPORTED_ARCHS,
    version = "1.24.8",
)

go_stdlib(
    name = "std",
    tags = [
        "netgo",
        "osusergo",
    ],
)

go_repo(
    module = "gopkg.in/op/go-logging.v1",
    version = "v1.0.0-20160211212156-b2cb9fa56473",
)

go_repo(
    module = "github.com/stretchr/testify",
    version = "v1.9.0",
)

go_repo(
    module = "github.com/pmezard/go-difflib",
    version = "v1.0.0",
)

go_repo(
    module = "github.com/davecgh/go-spew",
    version = "v1.1.1",
)

go_repo(
    module = "github.com/peterebden/go-cli-init/v5",
    version = "v5.2.1",
)

go_repo(
    module = "github.com/thought-machine/go-flags",
    version = "v1.6.3",
)

go_repo(
    module = "golang.org/x/term",
    version = "v0.18.0",
)

go_repo(
    module = "golang.org/x/sys",
    version = "v0.20.0",
)

go_repo(
    module = "github.com/dustin/go-humanize",
    version = "v1.0.1",
)

go_repo(
    module = "gopkg.in/yaml.v3",
    version = "v3.0.1",
)
