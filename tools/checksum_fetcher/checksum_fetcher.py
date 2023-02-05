"""
Utility for generating a build definitions file containing an updated list of
CPython interpreter versions and their related files and checksums.
"""

import asyncio
import functools
import logging
import json
import re
import urllib.error
import urllib.request

from time import sleep

from typing import Any
from typing import Callable
from typing import IO
from typing import Optional
from typing import OrderedDict
from typing import TypedDict


API_URL = "https://api.github.com/repos/indygreg/python-build-standalone/releases"
BASE_URL = "https://github.com/indygreg/python-build-standalone/releases/download"
OUTPUT_FILE = "./build_defs/checksums.build_defs"
WORKERS = 8
INDENTATION = " " * 4


class Asset(TypedDict):
    """
    Asset is a single item from the assets list of a release.
    """

    name: str
    # We only use those fields.
    ...


class Release(TypedDict):
    """
    Release is a single item of the list returned by the GitHub API.
    """

    tag_name: str
    assets: list[Asset]
    # We only use those fields.
    ...


def pipe(value: Any, /, *fns: Callable[..., Any]) -> Any:
    """
    Poor man's function piping. This function passes its first argument
    "value" into a pipeline of functions.

    Args:
        value: Value to pass into the fist function.
        *fns: Functions to pipeline, from left to right.

    Return:
        The return value of the last called function.
    """
    return functools.reduce(lambda x, f: f(x), fns, value)


def write_lines(f: IO[str], /, *lines: str) -> None:
    """
    Write multiple lines of text to a file-like object.

    Parameters:
    f: The file-like object to write to.
    *lines: The lines of text to write to the file.

    Returns:
    None

    Example:
    with open("output.txt", "w") as f:
        write_lines(f, "A line", "Another line")
    """
    for line in lines:
        print(line, file=f)


def parse_api_response(content: list[Release]) -> dict[str, dict[str, list[str]]]:
    """
    parse_api_response filters and transforms the given response from the
    GitHub API into a dict of releases to version numbers to filenames.

    Args:
        content: The JSON response from the GitHub API.

    Returns:
        A dict of releases to version numbers to release filenames.
    """

    def asset_predicate(asset: Asset) -> bool:
        return (
            asset["name"].startswith("cpython")
            # We don't support x64 CPUs.
            and "i686" not in asset["name"]
            # We don't support zst compression (yet)
            and asset["name"].endswith(".tar.gz")
        )

    def release_predicate(release: Release) -> bool:
        # These are releases from before the release naming scheme was
        # stabilized. They also contain versions we are not interested in.
        return release["tag_name"] not in (
            "20220222",
            "20211017",
            "20211012",
            "20210724",
        )

    result: dict[str, dict[str, list[str]]] = {}

    for item in filter(release_predicate, content):
        version: dict[str, list[str]] = {}

        for asset in filter(asset_predicate, item["assets"]):
            match = re.search(r"^cpython-([\d.]+)\+.+$", asset["name"])

            # NOTE: Linux releases have variants tagged with v2, v3, or v4
            # built for CPUs with relatively recent instruction sets. Since we
            # have no easy way of verifying those , they are not supported. We
            # might support up to v2 in the future or let the user choose
            # depending on a parameter, but let's keep things simple for now.
            # @see https://github.com/pydata/numexpr/blob/master/numexpr/cpuinfo.py
            if match and not re.match(
                r"^cpython-.+-x86_64_v[2-4]-unknown-linux.+$", asset["name"]
            ):
                version.setdefault(match.group(1), []).append(asset["name"])

        if version:
            result[item["tag_name"]] = version

    return result


def map_version_assets(raw: dict[str, dict[str, list[str]]]) -> dict[str, list[str]]:
    """
    map_version_assets takes the result of parse_api_response and returns
    a dict of version to asset paths.

    Args:
        raw: Return value of parse_api_response.

    Returns:
        A dict of version to asset paths.
    """
    # Multiple releases can provide the same version of the interpreter; to
    # avoid duplicates, we keep only the last occurrence, so we need the dict
    # to be sorted beforehand.
    d = OrderedDict(sorted(raw.items(), reverse=True))

    uniq: set[str] = set()
    va: dict[str, list[str]] = {}

    for release_name, values in d.items():
        for version, assets in values.items():
            # Skip versions we already saw or those with an empty asset list.
            if not assets or version in uniq:
                continue

            va[version] = [f"{release_name}/{asset}" for asset in assets]
            uniq.add(version)

    return va


