import click.testing

import tools.wheel_resolver as sut


class TestMain:
    def test_help(self) -> None:
        runner = click.testing.CliRunner()
        result = runner.invoke(cli=sut.main, args=["--help"])
        assert result.exit_code == 0
