"""
Tool to resolve a wheel file from an index given a package name
"""

import logging
import urllib.request
import os
import tools.wheel_resolver.wheel_tags.tags as tg
import argparse as argparse
import sys


def try_download(url):
    """
    Try to download url to $OUTS. Returns false if
    it failed.
    """
    output = os.environ.get("OUTS")
    if output is None:
        logging.critical("No output directory found")
        sys.exit(1)

    try:
        urllib.request.urlretrieve(url, output)
    except urllib.error.HTTPError:
        return False

    return True


def main():
    """
    Parse command line arguments
    Get all download urls for a given package/version combo
    Figure out which ones are compatible with our system (whether
    that's our actual system or a system we've specified that we
    are maybe cross-compiling for.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", type=str, help="the package to resolve")
    parser.add_argument(
        "--version", type=str, help="the version of the package to be resolved"
    )
    parser.add_argument(
        "--arch", nargs="*", type=str, default=[], help="specify architecture"
    )
    parser.add_argument(
        "--urls",
        nargs="*",
        type=str,
        default=[],
        help="URLs to try before looking in wheel index",
    )

    args = parser.parse_args()

    # If any URLs were passed, try them first before looking in the wheel index
    if args.urls:
        for url in args.urls:
            if try_download(url):
                return

    # Fetch all available wheel urls from index
    urls = tg.get_download_urls(args.package, args.version)
    if urls is None:
        logging.critical("No matching urls found in index")
        sys.exit(1)

    result = tg.get_url(urls, args.arch)

    if result is not None:
        if try_download(result):
            return

    logging.critical("Found %s URLs but none are compatible", len(urls))
    sys.exit(1)


main()
