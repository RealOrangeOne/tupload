import argparse
from tupload.common import upload
import os
import subprocess
import tempfile
import time


def capture():
    temp_file = tempfile.mkstemp()[1]
    img_output = subprocess.run(['gnome-screenshot', '-f', temp_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    assert img_output.returncode == 0
    return temp_file


def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument("--progress", action="store_true", help="Show Upload Progress")
    args = parser.parse_args()
    captured_file = capture()
    if not os.path.exists(captured_file) or os.path.getsize(captured_file) == 0:
        print("Failed to capture image.")
        exit(1)
    remote_file = "sc-{}.png".format(int(time.time()))
    url = upload(captured_file, remote_file_name=remote_file, progress=args.progress)
    os.remove(captured_file)
    print(url)
