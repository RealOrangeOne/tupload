import subprocess
import os
import json

CONFIG_PATH = os.path.expanduser('~/.upload')


def config(key):
    if not os.path.isfile(CONFIG_PATH):
        raise FileNotFoundError("Couldn't find config file at {}.".format(CONFIG_PATH))

    with open(CONFIG_PATH) as config_file:
        data = json.load(config_file)
    return data.get(key)


def copy_to_clipboard(value):
    output = subprocess.run(['xclip', '-selection', 'clipboard'], input=value.encode())
    assert output.returncode == 0
    return value


def upload_file(source, remote, progress):
    args = ['rsync', source, remote]
    if progress:
        args.append('--progress')
    upload_output = subprocess.run(args)
    assert upload_output.returncode == 0


def upload(
    source,
    viewable_root=config("viewable_root"),
    server=config("destination_server"),
    remote_path=config("remote_path"),
    remote_file_name=None,
    clipboard=True,
    progress=False
):
    if remote_file_name is None:
        remote_file_name = os.path.basename(source)
    dest_path = os.path.join(remote_path, remote_file_name)
    remote_path = os.path.join(viewable_root, remote_file_name)
    upload_file(source, "{}:{}".format(server, dest_path), progress=progress)
    if clipboard:
        copy_to_clipboard(remote_path)
    return remote_path



