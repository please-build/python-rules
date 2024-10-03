subinclude("//build_defs:archs", "///go//build_defs:go")

go_toolchain(
    name = "toolchain",
    hashes = [
        "445c0ef19d8692283f4c3a92052cc0568f5a048f4e546105f58e991d4aea54f5",  # darwin-amd64
        "d87031194fe3e01abdcaf3c7302148ade97a7add6eac3fec26765bcb3207b80f",  # darwin-arm64
        "025d77f1780906142023a364c31a572afd7d56d3a3be1e4e562e367ca88d3267",  # freebsd-amd64
        "542d3c1705f1c6a1c5a80d5dc62e2e45171af291e755d591c5e6531ef63b454e",  # linux-amd64
        "f626cdd92fc21a88b31c1251f419c17782933a42903db87a174ce74eeecc66a9",  # linux-arm64
    ],
    install_std = False,
    architectures = SUPPORTED_ARCHS,
    version = "1.23.2",
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
