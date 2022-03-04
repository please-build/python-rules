"""
Some methods for wheel fetching and selection
"""

import logging
import os
import sys
from third_party.python.wheel_filename import parse_wheel_filename
from third_party.python.packaging import tags
import third_party.python.distlib.locators as locators


def is_compatible(wheel, archs):
    """
    Check whether the given python package is a wheel compatible with the
    current platform and python interpreter.
    Compatibility is based on https://www.python.org/dev/peps/pep-0425/
    """

    # Get the tag from the wheel we're checking
    w = parse_wheel_filename(wheel)

    # taglist is a list of tags that we've got either from the user
    # or we've auto-generated them for this system
    taglist = generate_tags_from_all_archs(archs)
    # TODO: Could probably cache these? ^^

    if taglist is None:
        logging.critical("No tags generated")

    for system_tag in taglist:
        for tag in w.tag_triples():
            if system_tag in tags.parse_tag(tag):
                return True
    return False


def get_basename(url):
    return os.path.basename(url)


def is_wheel_file(url):
    """ Return whether or not this is a .whl file """
    basename = os.path.basename(url)
    _, ext = os.path.splitext(basename)
    return ext == '.whl'


def generate_tags_from_all_archs(archs):
    if len(archs) == 0:
        return tags.sys_tags()

    result = []
    for arch in archs:
        result += list(tags.generic_tags(interpreter=None,
                                         abis=None,
                                         platforms=[arch]))
        result += list(tags.compatible_tags(python_version=None,
                                            interpreter=None,
                                            platforms=[arch]))

    return result


def get_url(urls, archs):
    """
    From the list of urls we got from the wheel index, return the first
    one that is compatible (either with our system or a provided one)
    """
    if urls is None:
        logging.critical("Empty url list passed to get_url()")

    # Loop through all the urls fetched from index and check them against
    # our system tags
    for url in urls:
        if is_wheel_file(url) and is_compatible(get_basename(url), archs):
            return url

    logging.critical("No urls compatible with the provided system info")
    sys.exit(1)


def get_download_urls(package, version=None, index=None):
    """
    Return all downloadable urls from wheel index that match
    the provided package name and version requirement
    """
    if package is None:
        return None

    if index is None:
        index = 'https://pypi.org/pypi'

    mylocator = locators.PyPIJSONLocator(index)
    # Populate requirement
    requirement = None
    if version is not None:
        requirement = package + '==' + version
    else:
        requirement = package
    dist = mylocator.locate(requirement)
    if dist is not None:
        return dist.download_urls

    return None
