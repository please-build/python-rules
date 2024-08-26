subinclude("//build_defs:archs", "///go//build_defs:go")

go_toolchain(
    name = "toolchain",
    hashes = [
        "9c3c0124b01b5365f73a1489649f78f971ecf84844ad9ca58fde133096ddb61b",  # darwin_amd64
        "ebac39fd44fc22feed1bb519af431c84c55776e39b30f4fd62930da9c0cfd1e3",  # darwin_arm64
        "424a5618406800365fe3ad96a795fb55ce394bea3ff48eaf56d292bf7a916d1e",  # freebsd_amd64
        "999805bed7d9039ec3da1a53bfbcafc13e367da52aa823cb60b68ba22d44c616",  # linux_amd64
    ],
    install_std = False,
    architectures = SUPPORTED_ARCHS,
    version = "1.22.6",
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
