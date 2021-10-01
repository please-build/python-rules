from tools.wheel_resolver.src.wheel_tags.tags import get_download_urls, get_url


def run(package:str, version:str=None, archs:list=[]):
    download_urls = get_download_urls(package, version=None)
    return get_url(download_urls, archs)
