// Package pex implements construction of .pex files in Go.
// For performance reasons we've ultimately abandoned doing this in Python;
// we were ultimately not using pex for much at construction time and
// we already have most of what we need in Go via jarcat.
package pex

import (
	"bytes"
	"embed"
	"encoding/json"
	"fmt"
	"io/fs"
	"log"
	"os"
	"path"
	"path/filepath"
	"strings"

	"github.com/please-build/python-rules/tools/please_pex/preamble"
	"github.com/please-build/python-rules/tools/please_pex/zip"
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
//go:embed preamble
var files embed.FS

// A Writer implements writing a .pex file in various steps.
type Writer struct {
	preambleConfig   *preamble.Config
	zipSafe          bool
	realEntryPoint   string
	pexStamp         string
	testSrcs         []string
	includeLibs      []string
	testRunner       string
	customTestRunner string
	debugger         string
}

// NewWriter constructs a new Writer.
func NewWriter(entryPoint string, interpreters []string, interpreterArgs []string, stamp string, zipSafe, noSite bool) *Writer {
	pw := &Writer{
		preambleConfig: &preamble.Config{
			Interpreters:    interpreters,
			InterpreterArgs: interpreterArgs,
		},
		zipSafe:        zipSafe,
		realEntryPoint: toPythonPath(entryPoint),
		pexStamp:       stamp,
	}
	if noSite {
		pw.preambleConfig.InterpreterArgs = append(pw.preambleConfig.InterpreterArgs, "-S")
	}
	return pw
}

// SetPreambleVerbosity sets the preamble's default minimum logging level.
func (pw *Writer) SetPreambleVerbosity(verbosity preamble.Verbosity) {
	pw.preambleConfig.Verbosity = verbosity
}

// SetTest sets this Writer to write tests using the given sources.
// This overrides the entry point given earlier.
func (pw *Writer) SetTest(srcs []string, testRunner string, addTestRunnerDeps bool) {
	pw.realEntryPoint = "pex_test_main"
	pw.testSrcs = srcs

	// These are the outputs of //third_party/python:test_bootstrap and its transitive dependencies.
	testRunnerDeps := []string{
		".bootstrap/__init__.py",
		".bootstrap/coverage",
		".bootstrap/portalocker",
	}

	switch testRunner {
	case "pytest":
		// These are the outputs of //third_party/python:pytest_bootstrap and its transitive dependencies
		// (except for those from //third_party/python:test_bootstrap).
		testRunnerDeps = append(testRunnerDeps,
			".bootstrap/_pytest",
			".bootstrap/exceptiongroup",
			".bootstrap/iniconfig",
			".bootstrap/packaging",
			".bootstrap/pluggy",
			".bootstrap/py",
			".bootstrap/pygments",
			".bootstrap/pytest",
			".bootstrap/tomli",
			".bootstrap/typing_extensions.py",
		)
		pw.testRunner = filepath.Join(testRunnersDir, "pytest.py")
	case "behave":
		// These are the outputs of //third_party/python:behave_bootstrap and its transitive dependencies
		// (except for those from //third_party/python:test_bootstrap).
		testRunnerDeps = append(testRunnerDeps,
			".bootstrap/behave",
			".bootstrap/colorama",
			".bootstrap/enum",
			".bootstrap/parse.py",
			".bootstrap/parse_type",
			".bootstrap/six.py",
			".bootstrap/traceback2",
			".bootstrap/win_unicode_console",
		)
		pw.testRunner = filepath.Join(testRunnersDir, "behave.py")
	case "unittest":
		// These are the outputs of //third_party/python:unittest_bootstrap and its transitive dependencies
		// (except for those from //third_party/python:test_bootstrap).
		testRunnerDeps = append(testRunnerDeps,
			".bootstrap/xmlrunner",
		)
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

// Write writes the pex to the given output file.
func (pw *Writer) Write(out, moduleDir string) error {
	f := zip.NewFile(out, true)
	defer f.Close()

	// Write preamble (i.e. the binary that makes the .pex executable)
	preambleFile := mustOpen("preamble")
	defer preambleFile.Close()
	if err := f.WritePreambleFile(preambleFile); err != nil {
		return err
	}

	// Write preamble configuration file
	preambleConfig, err := json.Marshal(&pw.preambleConfig)
	if err != nil {
		return fmt.Errorf("marshal preamble configuration: %w", err)
	}
	if err := f.WriteFile(preamble.ConfigPath, preambleConfig, 0644); err != nil {
		return fmt.Errorf("write preamble configuration: %w", err)
	}

	// Non-zip-safe pexes need portalocker
	if !pw.zipSafe {
		pw.includeLibs = append(pw.includeLibs, ".bootstrap/portalocker")
	}

	// Write required extra libraries. Note that this executable is also a zipfile and we can
	// jarcat it directly in (nifty, huh?).
	//
	// Note that if the target contains its own test-runner, then we don't need to add anything.
	if len(pw.includeLibs) > 0 {
		f.Include = pw.includeLibs
		pexPath, err := os.Executable() // get abspath to currently-running executable
		if err != nil {
			return err
		}
		if err := f.AddZipFile(pexPath); err != nil {
			return err
		}
	}

	// Write plz.py which contains much of our import hooks etc
	b := mustRead("plz.py")
	if err := f.WriteFile(".bootstrap/plz.py", b, 0644); err != nil {
		return err
	}

	// Always write pex_main.py, with some templating.
	b = mustRead("pex_main.py")
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
	// We always append the final if __name__ == '__main__' bit.
	b = append(b, mustRead("pex_run.py")...)
	return f.WriteFile("__main__.py", b, 0644)
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

// mustOpen opens the given file from the embedded set. It dies on error.
func mustOpen(filename string) fs.File {
	f, err := files.Open(filename)
	if err != nil {
		panic(err)
	}
	return f
}

// mustRead reads the given file from the embedded set. It dies on error.
func mustRead(filename string) []byte {
	b, err := files.ReadFile(filename)
	if err != nil {
		panic(err)
	}
	return b
}
