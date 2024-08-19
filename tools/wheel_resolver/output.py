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
    package_name: str,
    package_version: typing.Optional[str],
    url: typing.Tuple[str],
    download_output: str,
) -> bool:
    """Download url to $OUTS."""
    for u in url:
        try:
            urllib.request.urlretrieve(u, download_output)
        except urllib.error.HTTPError as error:
            _LOGGER.warning(
                f"download {package_name}-{package_version} from {u}: {error}",
            )
        else:
            _LOGGER.info(f"downloaded {package_name}-{package_version} from {u}")
            return True
    return False
