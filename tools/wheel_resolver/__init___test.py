import click.testing
import pytest
import unittest.mock
import requests

import tools.wheel_resolver as sut


class TestMain:
    def test_help(self) -> None:
        runner = click.testing.CliRunner()
        result = runner.invoke(cli=sut.main, args=["--help"])
        assert result.exit_code == 0

    @unittest.mock.patch.object(sut.output, "try_download")
    @unittest.mock.patch.object(sut.requests, "head")
    def test_any_in_platforms(
            self, _mock_requests_head: unittest.mock.MagicMock, _mock_try_download: unittest.mock.MagicMock
    ) -> None:
        _mock_try_download.return_value = True
        _mock_requests_head.return_value = requests.Response()
        _mock_requests_head.return_value.status_code = requests.codes.ok

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
        assert result.exit_code == 0
