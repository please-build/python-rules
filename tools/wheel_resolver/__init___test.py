import click.testing
import unittest.mock
import tools.wheel_resolver as sut


class TestMain:
    def test_help(self) -> None:
        runner = click.testing.CliRunner()
        result = runner.invoke(cli=sut.main, args=["--help"])
        assert result.exit_code == 0

    def test_any_in_platforms(self) -> None:
        runner = click.testing.CliRunner()
        with unittest.mock.patch.object(sut.wheel, "url") as mock_url:
            result = runner.invoke(
                cli=sut.main,
                args=[
                    "--package-name",
                    "pytest-unordered",
                    "--package-version",
                    "0.6.0",
                    "--interpreter",
                    "py3",
                ],
            )
            for _, _, kwargs in mock_url.mock_calls:
                # Due to tags being a required keyword argument
                if "tags" in kwargs:
                    assert any([t for t in kwargs["tags"] if t.endswith("any")])

    @unittest.mock.patch.object(sut, "_LOGGER")
    @unittest.mock.patch.object(sut.output, "get")
    def test_output_not_set_error(
        self,
        mock_output_get: unittest.mock.MagicMock,
        mock_logger: unittest.mock.MagicMock,
    ) -> None:
        mock_output_get.side_effect = sut.output.OutputNotSetError

        runner = click.testing.CliRunner()
        result = runner.invoke(cli=sut.main, args=["--package-name", "some-package"])

        mock_logger.error.assert_called_once_with("could not get $OUTS")
        assert result.exit_code == 1

    @unittest.mock.patch.object(sut.output, "get")
    @unittest.mock.patch.object(sut.output, "download")
    @unittest.mock.patch.object(sut.wheel, "url")
    @unittest.mock.patch.object(sut, "_LOGGER")
    def test_wheel_url_error(
        self,
        mock_logger: unittest.mock.MagicMock,
        mock_wheel_url: unittest.mock.MagicMock,
        mock_output_download: unittest.mock.MagicMock,
        mock_output_get: unittest.mock.MagicMock,
    ) -> None:

        # Setup variables
        package_name = "test-package"
        package_version = "1.0.0"
        exception_message = "Test Exception"

        # Set up mocks
        mock_output_get.return_value = "output_name"
        mock_output_download.return_value = False
        mock_wheel_url.side_effect = Exception(exception_message)

        # Run the command
        runner = click.testing.CliRunner()
        result = runner.invoke(
            cli=sut.main,
            args=[
                "--package-name",
                f"{package_name}",
                "--package-version",
                f"{package_version}",
            ],
        )

        # Check that the error was logged correctly
        mock_logger.error.assert_any_call(
            f"could not find PyPI URL for {package_name}-{package_version}",
        )

        # Check that the program exited with an error code
        assert result.exit_code == 1
