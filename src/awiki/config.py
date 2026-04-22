import yaml
import pyaml
import os
from .err import AwikiError

DEFAULT_CONFIG = {
    "port": 8000,
    "max_title_chars": 18,
    "notmyown": "notmyown",
    "myown": "myown",
}


class AwikiConfig:
    def __init__(self):
        cnf_dir = os.getcwd()
        found = False
        while cnf_dir != "/":
            if os.path.exists(os.path.join(cnf_dir, "awiki_config.yaml")):
                found = True
                break
            cnf_dir = os.path.realpath(os.path.join(cnf_dir, os.pardir))
        os.chdir(cnf_dir)
        if not found:
            raise AwikiError(
                "can't find project config file 'awiki_config.yaml' (here or in any parent)\ncheck that you're in the correct directory and try again\nalternatively, run 'awiki init'"
            )
        with open("awiki_config.yaml") as f:
            config_dict = yaml.load(f, yaml.Loader)
        if not isinstance(config_dict.get("awiki"), dict):
            raise AwikiError("config file malformed")
        self.config_dict = config_dict["awiki"]

    def __getattr__(self, attr):
        result = self.config_dict.get(attr, DEFAULT_CONFIG.get(attr))
        if result is None:
            raise AwikiError(f"missing config attribute: {attr}")
        return result
