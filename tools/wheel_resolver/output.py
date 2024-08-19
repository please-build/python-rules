import os
import urllib.request
import logging
import typing

_LOGGER = logging.getLogger(__name__)


class OutputNotSetError(RuntimeError):
    pass


def get() -> str:
    output = os.environ.get("OUTS")
    if output is None:
        raise OutputNotSetError()
    return output


def download(
    package_name: str, package_version: str, url: typing.List[str], download_output: str
) -> typing.Optional[str]:
    """Download url to $OUTS."""
    for u in url:
        try:
            urllib.request.urlretrieve(u, download_output)
        except urllib.error.HTTPError:
            _LOGGER.warning(
                "%s-%s is not available in %s", package_name, package_version, u
            )
        else:
            return u
    return None
