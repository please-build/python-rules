// Package pex implements construction of .pex files in Go.
// For performance reasons we've ultimately abandoned doing this in Python;
// we were ultimately not using pex for much at construction time and
// we already have most of what we need in Go via jarcat.
package pex

import (
	"bytes"
	"embed"
	"fmt"
	"log"
	"os"
	"path"
	"path/filepath"
	"strings"
	// "github.com/thought-machine/please/tools/jarcat/zip"
)

const testRunnersDir = "test_runners"
const debuggersDir = "debuggers"

type Debugger string

const (
	Pdb     Debugger = "pdb"
	Debugpy Debugger = "debugpy"
)

//go:embed *.py
//go:embed test_runners/*.py
//go:embed debuggers/*.py
var files embed.FS

// A Writer implements writing a .pex file in various steps.
type Writer struct {
	zipSafe          bool
	noSite           bool
	shebang          string
	realEntryPoint   string
	pexStamp         string
	testSrcs         []string
	includeLibs      []string
	testRunner       string
	customTestRunner string
	debugger         string
}

// NewWriter constructs a new Writer.
func NewWriter(entryPoint, interpreter, options, stamp string, zipSafe, noSite bool) *Writer {
	pw := &Writer{
		zipSafe:        zipSafe,
		noSite:         noSite,
		realEntryPoint: toPythonPath(entryPoint),
		pexStamp:       stamp,
	}
	pw.SetShebang(interpreter, options)
	return pw
}

// SetShebang sets the leading shebang that will be written to the file.
func (pw *Writer) SetShebang(shebang string, options string) {
	shebang = strings.TrimSpace(fmt.Sprintf("%s %s", shebang, options))
	if !path.IsAbs(shebang) {
		shebang = "/usr/bin/env " + shebang
	}
	if pw.noSite {
		// In many environments shebangs cannot have more than one argument; we can work around
		// that by treating it as a shell script.
		if strings.Contains(shebang, " ") {
			shebang = "#!/bin/sh\nexec " + shebang + ` -S $0 "$@"`
		} else {
			shebang += " -S"
		}
	}
	if !strings.HasPrefix(shebang, "#") {
		shebang = "#!" + shebang
	}
	pw.shebang = shebang + "\n"
}

// SetTest sets this Writer to write tests using the given sources.
// This overrides the entry point given earlier.
func (pw *Writer) SetTest(srcs []string, testRunner string, addTestRunnerDeps bool) {
	pw.realEntryPoint = "pex_test_main"
	pw.testSrcs = srcs

	testRunnerDeps := []string{
		".bootstrap/coverage",
		".bootstrap/__init__.py",
		".bootstrap/six.py",
	}

	switch testRunner {
	case "pytest":
		// We only need xmlrunner for unittest, the equivalent is builtin to pytest.
		testRunnerDeps = append(testRunnerDeps,
			".bootstrap/pytest.py",
			".bootstrap/_pytest",
			".bootstrap/py",
			".bootstrap/pluggy",
			".bootstrap/attr",
			".bootstrap/funcsigs",
			".bootstrap/more_itertools",
			".bootstrap/packaging",
			".bootstrap/pkg_resources",
			".bootstrap/importlib_metadata",
			".bootstrap/zipp",
		)
		pw.testRunner = filepath.Join(testRunnersDir, "pytest.py")
	case "behave":
		testRunnerDeps = append(testRunnerDeps,
			".bootstrap/behave",
			".bootstrap/parse.py",
			".bootstrap/parse_type",
			".bootstrap/traceback2",
			".bootstrap/enum",
			".bootstrap/win_unicode_console",
			".bootstrap/colorama",
		)
		pw.testRunner = filepath.Join(testRunnersDir, "behave.py")
	case "unittest":
		testRunnerDeps = append(testRunnerDeps, ".bootstrap/xmlrunner")
		pw.testRunner = filepath.Join(testRunnersDir, "unittest.py")
	default:
		if !strings.ContainsRune(testRunner, '.') {
			panic("Custom test runner '" + testRunner + "' is invalid; must contain at least one dot")
		}
		pw.testRunner = filepath.Join(testRunnersDir, "custom.py")
		pw.customTestRunner = testRunner
	}

	if addTestRunnerDeps {
		pw.includeLibs = append(pw.includeLibs, testRunnerDeps...)
	}
}

func (pw *Writer) SetDebugger(debugger Debugger) {
	pw.pexStamp = "debug"

	switch debugger {
	case "pdb":
		pw.debugger = filepath.Join(debuggersDir, "pdb.py")
	case "debugpy":
		pw.debugger = filepath.Join(debuggersDir, "debugpy.py")
		pw.includeLibs = append(pw.includeLibs, ".bootstrap/debugpy")
	default:
		log.Fatalf("Unknown debugger: %s", debugger)
	}
}

func appendByteArrayToFile(name string, data []byte, perm os.FileMode) error {
	f, err := os.OpenFile(name, os.O_APPEND|os.O_WRONLY|os.O_CREATE, perm)
	if err != nil {
		return err
	}
	_, err = f.Write(data)
	if err1 := f.Close(); err1 != nil && err == nil {
		err = err1
	}
	return err
}

// Write writes the pex to the given output file.
func (pw *Writer) Write(out, moduleDir string) error {
	// Create file
	f, err := os.Create("__main__.py")
	fmt.Printf("Created __main__.py\n")
	if err != nil {
		panic(err)
	}

	defer f.Close()

	// If this is just going to be a .py file, you can't have a shebang at the top of it
	// Write preamble
	// shebang := []byte(pw.shebang)
	// if _, err := f.Write(shebang); err != nil {
	// 	panic(err)
	// }

	// Write pex_main.py with some templating.
	b := mustRead("pex_main.py")
	b = bytes.Replace(b, []byte("__MODULE_DIR__"), []byte(strings.ReplaceAll(moduleDir, ".", "/")), 1)
	b = bytes.Replace(b, []byte("__ENTRY_POINT__"), []byte(pw.realEntryPoint), 1)
	b = bytes.Replace(b, []byte("__ZIP_SAFE__"), []byte(pythonBool(pw.zipSafe)), 1)
	b = bytes.Replace(b, []byte("__PEX_STAMP__"), []byte(pw.pexStamp), 1)

	if len(pw.testSrcs) != 0 {
		// If we're writing a test, we append pex_test_main.py to it.
		b2 := mustRead("pex_test_main.py")
		b2 = bytes.Replace(b2, []byte("__TEST_NAMES__"), []byte(strings.Join(pw.testSrcs, ",")), 1)
		b = append(b, b2...)
		// It also needs an appropriate test runner.
		b = append(b, bytes.Replace(mustRead(pw.testRunner), []byte("__TEST_RUNNER__"), []byte(pw.customTestRunner), 1)...)
	}

	if len(pw.debugger) > 0 {
		b = append(b, mustRead(pw.debugger)...)
	}

	b = append(b, mustRead("pex_run.py")...)

	return appendByteArrayToFile("__main__.py", b, 0644)
}

// pythonBool returns a Python bool representation of a Go bool.
func pythonBool(b bool) string { //nolint:unused
	if b {
		return "True"
	}
	return "False"
}

// toPythonPath converts a normal path to a Python import path.
func toPythonPath(p string) string {
	ext := path.Ext(p)
	return strings.ReplaceAll(p[:len(p)-len(ext)], "/", ".")
}

// mustRead reads the given file from the embedded set. It dies on error.
func mustRead(filename string) []byte {
	b, err := files.ReadFile(filename)
	if err != nil {
		panic(err)
	}
	return b
}
