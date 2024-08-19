import typing
import distlib.locators
import logging

_LOGGER = logging.getLogger(__name__)


class DistributionNotFoundError(RuntimeError):
    pass


class CompatibleUrlNotFoundError(RuntimeError):
    pass


def url(
    *,
    package_name: str,
    package_version: typing.Optional[str],
    tags: typing.List[str],
    locator: distlib.locators.Locator,
    prereleases: bool = True,
) -> str:
    _LOGGER.info(
        "locating %s-%s",
        package_name,
        package_version,
    )
    _LOGGER.debug("tags: %s", ", ".join(tags))
    _LOGGER.debug("prerelease wheels: %s", prereleases)

    requirement = package_name
    if package_version:
        requirement = f"{requirement} (=={package_version})"
    _LOGGER.debug("requirement: %r", requirement)

    distribution = locator.locate(requirement=requirement, prereleases=prereleases)
    _LOGGER.debug("distribution: %r", distribution)

    if not distribution:
        raise DistributionNotFoundError(
            f"{package_name}-{package_version} not found in {locator.base_url!r} using {requirement!r}"
        )

    _LOGGER.debug(
        "len(distribution.download_urls): %d", len(distribution.download_urls)
    )

    compatible_urls = sorted([x for x in distribution.download_urls if _is_wheel(x)])

    if not compatible_urls:
        raise CompatibleUrlNotFoundError(
            f"{package_name}-{package_version} has no compatible URLs"
        )

    if len(compatible_urls) > 1:
        _LOGGER.warning(
            "found %d URLs for %s-%s:\n - %s",
            len(compatible_urls),
            package_name,
            package_version,
            "\n - ".join(compatible_urls),
        )

    return compatible_urls[0]


def _is_wheel(url: str) -> bool:
    return url.endswith(".whl")
