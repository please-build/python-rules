import importlib.resources
import unittest


class ModuleDirImportResourcesTest(unittest.TestCase):
    """Tests that importlib.resources works for a package imported via its Please
    module_dir alias (e.g. `third_party.python.pygments`), not just its plain top-level
    name (`pygments`).

    ModuleDirImport aliases third_party.python.X to the same module object as X, but the
    ModuleSpec it hands back for the aliased name doesn't carry over submodule_search_locations
    from the real module's spec. Because both names share the same module object,
    importlib._bootstrap unconditionally overwrites module.__spec__ with that incomplete spec
    as soon as the aliased name is imported, which then breaks importlib.resources for both
    names (see https://docs.python.org/3/library/importlib.html#importlib.machinery.ModuleSpec).
    """

    def test_read_resource_text_file_via_module_dir_alias(self):
        init = importlib.resources.files("third_party.python.pygments") / "__init__.py"
        self.assertIn("__version__ = '2.19.2'", init.read_text())

    def test_read_resource_text_file_via_plain_name_after_alias_import(self):
        import third_party.python.pygments  # noqa: F401  (import triggers the aliasing)

        init = importlib.resources.files("pygments") / "__init__.py"
        self.assertIn("__version__ = '2.19.2'", init.read_text())
