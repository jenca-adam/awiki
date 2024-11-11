from .config import AwikiConfig
from .page import Page
import yaml
import os


def get_all_tags(awiki_config=None):
    awiki_config = awiki_config or AwikiConfig()
    tags = set()
    for page_name in os.listdir(
        os.path.join(awiki_config.project_root, awiki_config.pages_dir)
    ):
        page = Page(page_name)
        if not page.exists:
            continue
        metadata, _, _ = page.load()
        tags.update(metadata.get("tags", set()))
    return list(tags)


def get_taglist_tags(awiki_config=None):
    awiki_config = awiki_config or AwikiConfig()
    tags_file = os.path.join(
        awiki_config.project_root, awiki_config.awiki_dir, "taglist.yaml"
    )
    if not os.path.exists(tags_file):
        return []
    with open(tags_file, "r") as f:
        return yaml.safe_load(f)


def add_tags(tags, awiki_config=None):
    awiki_config = awiki_config or AwikiConfig()
    current_tags = set(get_taglist_tags())
    tags_file = os.path.join(
        awiki_config.project_root, awiki_config.awiki_dir, "taglist.yaml"
    )
    current_tags.update(set(tags))
    with open(tags_file, "w") as f:
        yaml.safe_dump(list(current_tags), f)
