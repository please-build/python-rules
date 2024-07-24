import os
import sys
import urllib.request
import logging

_LOGGER = logging.getLogger(__name__)

class OutputNotSetError(RuntimeError):
    pass

def try_download(url):
    """
    Try to download url to $OUTS. Returns false if
    it failed.
    """
    output = os.environ.get("OUTS")
    if output is None:
        raise OutputNotSetError()

    try:
        urllib.request.urlretrieve(url, output)
    except urllib.error.HTTPError:
        return False

    return True


