import argparse
from upload.common import upload
import os


def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    args = parser.parse_args()
    input_file = os.path.abspath(args.file)
    assert os.path.isfile(input_file)
    url = upload(input_file)
    print(url)
