"""Test for passing flags to python_test."""

import sys
import unittest


class FlagsTest(unittest.TestCase):

    def test_flags(self):
        self.assertIn("--test_flag", sys.argv)
