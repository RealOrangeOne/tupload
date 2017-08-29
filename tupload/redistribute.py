from tupload.common import upload, terminate
import urllib.error
import urllib.request
import urllib.parse
import os
import argparse


def download_handle(count, block_size, total_size):
    if total_size < 1:
        return
    print("{}%\r".format(int(count * block_size * 100 / total_size)))


def download_url(url, progress=False):
    try:
        download_location, headers = urllib.request.urlretrieve(url, reporthook=download_handle if progress else None)
    except urllib.error.HTTPError as e:
        if e.code == 404:
            terminate("Couldn't find file at {}.".format(url))
        raise
    return download_location


def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    parser.add_argument("--progress", action="store_true", help="Show Download / Upload Progress")
    parser.add_argument("--to", help="Configuration to upload to", default='default')
    args = parser.parse_args()
    parsed_url = urllib.parse.urlparse(args.url)
    filename = urllib.parse.quote(os.path.basename(parsed_url.path))
    if not parsed_url.path or not filename:
        terminate("Failed to read filename from {}.".format(args.url))
    local_file = download_url("https://google.co.uk", args.progress)
    url = upload(local_file, remote_file_name=filename, progress=args.progress, config=args.to)
    os.remove(local_file)
    print(url)
