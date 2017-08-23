import argparse
from tupload.common import upload, get_config
import os
import subprocess
import tempfile
import time
import random
from string import hexdigits


def capture():
    temp_file = tempfile.mkstemp()[1]
    img_output = subprocess.run(['gnome-screenshot', '-f', temp_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    assert img_output.returncode == 0
    return temp_file


def get_remote_filename(config):
    preset = get_config('screenshot_preset', config).lower()
    presets = {
        'timestamp': int(time.time()),
        'hex': ''.join(random.sample(hexdigits, 8)).lower()
    }
    if preset not in presets:
        raise KeyError("Invalid preset {}.".format(preset))
    return str(presets[preset]) + '.png'


def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument("--progress", action="store_true", help="Show Upload Progress")
    parser.add_argument("--to", help="Configuration to upload to", default='default')
    args = parser.parse_args()
    captured_file = capture()
    if not os.path.exists(captured_file) or os.path.getsize(captured_file) == 0:
        print("Failed to capture image.")
        exit(1)
    url = upload(captured_file, remote_file_name=get_remote_filename(args.to), progress=args.progress, config=args.to)
    os.remove(captured_file)
    print(url)
