from .config import DEFAULT_CONFIG, AwikiConfig
from .data import get_path
import os
import shutil
import pyaml
from .err import AwikiError
import click
import unidecode
def awiki_init(pages_dir, static_dir, awiki_dir, name):
    if os.path.exists(awiki_dir):
        if not click.confirm(f"directory exists: {awiki_dir!r} . overwrite?"):
            raise AwikiError("awiki already initialised here")
        else:
            shutil.rmtree(awiki_dir)
    if not os.path.exists(pages_dir):
        os.mkdir(pages_dir)
    if not os.path.isdir(pages_dir):
        raise AwikiError(f"{pages_dir}: not a directory")
    if not os.path.exists(static_dir):
        os.mkdir(static_dir)
    if not os.path.isdir(static_dir):
        raise AwikiError(f"{static_dir}: not a directory")
    shutil.copytree(get_path(""), awiki_dir)
    project_root = os.getcwd()
    awk_dict = DEFAULT_CONFIG
    awk_dict.update(
            {"pages_dir": pages_dir, "awiki_dir":awiki_dir, "static_dir": static_dir, "project_root": project_root, "name": unidecode.unidecode(name).lower()}
    )
    with open("awiki_config.yaml", "w") as f:
        pyaml.dump({"awiki": awk_dict}, f)

def awiki_reload_data():
    awiki_config=AwikiConfig()
    if os.path.exists(awiki_config.awiki_dir):
        shutil.rmtree(awiki_config.awiki_dir)
    shutil.copytree(get_path(""), awiki_config.awiki_dir)

