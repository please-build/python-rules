"""Internal module for Please builtins."""

from collections import defaultdict
from importlib import import_module, machinery
from importlib.abc import MetaPathFinder
from importlib.metadata import Distribution
from importlib.util import spec_from_loader
import itertools
import os
import re
import sys
import tempfile
import zipfile


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

    def __init__(self, module_dir):
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
                    if path.startswith(module_dir):
                        self.modules.setdefault(importpath[len(module_dir) + 1:], name)
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
    def __init__(self, module_dir):
        self.prefix = module_dir.replace("/", ".") + "."
        self._distributions = self._find_all_distributions(module_dir)

    def _find_all_distributions(self, module_dir):
        pex_file = sys.argv[0]
        if zipfile.is_zipfile(pex_file):
            zf = ZipFileWithPermissions(pex_file)
            r = re.compile(r"{module_dir}{sep}([^/]+)-[^/-]+?\.(?:dist|egg)-info/(.*)".format(
                module_dir=module_dir,
                sep=os.sep,
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
        module = import_module(spec.name.removeprefix(self.prefix))
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
        module = import_module(fullname.removeprefix(self.prefix))
        return module.__loader__.get_code(fullname)
