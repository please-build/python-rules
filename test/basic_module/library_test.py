import unittest
from test.basic_module import library

class LibraryTest(unittest.TestCase):
    def test_foo(self):
        self.assertEqual("something", library.foo())