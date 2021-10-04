"""
Tool to resolve a wheel file from an index given a package name
"""

import sys
import tools.wheel_resolver.src.wheel_tags.tags as tg
import third_party.python.argparse as argparse


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
    if urls == 1:
        print("Couldn't find any matching urls in the index")
        sys.exit(1)

    result = tg.get_url(urls, args.arch)

    if result is None:
        print("error")
        sys.exit(1)
    elif result == 1:
        print("Found", len(urls), "urls but none are "
              "compatible with the specified architecture")
        sys.exit(1)
    else:
        print(result)


main()
