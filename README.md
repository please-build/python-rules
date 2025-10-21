# Python rules

This repo is a plugin that provides python rules for the [Please](https://please.build) build system.

## Basic usage

```python
# BUILD
# This adds the plugin to your project
github_repo(
    name = "python_rules",
    repo = "please-build/python-rules",
    revision = "<Some git tag, commit, or other reference>",
)

# src/main/python/build/please/foo/BUILD
# This defines a python library that can be depended on by other python rules
python_library(
    name = "foo",
    srcs = ["foo.py"],
    visibility = ["//src/test/python/build/please/..."]
)

# src/test/python/build/please/foo/BUILD
# A test for the above library
python_test(
    name = "foo_test",
    srcs = ["foo_test.py"],
    deps = [
        "//src/main/python/build/please/foo",
    ]
)

# src/main/python/build/please/foo/BUILD
# This produces an executable pex file
python_binary(
    name = "pybin",
    main = "pybin.py",
    deps = ["//src/main/python/build/please/foo"]
)
```

Add the following to your `.plzconfig`

```ini
[Parse]
PreloadSubincludes = @python_rules//build_defs:python
```

Alternatively, if you are not using python everywhere, you can simply put `subinclude("@python_rules//build_defs:python")` at the top of individual BUILD files as needed.

## Configuration

Plugins are configured under a Plugin heading like so:

```ini
[Plugin "python"]
DefaultInterpreter = python3
```

The available configuration options are:

```ini
[Plugin "python"]
InterpreterOptions = -b
InterpreterOptions = -s
DefaultInterpreter = python3
PexTool = //tools/please_pex
TestRunner = unittest
Debugger = pdb
ModuleDir = third_party.python
WheelRepo = https://pypi.org/pypi
WheelNameScheme = None
WheelTool = //tools/wheel_resolver
TestRunnerDeps = //third_party/python:unittest_bootstrap
PipTool = ""
DefaultPipRepo = ""
UsePypi = True
PipFlags = ""
DisableVendorFlags = False
```

## Compatibility

This plugin is compatible with the same operating systems as Please itself:

- Darwin (amd64, arm64)
- FreeBSD (amd64)
- Linux (amd64, arm64)

and is compatible with the following Python versions:

- 3.9
- 3.10
- 3.11 (as of python-rules v1.7.0)
- 3.12 (as of python-rules v1.7.0)
- 3.13 (as of python-rules v1.8.0)
- 3.14 (as of python-rules v1.14.0)

Whenever possible, we aim to ensure the plugin works with all of the
[supported Python branches](https://devguide.python.org/versions/#supported-versions). Please
[report](https://github.com/please-build/cc-rules/issues) any bugs you encounter when building,
testing or running Python code under one of these versions.

### Unsupported versions

The following Python versions are no longer supported by this plugin:

- 3.8 (last supported by python-rules v1.7.4)

Outputs that this plugin generates may not run correctly under these Python versions, or may run
with significantly reduced performance.
