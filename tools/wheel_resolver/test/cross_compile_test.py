import unittest
import src.tags.tags as tg


class CrossCompileTest(unittest.TestCase):
    """ Test cross compilation """

    def test_darwin_tag(self):
        urls = tg.get_download_urls('tensorflow')
        # result = tg.get_url(urls, "darwin_amd64")
        result = tg.get_url(urls, "macosx_10_11_x86_64")
        self.assertNotEqual(result, 1)
        self.assertIn('.whl', tg.get_basename(result))
        self.assertIn('tensorflow', tg.get_basename(result))

    def test_freebsd_tag(self):
        package = 'six'
        urls = tg.get_download_urls(package)
        archs = ["manylinux"]
        result = tg.get_url(urls, archs)

        # Assert we get a url back from get_url
        self.assertNotEqual(result, 1)

        # Assert that the url we get back is for a .whl file
        self.assertIn('.whl', tg.get_basename(result))
        self.assertIn(package, tg.get_basename(result))
