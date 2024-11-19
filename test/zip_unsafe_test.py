import os
import unittest


class ZipUnsafeTest(unittest.TestCase):
    """Test importing something that requires zip-unsafety and exploding the pex."""

    @unittest.skipIf(os.getenv("TOOL_DEV", "") != "true", "needs tool update to work")
    def test_can_import(self):
        from third_party.python.confluent_kafka import cimpl
        self.assertIsNotNone(cimpl)
