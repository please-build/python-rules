subinclude(
    "///shell//build_defs:shell",
    "//build_defs:python",
)

python_binary(
    name = "print_args",
    main = "print_args.py",
)

sh_test(
    name = "path_test",
    src = "path_test.sh",
    data = {
        "pex": [":print_args"],
    },
)
