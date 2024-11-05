"""Contains tests specific to the CI environment provided by GitHub Actions workflows."""

import os
import sys
import unittest


@unittest.skipIf(os.getenv("CI_PYTHON_VERSION") is None, "Not running in CI environment")
class CITest(unittest.TestCase):

    def test_use_setup_python_interpreter(self):
        """Ensures that python_tests are being run by the Python interpreter installed by
        actions/setup-python.
        """
        ci_major, _, ci_minor = os.getenv("CI_PYTHON_VERSION").partition(".")
        self.assertEqual(int(ci_major), sys.version_info[0])
        self.assertEqual(int(ci_minor), sys.version_info[1])
