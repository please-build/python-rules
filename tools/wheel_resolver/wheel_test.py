import pytest
import tools.wheel_resolver.wheel as sut
import collections
import typing
import unittest.mock
import distlib.locators
import distlib.database
import logging

IsCompatibleCase = collections.namedtuple(
    "IsCompatibleCase",
    ["url", "tags", "expected"],
)


class TestUrl:
    def _mock_locator(
        self,
        *,
        with_distribution: bool = True,
        download_urls: typing.Optional[typing.Set[str]] = None,
    ) -> unittest.mock.MagicMock:
        distribution = None
        if with_distribution:
            distribution = distlib.database.Distribution(
                metadata=unittest.mock.MagicMock()
            )
            distribution.download_urls = (
                download_urls if download_urls is not None else set()
            )

        return unittest.mock.MagicMock(
            spec=distlib.locators.PyPIJSONLocator,
            locate=unittest.mock.MagicMock(return_value=distribution),
            base_url="",
        )

    def test_no_distribution(self) -> None:
        with pytest.raises(sut.DistributionNotFoundError):
            sut.url(
                package_name="",
                package_version=None,
                tags=[],
                locator=self._mock_locator(with_distribution=False),
            )

    def test_no_compatible_urls(self) -> None:
        with pytest.raises(sut.CompatibleUrlNotFoundError):
            sut.url(
                package_name="",
                package_version=None,
                tags=[],
                locator=self._mock_locator(),
            )

    @pytest.mark.skip("caplog doesn't capture logging")
    def test_warns_multiple_compatible_urls(self, caplog) -> None:
        with caplog.at_level(logging.WARNING, logger=sut.__name__):
            sut.url(
                package_name="pyyaml",
                package_version="6.0.1",
                tags=[
                    "cp310-cp310-manylinux_2_17_x86_64",
                    "cp311-cp311-manylinux_2_17_x86_64",
                ],
                locator=self._mock_locator(
                    download_urls={
                        "https://files.pythonhosted.org/packages/29/61/bf33c6c85c55bc45a29eee3195848ff2d518d84735eb0e2d8cb42e0d285e/PyYAML-6.0.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl",
                        "https://files.pythonhosted.org/packages/7b/5e/efd033ab7199a0b2044dab3b9f7a4f6670e6a52c089de572e928d2873b06/PyYAML-6.0.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl",
                    }
                ),
            )
            assert len(caplog.records) > 0
            assert any(x.level == logging.WARNING for x in caplog.records)

    @pytest.mark.skip(
        "ordering and selection is unclear; this test case should be updated if we have a preference for a specific URL when collissions happen."
    )
    def test_preferred_url(self) -> None:
        sut.url(
            package_name="pyyaml",
            package_version="6.0.1",
            tags=[
                "cp310-none-manylinux_2_35_x86_64",
                "cp310-none-manylinux_2_34_x86_64",
                "cp310-none-manylinux2014_x86_64",
                "cp310-none-manylinux2010_x86_64",
                "cp310-none-manylinux1_x86_64",
                "cp310-none-linux_x86_64",
                "cp310-abi3-manylinux_2_35_x86_64",
                "cp310-abi3-manylinux2014_x86_64",
                "cp310-abi3-manylinux2010_x86_64",
                "cp310-abi3-manylinux1_x86_64",
                "cp310-abi3-linux_x86_64",
                "cp310-cp310-manylinux_2_35_x86_64",
                "cp310-cp310-manylinux_2_34_x86_64",
                "cp310-cp310-manylinux2014_x86_64",
                "cp310-cp310-manylinux2010_x86_64",
                "cp310-cp310-manylinux1_x86_64",
                "cp310-cp310-linux_x86_64",
            ],
            locator=self._mock_locator(
                download_urls={
                    "https://files.pythonhosted.org/packages/29/61/bf33c6c85c55bc45a29eee3195848ff2d518d84735eb0e2d8cb42e0d285e/PyYAML-6.0.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl",
                    "https://files.pythonhosted.org/packages/7b/5e/efd033ab7199a0b2044dab3b9f7a4f6670e6a52c089de572e928d2873b06/PyYAML-6.0.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl",
                }
            ),
        )

    def test_has_compatible_urls(self) -> None:
        expected = "https://files.pythonhosted.org/packages/29/61/bf33c6c85c55bc45a29eee3195848ff2d518d84735eb0e2d8cb42e0d285e/PyYAML-6.0.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl"
        assert expected == sut.url(
            package_name="pyyaml",
            package_version="6.0.1",
            tags=["cp310-cp310-manylinux_2_17_x86_64"],
            locator=self._mock_locator(download_urls={expected}),
        )


class TestIsCompatible:
    @pytest.mark.parametrize(
        argnames=IsCompatibleCase._fields,
        argvalues=[
            IsCompatibleCase(
                url="https://files.pythonhosted.org/packages/29/61/bf33c6c85c55bc45a29eee3195848ff2d518d84735eb0e2d8cb42e0d285e/PyYAML-6.0.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl",
                tags=["cp310-cp310-manylinux_2_17_x86_64"],
                expected=True,
            ),
            IsCompatibleCase(
                url="https://files.pythonhosted.org/packages/29/61/bf33c6c85c55bc45a29eee3195848ff2d518d84735eb0e2d8cb42e0d285e/PyYAML-6.0.1-cp310.cp311-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl",
                tags=["cp310-cp310-manylinux_2_17_x86_64"],
                expected=True,
            ),
            IsCompatibleCase(
                url="https://files.pythonhosted.org/packages/29/61/bf33c6c85c55bc45a29eee3195848ff2d518d84735eb0e2d8cb42e0d285e/PyYAML-6.0.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl",
                tags=["cp311-cp311-manylinux_2_17_x86_64"],
                expected=False,
            ),
        ],
    )
    def test_is_compatible(
        self,
        url: str,
        tags: typing.List[str],
        expected: bool,
    ) -> None:
        assert expected == sut._is_compatible(
            url=url, tags=tags
        ), f"{url!r} is not compatible with {tags!r}"
