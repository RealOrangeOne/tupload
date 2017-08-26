# TUpload

[![CircleCI](https://img.shields.io/circleci/project/github/RealOrangeOne/tupload.svg?style=flat-square)](https://circleci.com/gh/RealOrangeOne/tupload)

Upload files and screenshots to a server using `rsync`


## Usage

### `upload` / `tupload`
```
usage: upload [-h] [--progress] [--to TO] file

positional arguments:
  file

optional arguments:
  -h, --help  show this help message and exit
  --progress  Show Upload Progress
  --to TO     Configuration to upload to
```

```bash
upload README.md

upload README.md --to drop
```

### `screenshot`
```
usage: screenshot [-h] [--progress] [--to TO] [-w] [-a] [-p]

optional arguments:
  -h, --help            show this help message and exit
  --progress            Show Upload Progress
  --to TO               Configuration to upload to
  -w, --window
  -a, --area
  -p, --include-pointer
```

```bash
screenshot
 
screenshot -wp 

screenshot --to pics
```

## Configuration
Configuration is done using the config file at `/etc/.upload`, in JSON. Here's [an example](https://github.com/RealOrangeOne/tupload/blob/master/tupload/config.json).

Each top-level key is the name of a config, each config must define 3 keys:

- `destination_server`: The address to connect to. User information can be passed using standard SSH syntax.   
- `viewable_root`: The remote path the file can be viewed at. The file name will be joined to the end of this.
- `remote_path`: The directory on the server to put the file, should be writable by the connecting user

### Optional Keys
- `screenshot_preset`: Filename pattern to user for screenshot.
    - `hex`: 8 random lowercase hex characters
    - `timestamp`: unix timestamp of capture time
