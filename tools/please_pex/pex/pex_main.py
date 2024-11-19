"""Zipfile entry point which supports auto-extracting itself based on zip-safety."""

import os
import runpy
import sys

# Put this pex on the path before anything else.
PEX = os.path.abspath(sys.argv[0])
# This might get overridden down the line if the pex isn't zip-safe.
PEX_PATH = PEX
sys.path = [PEX_PATH] + sys.path

# These will get templated in by the build rules.
MODULE_DIR = '__MODULE_DIR__'
ENTRY_POINT = '__ENTRY_POINT__'
ZIP_SAFE = __ZIP_SAFE__
PEX_STAMP = '__PEX_STAMP__'


def add_module_dir_to_sys_path(dirname, zip_safe=True):
    """Adds the given dirname to sys.path if it's nonempty."""
    import plz  # this needs to be imported after paths are set up
    if dirname:
        sys.path.insert(1, os.path.join(sys.path[0], dirname))
        sys.meta_path.insert(0, plz.ModuleDirImport(dirname))
    if zip_safe:
        sys.meta_path.append(plz.SoImport(MODULE_DIR))


def pex_basepath(temp=False):
    if temp:
        import tempfile
        return tempfile.mkdtemp(dir=os.environ.get('TEMP_DIR'), prefix='pex_')
    else:
        return os.environ.get('PEX_CACHE_DIR',os.path.expanduser('~/.cache/pex'))


def pex_uniquedir():
    return 'pex-%s' % PEX_STAMP


def pex_paths():
    no_cache = os.environ.get('PEX_NOCACHE')
    no_cache = no_cache and no_cache.lower() == 'true'
    basepath, uniquedir = pex_basepath(no_cache), pex_uniquedir()
    pex_path = os.path.join(basepath, uniquedir)
    return pex_path, basepath, uniquedir, no_cache


def explode_zip():
    """Extracts the current pex to a temp directory where we can import everything from.

    This is primarily used for binary extensions which can't be imported directly from
    inside a zipfile.
    """
    # Temporarily add bootstrap to sys path
    sys.path = [os.path.join(sys.path[0], '.bootstrap')] + sys.path[1:]
    import contextlib, portalocker
    sys.path = sys.path[1:]

    @contextlib.contextmanager
    def pex_lockfile(basepath, uniquedir):
        # Acquire the lockfile.
        lockfile_path = os.path.join(basepath, '.lock-%s' % uniquedir)
        lockfile = open(lockfile_path, "a+")
        # Block until we can acquire the lockfile.
        portalocker.lock(lockfile, portalocker.LOCK_EX)
        lockfile.seek(0)
        yield lockfile
        portalocker.lock(lockfile, portalocker.LOCK_UN)

    @contextlib.contextmanager
    def _explode_zip():
        # We need to update the actual variable; other modules are allowed to look at
        # these variables to find out what's going on (e.g. are we zip-safe or not).
        global PEX_PATH

        PEX_PATH, basepath, uniquedir, no_cache = pex_paths()
        os.makedirs(basepath, exist_ok=True)
        with pex_lockfile(basepath, uniquedir) as lockfile:
            if len(lockfile.read()) == 0:
                import compileall, zipfile, plz

                os.makedirs(PEX_PATH, exist_ok=True)
                with plz.ZipFileWithPermissions(PEX, "r") as zf:
                    zf.extractall(PEX_PATH)

                if not no_cache:  # Don't bother optimizing; we're deleting this when we're done.
                    compileall.compile_dir(PEX_PATH, optimize=2, quiet=1)

                # Writing nonempty content to the lockfile will signal to subsequent invocations
                # that the cache has already been prepared.
                lockfile.write("pex unzip completed")
        sys.path = [PEX_PATH] + [x for x in sys.path if x != PEX]
        try:
            yield
        finally:
            if no_cache:
                import shutil
                shutil.rmtree(basepath)

    return _explode_zip


def profile(filename):
    """Returns a context manager to perform profiling while the program runs.

    This is triggered by setting the PEX_PROFILE_FILENAME env var to the destination file,
    at which point this will be invoked automatically at pex startup.
    """
    import contextlib, cProfile

    @contextlib.contextmanager
    def _profile():
        profiler = cProfile.Profile()
        profiler.enable()
        yield
        profiler.disable()
        sys.stderr.write('Writing profiler output to %s\n' % filename)
        profiler.dump_stats(filename)

    return _profile


# This must be redefined/implemented when the pex is built for debugging.
# The `DEBUG_PORT` environment variable should be used if the debugger is
# to be used as a server.
def start_debugger():
    pass


def main():
    """Runs the 'real' entry point of the pex.

    N.B. This gets redefined by pex_test_main to run tests instead.
    """
    # Starts a debugging session, if defined, before running the entry point.
    if os.getenv("PLZ_DEBUG") is not None:
        start_debugger()

    # Must run this as __main__ so it executes its own __name__ == '__main__' block.
    runpy.run_module(ENTRY_POINT, run_name='__main__')
    return 0  # unless some other exception gets raised, we're successful.
