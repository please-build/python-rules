import sys
import unittest
import zipfile


class InterpreterNotIncludedTest(unittest.TestCase):

    def test_interpreter_is_not_included(self):
        """Test that we don't include any in-repo interpreter in the .pex file."""
        zf = zipfile.ZipFile(sys.argv[0])
        names = [name for name in zf.namelist() if "third_party/cc/cpython/" in name]
        self.assertFalse(names)

    def test_arcat_is_not_included(self):
        """Test that arcat isn't included either."""
        zf = zipfile.ZipFile(sys.argv[0])
        names = [name for name in zf.namelist() if "arcat" in name]
        self.assertFalse(names)
