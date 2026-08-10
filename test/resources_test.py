import importlib.resources
import unittest


class ResourcesTest(unittest.TestCase):
    """Tests that PexDistribution is able to provide access to files that are part of a distribution
    via the importlib.resources API.
    """

    def test_read_resource_text_file(self):
        init = importlib.resources.files("pygments") / "__init__.py"
        self.assertIn("__version__ = '2.19.2'", init.read_text())
