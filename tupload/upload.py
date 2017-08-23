import argparse
from tupload.common import upload, expand_path
import os


def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    parser.add_argument("--progress", action="store_true", help="Show Upload Progress")
    parser.add_argument("--to", help="Configuration to upload to", default='default')
    args = parser.parse_args()
    input_file = expand_path(args.file)
    assert os.path.isfile(input_file)
    url = upload(input_file, progress=args.progress, config=args.to)
    print(url)
