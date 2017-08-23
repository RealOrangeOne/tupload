import argparse
from upload.common import upload
import os


def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    parser.add_argument("--progress", action="store_true", help="Show Upload Progress")
    args = parser.parse_args()
    input_file = os.path.abspath(args.file)
    assert os.path.isfile(input_file)
    url = upload(input_file, progress=args.progress)
    print(url)
