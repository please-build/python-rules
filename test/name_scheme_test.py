import unittest


class NameSchemeTest(unittest.TestCase):

    # The click python_wheel has no name_scheme argument, and is thus using the default value which
    # is a list.
    def test_click_is_importable(self):
        import click
        self.assertIsNotNone(click.command)

    # The click-log python_wheel has an explicit name_scheme argument which is a string.
    def test_click_log_is_importable(self):
        import click_log
        self.assertIsNotNone(click_log.basic_config)
