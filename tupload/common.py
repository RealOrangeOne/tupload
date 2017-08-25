import subprocess
import os
import json


def expand_path(path):
    return os.path.abspath(os.path.expanduser(os.path.expandvars(path)))

CONFIG_PATH = expand_path("/etc/.updated")


def get_config(key, config):
    if not os.path.isfile(CONFIG_PATH):
        raise FileNotFoundError("Couldn't find config file at {}.".format(CONFIG_PATH))

    with open(CONFIG_PATH) as config_file:
        data = json.load(config_file)
    if config not in data:
        raise KeyError("Couldnt find configuration {}".format(config))
    required_config = data[config]
    if key not in required_config:
        raise KeyError("{} is missing key {}.".format(config, key))
    return required_config[key]


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
    viewable_root=None,
    server=None,
    remote_path=None,
    remote_file_name=None,
    clipboard=True,
    progress=False,
    config='default'
):
    if remote_file_name is None:
        remote_file_name = os.path.basename(source)
    if viewable_root is None:
        viewable_root = get_config("viewable_root", config)
    if server is None:
        server = get_config("destination_server", config)
    if remote_path is None:
        remote_path = get_config("remote_path", config)

    dest_path = os.path.join(remote_path, remote_file_name)
    remote_path = os.path.join(viewable_root, remote_file_name)
    upload_file(source, "{}:{}".format(server, dest_path), progress=progress)
    if clipboard:
        copy_to_clipboard(remote_path)
    return remote_path



