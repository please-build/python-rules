import unittest
import tools.wheel_resolver.src.e2e_test.e2e as e2e


class e2eTest(unittest.TestCase):


    def test_six_with_version(self):
        result = e2e.run('six', '1.16.0')
        self.assertIn('.whl', result)
        self.assertIn('six', result)

    def test_tensorflow_no_version(self):
        result = e2e.run('tensorflow')
        self.assertIn('tensorflow', result)