def fetch_checksum(url: str, *, _retry: int = 3) -> Optional[str]:
    """
    Fetch the checksum of a file located at a URL.

    Parameters:
    url: The URL of the file to fetch the checksum for.
    _retry: The number of times to retry the request if it fails. Defaults to 3.

    Returns:
    str | None: The checksum of the file, or None if the HTTP request resulted in a 404 error.

    Raises:
    Exception: If the HTTP request fails after the specified number of retries, an error will be logged.
    """
    try:
        with urllib.request.urlopen(f"{BASE_URL}/{url}.sha256") as u:
            checksum = u.read().decode("utf-8").strip().split(" ")[0]
            logging.debug("%s: %s", url, checksum)
            return checksum

    except urllib.error.HTTPError as error:
        if error.code == 404:
            return
        else:
            if _retry > 0:
                sleep(4 - _retry)
                return fetch_checksum(url, _retry=_retry - 1)

            logging.error("something went wrong for %s: %s", url, error.reason)


async def worker(
    loop: asyncio.AbstractEventLoop,
    queue: asyncio.Queue[tuple[str, str]],
    mutex: asyncio.Lock,
    result: dict[str, dict[str, str]],
) -> None:
    while True:
        version, url = await queue.get()
        # Schedule the request on the event loop.
        checksum = await loop.run_in_executor(None, lambda: fetch_checksum(url))

        if checksum:
            # Lock to avoid concurrent dict access.
            async with mutex:
                result.setdefault(version, {})
                result[version][url] = checksum

        # Mark the item as processed, allowing queue.join() to keep track of
        # remaining work and know when everything is done.
        queue.task_done()


def write_results(results: dict[str, dict[str, str]]) -> None:
    with open(OUTPUT_FILE, "w", buffering=-1, encoding="utf-8") as f:
        write_lines(
            f,
            '"""',
            "A module containing a mapping of CPython interpreters to checksums.",
            "",
            "This is a generated file -- see //tools/checksum_fetcher",
            '"""',
            "",
            "SUPPORTED_VERSIONS = [",
        )

        for version in results.keys():
            write_lines(f, f'{INDENTATION}"{version}",')

        write_lines(f, "]", "", "INTERPRETERS = {")

        for version, mappings in results.items():
            write_lines(f, f'{INDENTATION}"{version}" = {{')

            for url, checksum in mappings.items():
                write_lines(f, f'{INDENTATION * 2}"{url}": "{checksum}",')

            write_lines(f, f"{INDENTATION}}},")

        write_lines(f, "}")


async def main() -> int:
    """
    Main entrypoint.
    """

    logging.basicConfig(
        datefmt="%Y-%m-%d %H:%M:%S",
        format="%(asctime)s %(levelname)9s - %(message)s",
        level=logging.DEBUG,
    )
    logging.info("Listing releases...")

    request = urllib.request.Request(API_URL)
    request.add_header("Accept", "application/vnd.github+json")
    request.add_header("X-GitHub-Api-Version", "2022-11-28")

    content: dict[str, list[str]] = pipe(
        request,
        urllib.request.urlopen,
        json.load,
        parse_api_response,
        map_version_assets,
    )

    # Get or create an asyncio event loop.
    loop = asyncio.get_event_loop()
    # Create a mutex for avoiding concurrent dict access.
    mutex = asyncio.Lock()
    # Create a queue for asynchronous pub/sub.
    queue = asyncio.Queue[tuple[str, str]](WORKERS)
    # Dict containing the results of fetching the file checksums.
    result: dict[str, dict[str, str]] = {}

    # Create the workers.
    workers = [
        asyncio.create_task(worker(loop, queue, mutex, result)) for _ in range(WORKERS)
    ]

    logging.info("Fetching hashes...")

    # Feed the urls to the workers. The fixed capacity of the queue ensures
    # that we never hold all the urls in memory at the same time. When the
    # queue reaches full capacity, this will block until a worker dequeues an
    # item.
    for version, assets in content.items():
        for asset in assets:
            await queue.put((version, asset))

    # Wait for all enqueued items to be processed.
    await queue.join()

    # At this point, the workers are idly waiting for the next queue item and
    # are no longer needed. Gracefully clean them up before continuing.
    for w in workers:
        w.cancel()

    write_results(result)

    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(asyncio.run(main()))
    except KeyboardInterrupt:
        # Suppress KeyboardInterrupt stack traces.
        raise SystemExit(1)
