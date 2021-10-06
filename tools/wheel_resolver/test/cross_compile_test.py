import unittest
import tools.wheel_resolver.src.wheel_tags.tags as tg


class CrossCompileTest(unittest.TestCase):
    """
    Test cross compilation. These are set to manual
    for the moment because cross compilation isn't
    working yet. Also would probably be better to make
    these proper e2e tests.
    """

    def test_darwin_tag(self):
        urls = tg.get_download_urls('tensorflow')
        # result = tg.get_url(urls, "darwin_amd64")
        result = tg.get_url(urls, "macosx_10_11_x86_64")
        self.assertNotEqual(result, 1)
        self.assertIn('.whl', tg.get_basename(result))
        self.assertIn('tensorflow', tg.get_basename(result))

    def test_manylinux_tag(self):
        package = 'six'
        urls = tg.get_download_urls(package)
        archs = ["manylinux"]
        result = tg.get_url(urls, archs)

        # Assert we get a url back from get_url
        self.assertNotEqual(result, 1)

        # Assert that the url we get back is for a .whl file
        self.assertIn('.whl', tg.get_basename(result))
        self.assertIn(package, tg.get_basename(result))
