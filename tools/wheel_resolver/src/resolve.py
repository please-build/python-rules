"""
Tool to resolve a wheel file from an index given a package name
"""

import sys
import src.tags.tags as tg
import third_party.python.argparse as argparse

# my_platform_tag = util.get_platform()
# print('my os:', my_platform_tag)


def main():
    """ main function """
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

    # print('package:', args.package)
    # print('version:', args.version)
    # print('arch:', args.arch)

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
