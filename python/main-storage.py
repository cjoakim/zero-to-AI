"""
Usage:
  CLI app for Azure Storage.
  python main-storage.py <func>
  python main-storage.py check_env
  python main-storage.py execute_examples 5
"""

# Chris Joakim, 3Cloud/Cognizant, 2026

import json
import os
import sys
import time
import tomllib
import traceback

from docopt import docopt
from dotenv import load_dotenv

from src.app.app import App
from src.io.fs import FS
from src.io.storage_util import StorageUtil
from src.os.env import Env


def print_options(msg):
    print(msg)
    arguments = docopt(__doc__, version="1.0.0")
    print(arguments)


def check_env():
    for name in sorted(os.environ.keys()):
        if name.startswith("AZURE_STORAGE_"):
            print("{}: {}".format(name, os.environ[name]))
    conn_str = Env.azure_storage_conn_string()
    print(f"Env.azure_storage_conn_string(): {conn_str}")

def execute_examples(sleep_time: int = 3):
    print("\n===== StorageUtil constructor")
    conn_str = Env.azure_storage_conn_string()
    #print(f"conn_str: {conn_str}")
    storage_util = StorageUtil(conn_str, logging_level=None)
    time.sleep(sleep_time)

    print("\n===== initial listing, and deletion of execute_examples containers")
    containers = storage_util.list_containers()
    print(f"Current storage containers: {containers}")
    for container in containers:
        if container.startswith("execute-examples"):
            print(f"Deleting container: {container}")
            if storage_util.delete_container(container):
                print(f"Container '{container}' deleted successfully.")
            else:
                print(f"Container '{container}' does not exist or could not be deleted.")
        else:
            print(f"Retaining container: {container} (not a execute-examples container)")
    time.sleep(sleep_time)

    cname = "execute-examples-{}".format(int(Env.epoch()))

    print("\n===== creating a new container named: {}".format(cname))
    created_container = storage_util.create_container(cname)
    if created_container:
        print(f"Container '{created_container}' created successfully.")
    else:
        print(f"Failed to create container '{cname}'.")
    time.sleep(sleep_time)

    print("\n===== uploading pyproject.toml, with optional metadata attributes")
    lines = FS.read_lines("pyproject.toml")
    line_count = str(len(lines))
    print(f"pyproject.toml has {len(lines)} lines")
    metadata = {
        "description": "pyproject.toml file for the zero-to-AI project",
        "line_count": line_count,
    }
    result = storage_util.upload_file(cname, "pyproject.toml", metadata=metadata, replace=True)
    print(f"Upload result: {result}")
    time.sleep(sleep_time)

    print("\n===== uploading data/stdlib.json")
    result = storage_util.upload_file(cname, "data/stdlib.json", replace=True)
    print(f"Upload result: {result}")
    time.sleep(sleep_time)

    print("\n===== list containers again")
    containers = storage_util.list_containers()
    print(f"Containers: {containers}")
    FS.write_json(containers, "tmp/storage-containers.json", pretty=True, sort_keys=True)
    time.sleep(sleep_time)

    # print("\n===== list container, with blob details")
    # blobs = storage_util.list_container(cname, names_only=False)
    # for b in blobs:
    #     print("---\nlist item: {}".format(b))
    #     for key in b.keys():
    #         print(f"  item key: {key}: {b[key]}")
    # time.sleep(sleep_time)

    print("\n===== list container, blob names only")
    blobs = storage_util.list_container(cname, names_only=True)
    print(f"Blobs in '{cname}': {blobs}")
    FS.write_json(blobs, "tmp/storage-blobs.json", pretty=True, sort_keys=True)
    time.sleep(sleep_time)

    print("\n===== download_blob_to_file: pyproject.toml -> tmp/pyproject_downloaded.toml")
    result = storage_util.download_blob_to_file(
        cname, "pyproject.toml", "tmp/pyproject_downloaded.toml"
    )
    print(f"Download result: {result}")
    print(f"Download result metadata: {result[1]['metadata']}")
    time.sleep(sleep_time)

    print("\n===== download_blob_to_file: data/stdlib.json -> tmp/stdlib.json")
    result = storage_util.download_blob_to_file(cname, "data/stdlib.json", "tmp/stdlib.json")
    print(f"Download result: {result}")
    time.sleep(sleep_time)

    print("\n===== parse the downloaded pyproject file with tomllib.load()")
    with open("tmp/pyproject_downloaded.toml", "rb") as f:
        data = tomllib.load(f)
    print(f"project name: {data['project']['name']}")
    print(f"project version: {data['project']['version']}")
    print(f"project description: {data['project']['description']}")
    print(f"project dependencies: {data['project']['dependencies']}")
    FS.write_json(data, "tmp/pyproject_downloaded.json", pretty=True, sort_keys=True)
    time.sleep(sleep_time)

    # print("\n===== download_blob_as_string, then parse it with json.loads()")
    # txt = storage_util.download_blob_as_string(cname, "data/stdlib.json")
    # print(json.loads(txt))
    # time.sleep(sleep_time)
    # print("\ndone")


if __name__ == "__main__":
    try:
        if len(sys.argv) < 2:
            print_options("Error: no CLI args provided")
        else:
            App.initialize()
            func = sys.argv[1].lower()
            if func == "check_env":
                check_env()
            elif func == "execute_examples":
                sleep_time = int(sys.argv[2])
                execute_examples(sleep_time)
            else:
                print_options("Error: invalid function: {}".format(func))
    except Exception as e:
        print(str(e))
        print(traceback.format_exc())
