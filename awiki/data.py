import pathlib
import os
import site
from .err import AwikiError

AWIKI_DATA_DIR = None
AWIKI_DIR_SEARCH_DIRS = ["/usr", "/usr/local", site.USER_BASE]


def find_awiki_data_dir():
    global AWIKI_DATA_DIR
    for search_dir in AWIKI_DIR_SEARCH_DIRS:
        path = os.path.join(search_dir, "share/awiki")
        if os.path.exists(path):
            AWIKI_DATA_DIR = pathlib.Path(path)
            return
    raise AwikiError(
        f"Can't find awiki data directory. Check your awiki installation. Checked: {[os.path.join(sd,'share/awiki') for sd in AWIKI_DIR_SEARCH_DIRS]}"
    )


def get_path(path_name):
    return AWIKI_DATA_DIR / path_name
