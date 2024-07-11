import click
import typing
import requests
import logging
import click_log
import sys
import tools.wheel_resolver.wheel as wheel
import packaging.tags as tags
import distlib.locators

_LOGGER = logging.getLogger(__name__)

click_log.basic_config(_LOGGER)


@click.command()
@click.option(
    "--url",
    "--urls",
    multiple=True,
    metavar="URL",
    default=[],
    help="URLs to check for package before looking in the wheel index",
)
@click.option(
    "--package-name",
    "--package",
    metavar="NAME",
    required=True,
    help="Name of Python package in PyPI",
)
@click.option(
    "--package-version",
    "--version",
    metavar="VERSION",
    help="Version of Python package in PyPI",
)
@click.option(
    "--interpreter",
    type=click.Choice(
        choices=sorted(
            list(tags.INTERPRETER_SHORT_NAMES.keys())
            + list(tags.INTERPRETER_SHORT_NAMES.values())
        ),
        case_sensitive=False,
    ),
    default=tags.interpreter_name(),
    show_default=True,
    help="The interpreter name or abbreviation code",
)
@click.option(
    "--interpreter-version",
    default=tags.interpreter_version(),
    show_default=True,
    metavar="INTERPRETER_VERSION",
    help="The interpreter version, for example 312 for 3.12",
)
@click.option(
    "--platform",
    # Must cast to list so click knows we want multiple default values.
    default=list(tags.platform_tags()),
    metavar="PLATFORM",
    multiple=True,
    help="The platform identifier, for example linux_x86_64 or linux_i686",
)
@click.option(
    "--abi",
    default={t.abi for t in tags.sys_tags()},
    metavar="ABI",
    show_default=True,
    multiple=True,
    help="The ABI identifier, for example cp310 or abi3",
)
@click_log.simple_verbosity_option(_LOGGER)
def main(
    url: typing.List[str],
    package_name: typing.Optional[str],
    package_version: typing.Optional[str],
    interpreter: str,
    interpreter_version: str,
    platform: typing.Iterable[str],
    abi: typing.Iterable[str],
):
    """Resolve a wheel by name and version to a URL.

    If URLs are specified, they are checked literally before doing a lookup in
    PyPI for PACKAGE with VERSION.

    """
    for u in url:
        response = requests.head(u)
        if response.status_code != requests.codes.ok:
            _LOGGER.warning(
                "%s-%s is not available, tried %r", package_name, package_version, u
            )
        else:
            click.echo(u)
            return

    u = wheel.url(
        package_name,
        package_version,
        tags=[
            str(x)
            for x in tags.generic_tags(
                interpreter=f"{interpreter}{interpreter_version}",
                abis=abi,
                platforms=platform,
            )
        ],
        # We're currently hardcoding PyPI but we should consider allowing other
        # repositories
        locator=distlib.locators.PyPIJSONLocator(url="https://pypi.org/pypi"),
    )
    response = requests.head(u)
    if response.status_code != requests.codes.ok:
        _LOGGER.error(
            "%s-%s is not available, tried %r", package_name, package_version, u
        )
        sys.exit(1)
    click.echo(u)
