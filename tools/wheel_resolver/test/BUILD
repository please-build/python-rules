python_test(
    name = "lib_test",
    srcs = ["test.py"],
    deps = ["//tools/wheel_resolver/src/wheel_tags:tags"],
)

gentest(
    name = "e2e_test",
    data = ["//tools/wheel_resolver/src:resolve"],
    no_test_output = True,
    test_cmd = "PKG=tensorflow; OUTS=$PKG.whl; export OUTS; $DATA --package \"$PKG\"; \
                if [[ -f \"$PKG\".whl ]]; then exit 0; else exit 1; fi;",
)
