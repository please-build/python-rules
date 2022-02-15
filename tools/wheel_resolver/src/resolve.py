"""
Tool to resolve a wheel file from an index given a package name
"""

import logging
import urllib.request
import os
import tools.wheel_resolver.src.wheel_tags.tags as tg
import argparse as argparse
import sys


def download(url):
    output = os.environ.get("OUTS")
    if output is None:
        logging.critical("No output directory found")
        sys.exit(1)

    urllib.request.urlretrieve(url, output)


def main():
    """
    Parse command line arguments
    Get all download urls for a given package/version combo
    Figure out which ones are compatible with our system (whether
    that's our actual system or a system we've specified that we
    are maybe cross-compiling for.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
            '--package',
            type=str,
            help='the package to resolve')
    parser.add_argument(
            '--version',
            type=str,
            help='the version of the package to be resolved')
    parser.add_argument(
            '--arch',
            nargs="*",
            type=str,
            default=[],
            help='specify architecture')

    args = parser.parse_args()

    # Fetch all available wheel urls from index
    urls = tg.get_download_urls(args.package, args.version)
    if urls is None:
        logging.critical("No matching urls found in index")
        sys.exit(1)

    result = tg.get_url(urls, args.arch)

    if result is not None:
        download(result)
    else:
        logging.critical("Found %s urls but none are compatible", len(urls))
        sys.exit(1)


main()
