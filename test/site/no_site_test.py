import sys
import unittest


class NoSiteTest(unittest.TestCase):

    def test_no_site_flag_passed(self):
        """Ensures that the Python interpreter was invoked with the -S option."""
        self.assertTrue(sys.flags.no_site)
