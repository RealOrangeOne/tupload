import argparse
from upload.common import upload
import os


def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    args = parser.parse_args()
    input_file = os.path.abspath(args.file)
    assert os.path.exists(input_file)
    url = upload(input_file)
    print(url)
