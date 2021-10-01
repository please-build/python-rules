import unittest
import src.tags.tags as tg


class LibTest(unittest.TestCase):

    def test_no_package_arg(self):
        url = tg.get_download_urls(None)
        self.assertIsNone(url)

    def test_no_version_arg(self):
        urls = tg.get_download_urls('argparse')
        self.assertNotEqual(len(urls), 0)

    def test_url_is_whl(self):
        urls = tg.get_download_urls('tensorflow')
        for url in urls:
            self.assertIn('.whl', url)

    def test_make_list_of_tags_from_archs(self):
        archs = ['macosx_10_10_x86_64', 'any']
        result = tg.generate_tags_from_all_archs(archs)

        self.assertNotEqual(result, [])
