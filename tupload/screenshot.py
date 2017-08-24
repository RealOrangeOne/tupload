import argparse
from tupload.common import upload, get_config
import os
import subprocess
import tempfile
import time
import random
from string import hexdigits


def capture(capture_mode, include_pointer=False):
    temp_file = tempfile.mkstemp()[1]
    args = ['gnome-screenshot', capture_mode, '-f', temp_file]
    if include_pointer:
        args.append('-p')
    img_output = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
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


def get_capture_mode(args):
    if args.window:
        return '-w'
    elif args.area:
        return '-a'
    return ''


def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument("--progress", action="store_true", help="Show Upload Progress")
    parser.add_argument("--to", help="Configuration to upload to", default='default')
    parser.add_argument("-w", "--window", action="store_true")
    parser.add_argument("-a", "--area", action="store_true")
    parser.add_argument("-p", "--include-pointer", action="store_true")
    args = parser.parse_args()
    if args.window and args.area:
        print("Can't use window and area")
        exit(1)
    capture_mode = get_capture_mode(args)
    captured_file = capture(capture_mode, args.include_pointer)
    if not os.path.exists(captured_file) or os.path.getsize(captured_file) == 0:
        print("Failed to capture image.")
        exit(1)
    url = upload(captured_file, remote_file_name=get_remote_filename(args.to), progress=args.progress, config=args.to)
    os.remove(captured_file)
    print(url)
