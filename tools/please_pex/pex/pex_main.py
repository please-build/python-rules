"""Zipfile entry point which supports auto-extracting itself based on zip-safety."""

from collections import defaultdict
from importlib import import_module, machinery
from importlib.abc import MetaPathFinder
from importlib.metadata import Distribution
from importlib.util import spec_from_loader
import itertools
import os
import re
import runpy
import sys
import tempfile
import zipfile


try:
    from site import getsitepackages
except:
    def getsitepackages(prefixes=[sys.prefix, sys.exec_prefix]):
        """Returns a list containing all global site-packages directories.

        For each directory present in ``prefixes`` (or the global ``PREFIXES``),
        this function will find its `site-packages` subdirectory depending on the
        system environment, and will return a list of full paths.
        """
        sitepackages = []
        seen = set()

        if prefixes is None:
            prefixes = PREFIXES

        for prefix in prefixes:
            if not prefix or prefix in seen:
                continue
            seen.add(prefix)

            if os.sep == '/':
                sitepackages.append(os.path.join(prefix, "lib",
                                            "python%d.%d" % sys.version_info[:2],
                                            "site-packages"))
            else:
                sitepackages.append(prefix)
                sitepackages.append(os.path.join(prefix, "lib", "site-packages"))

        return sitepackages

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

# Workaround for https://bugs.python.org/issue15795
class ZipFileWithPermissions(zipfile.ZipFile):
    """ Custom ZipFile class handling file permissions. """

    def _extract_member(self, member, targetpath, pwd):
        if not isinstance(member, zipfile.ZipInfo):
            member = self.getinfo(member)

        targetpath = super(ZipFileWithPermissions, self)._extract_member(
            member, targetpath, pwd
        )

        attr = member.external_attr >> 16
        if attr != 0:
            os.chmod(targetpath, attr)
        return targetpath

class SoImport(MetaPathFinder):
    """So import. Much binary. Such dynamic. Wow."""

    def __init__(self):
        self.suffixes = machinery.EXTENSION_SUFFIXES  # list, as importlib will not be using the file description
        self.suffixes_by_length = sorted(self.suffixes, key=lambda x: -len(x))
        # Identify all the possible modules we could handle.
        self.modules = {}
        if zipfile.is_zipfile(sys.argv[0]):
            zf = ZipFileWithPermissions(sys.argv[0])
            for name in zf.namelist():
                path, _ = self.splitext(name)
                if path:
                    if path.startswith('.bootstrap/'):
                        path = path[len('.bootstrap/'):]
                    importpath = path.replace('/', '.')
                    self.modules.setdefault(importpath, name)
                    if path.startswith(MODULE_DIR):
                        self.modules.setdefault(importpath[len(MODULE_DIR)+1:], name)
            if self.modules:
                self.zf = zf

    def find_spec(self, name, path, target=None):
        """Implements abc.MetaPathFinder."""
        if name in self.modules:
            return spec_from_loader(name, self)

    def create_module(self, spec):
        """Create a module object that we're going to load."""
        filename = self.modules[spec.name]
        prefix, ext = self.splitext(filename)
        with tempfile.NamedTemporaryFile(suffix=ext, prefix=os.path.basename(prefix)) as f:
            f.write(self.zf.read(filename))
            f.flush()
            spec.origin = f.name
            loader = machinery.ExtensionFileLoader(spec.name, f.name)
            spec.loader = loader
            mod = loader.create_module(spec)
        # Make it look like module came from the original location for nicer tracebacks.
        mod.__file__ = filename
        return mod

    def exec_module(self, mod):
        """Because we set spec.loader above, the ExtensionFileLoader's exec_module is called."""
        raise NotImplementedError("SoImport.exec_module isn't used")

    def splitext(self, path):
        """Similar to os.path.splitext, but splits our longest known suffix preferentially."""
        for suffix in self.suffixes_by_length:
            if path.endswith(suffix):
                return path[:-len(suffix)], suffix
        return None, None


