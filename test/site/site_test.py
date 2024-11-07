import sys
import unittest


class SiteTest(unittest.TestCase):

    def test_no_site_flag_not_passed(self):
        """Ensures that the Python interpreter was *not* invoked with the -S option."""
        self.assertFalse(sys.flags.no_site)
