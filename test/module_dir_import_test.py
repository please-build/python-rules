import unittest


class TestModuleDirImport(unittest.TestCase):

    def test_imports_are_the_same(self):
        import six
        import third_party.python.six
        self.assertEqual(six, third_party.python.six)