class PexDistribution(Distribution):
    """Represents a distribution package that exists within a pex file (which is, ultimately, a zip
    file). Distribution packages are identified by the presence of a suitable dist-info or egg-info
    directory member inside the pex file, which need not necessarily exist at the top level if a
    directory prefix is specified in the constructor.
    """
    def __init__(self, name, pex_file, zip_file, files, prefix):
        self._name = name
        self._zf = zip_file
        self._pex_file = pex_file
        self._prefix = prefix
        # Mapping of <path within distribution> -> <full path in zipfile>
        self._files = files

    def read_text(self, filename):
        full_name = self._files.get(filename)
        if full_name:
            return self._zf.read(full_name).decode(encoding="utf-8")

    def locate_file(self, path):
        return zipfile.Path(
            self._pex_file,
            at=os.path.join(self._prefix, path) if self._prefix else path,
        )

    read_text.__doc__ = Distribution.read_text.__doc__


class ModuleDirImport(MetaPathFinder):
    """Handles imports to a directory equivalently to them being at the top level.

    This means that if one writes `import third_party.python.six`, it's imported like `import six`,
    but becomes accessible under both names. This handles both the fully-qualified import names
    and packages importing as their expected top-level names internally.
    """
    def __init__(self, module_dir=MODULE_DIR):
        self.prefix = module_dir.replace("/", ".") + "."
        self._distributions = self._find_all_distributions(module_dir)

    def _find_all_distributions(self, module_dir):
        pex_file = sys.argv[0]
        if zipfile.is_zipfile(pex_file):
            zf = ZipFileWithPermissions(pex_file)
            r = re.compile(r"{module_dir}{sep}([^/]+)-[^/-]+?\.(?:dist|egg)-info/(.*)".format(
                module_dir=module_dir,
                sep = os.sep,
            ))
            filenames = defaultdict(dict)
            for name in zf.namelist():
                match = r.match(name)
                if match:
                    filenames[match.group(1)][match.group(2)] = name
            return {mod: [PexDistribution(mod, pex_file, zf, files, prefix=module_dir)]
                    for mod, files in filenames.items()}
        return {}

    def find_spec(self, name, path, target=None):
        """Implements abc.MetaPathFinder."""
        if name.startswith(self.prefix):
            return spec_from_loader(name, self)

    def create_module(self, spec):
        """Actually load a module that we said we'd handle in find_module."""
        module = import_module(spec.name[len(self.prefix):])
        sys.modules[spec.name] = module
        return module

    def exec_module(self, mod):
        """Nothing to do, create_module already did the work."""

    def find_distributions(self, context):
        """Return an iterable of all Distribution instances capable of
        loading the metadata for packages for the indicated ``context``.
        """
        if context.name:
            # The installed directories have underscores in the place of what might be a hyphen
            # in the package name (e.g. the package opentelemetry-sdk installs opentelemetry_sdk).
            return self._distributions.get(context.name.replace("-", "_"), [])
        else:
            return itertools.chain(*self._distributions.values())

    def get_code(self, fullname):
        module = self.load_module(fullname)
        return module.__loader__.get_code(fullname)


def add_module_dir_to_sys_path(dirname):
    """Adds the given dirname to sys.path if it's nonempty."""
    if dirname:
        sys.path = sys.path[:1] + [os.path.join(sys.path[0], dirname)] + sys.path[1:]
        sys.meta_path.insert(0, ModuleDirImport(dirname))


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
                import compileall, zipfile

                os.makedirs(PEX_PATH, exist_ok=True)
                with ZipFileWithPermissions(PEX, "r") as zf:
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
    # Add .bootstrap dir to path, after the initial pex entry
    sys.path = sys.path[:1] + [os.path.join(sys.path[0], '.bootstrap')] + sys.path[1:]
    # Starts a debugging session, if defined, before running the entry point.
    if os.getenv("PLZ_DEBUG") is not None:
        start_debugger()

    # Must run this as __main__ so it executes its own __name__ == '__main__' block.
    runpy.run_module(ENTRY_POINT, run_name='__main__')
    return 0  # unless some other exception gets raised, we're successful.
