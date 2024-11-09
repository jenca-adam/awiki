from .config import DEFAULT_CONFIG
from .data import get_path
import os
import shutil
import pyaml


def awiki_init(pages_dir, static_dir):
    if os.path.exists(".awiki"):
        raise AwikiError("awiki already initialised here")
    if not os.path.exists(pages_dir):
        os.mkdir(pages_dir)
    if not os.path.isdir(pages_dir):
        raise AwikiError(f"{pages_dir}: not a directory")
    if not os.path.exists(static_dir):
        os.mkdir(static_dir)
    if not os.path.isdir(static_dir):
        raise AwikiError(f"{static_dir}: not a directory")
    shutil.copytree(get_path(""), ".awiki")
    project_root = os.getcwd()
    awk_dict = DEFAULT_CONFIG
    awk_dict.update(
        {"pages_dir": pages_dir, "static_dir": static_dir, "project_root": project_root}
    )
    with open("awiki_config.yaml", "w") as f:
        pyaml.dump({"awiki": awk_dict}, f)
