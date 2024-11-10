import yaml
import pyaml
import os
from .err import AwikiError

DEFAULT_CONFIG = {
    "port": 8000,
    "awiki_dir": "awiki",
    "static_dir": "static",
    "max_title_chars": 18,
    "notmyown": "notmyown",
    "myown": "myown"
}


class AwikiConfig:
    def __init__(self):
        if not os.path.exists("awiki_config.yaml"):
            raise AwikiError(
                "can't find project config file 'awiki_config.yaml'\ncheck that you're in the correct directory and try again\nalternatively, run 'awiki init'"
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
