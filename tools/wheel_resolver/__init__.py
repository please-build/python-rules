import click
import typing
import requests
import logging
import click_log
import sys
import tools.wheel_resolver.wheel as wheel
import tools.wheel_resolver.output as output
import packaging.tags as tags
import distlib.locators
import itertools

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
    default={t.interpreter for t in tags.sys_tags()},
    multiple=True,
    metavar="INTERPRETER",
    show_default=True,
    help="The interpreter name or abbreviation code with version, for example py31 or cp310",
)
@click.option(
    "--platform",
    # Must cast to list so click knows we want multiple default values.
    default={t.platform for t in tags.sys_tags()},
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
@click.option(
    "--prereleases",
    default=False,
    metavar="PRERELEASES",
    show_default=True,
    multiple=False,
    help="Whether prereleased wheels should also be downloaded",
)
@click_log.simple_verbosity_option(_LOGGER)
def main(
    url: typing.Tuple[str],
    package_name: str,
    package_version: typing.Optional[str],
    interpreter: typing.Tuple[str, ...],
    platform: typing.Tuple[str, ...],
    abi: typing.Tuple[str, ...],
    prereleases: bool = False,
):
    """Resolve a wheel by name and version to a URL.

    If URLs are specified, they are checked literally before doing a lookup in
    PyPI for PACKAGE with VERSION.

    """
    try:
        download_output = output.get()
    except output.OutputNotSetError:
        _LOGGER.error("Could not get $OUTS")
        sys.exit(1)

    locator = distlib.locators.SimpleScrapingLocator(url="https://pypi.org/simple")
    locator.wheel_tags = list(itertools.product(interpreter, abi, platform))
    try:
        u = wheel.url(
            package_name=package_name,
            package_version=package_version,
            tags=[
                str(x)
                for i in interpreter
                for x in tags.generic_tags(
                    interpreter=i,
                    abis=set(abi),
                    platforms=set(platform).union({"any"}),
                )
            ],
            locator=locator,
            prereleases=prereleases,
        )
        url += (u,)
        print(url)
    except Exception as error:
        _LOGGER.warning(error)

    origin_url = output.download(package_name, package_version, url, download_output)
    if origin_url:
        click.echo(f"Downloaded {package_name}-{package_version} from {origin_url}")
        return
