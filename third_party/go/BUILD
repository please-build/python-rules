subinclude("//build_defs:archs", "///go//build_defs:go")

go_toolchain(
    name = "toolchain",
    hashes = [
        "1641050b422b80dfd6299f8aa7eb8798d1cd23eac7e79f445728926e881b7bcd",  # darwin-amd64
        "7c083e3d2c00debfeb2f77d9a4c00a1aac97113b89b9ccc42a90487af3437382",  # darwin-arm64
        "77a36eef352609f616813ec710274d122738510b62efd0fac1435cb480a07170",  # freebsd-amd64
        "0335f314b6e7bfe08c3d0cfaa7c19db961b7b99fb20be62b0a826c992ad14e0f",  # linux-amd64
        "1d42ebc84999b5e2069f5e31b67d6fc5d67308adad3e178d5a2ee2c9ff2001f5",  # linux-arm64
    ],
    install_std = False,
    architectures = SUPPORTED_ARCHS,
    version = "1.25.3",
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
    version = "v0.26.0",
)

go_repo(
    module = "github.com/dustin/go-humanize",
    version = "v1.0.1",
)

go_repo(
    module = "gopkg.in/yaml.v3",
    version = "v3.0.1",
)
