#!/usr/bin/env python3

import subprocess
import os
import json
import argparse


def config(key):
    with open(os.path.expanduser('~/.upload')) as config_file:
        data = json.load(config_file)
    return data.get(key)


def copy_to_clipboard(value):
    output = subprocess.run(['xclip', '-selection', 'clipboard'], input=value.encode())
    assert output.returncode == 0
    return value


def upload_file(source, remote):
    upload_output = subprocess.run(['rsync', source, remote], stdout=subprocess.PIPE)
    assert upload_output.returncode == 0


def main(
    source,
    viewable_root=config("viewable_root"),
    server=config("destination_server"),
    remote_path=config("remote_path"),
    remote_file_name=None,
    clipboard=True,
):
    if remote_file_name is None:
        remote_file_name = os.path.basename(source)
    dest_path = os.path.join(remote_path, remote_file_name)
    remote_path = os.path.join(viewable_root, remote_file_name)
    upload_file(source, "{}:{}".format(server, dest_path))
    if clipboard:
        copy_to_clipboard(remote_path)
    return remote_path


def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    args = parser.parse_args()
    input_file = os.path.abspath(args.file)
    assert os.path.exists(input_file)
    url = main(input_file)
    print(url)
