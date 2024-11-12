from importlib.metadata import PackagePath, files, version
import importlib_metadata
import unittest


class DistributionMetadataTest(unittest.TestCase):
    """Tests that the pex meta path finder in ModuleDirImport is able to extract distribution
    metadata directly from a .dist-info directory inside the pex file.
    """

    def test_importlib_metadata_version(self):
        self.assertEqual(version("pygments"), "2.18.0")

    def test_importlib_metadata_files(self):
        self.assertIn(PackagePath("pygments/__init__.py"), files("pygments"))


class DistributionMetadataThirdPartyTest(unittest.TestCase):
    """As above, but uses the third-party importlib_metadata package."""

    def test_importlib_metadata_version(self):
        self.assertEqual(importlib_metadata.version("pygments"), "2.18.0")

    def test_importlib_metadata_files(self):
        self.assertIn(importlib_metadata.PackagePath("pygments/__init__.py"),
                      importlib_metadata.files("pygments"))
