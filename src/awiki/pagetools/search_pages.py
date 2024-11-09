import re
import os
import unidecode
from awiki.config import AwikiConfig
from awiki.page import Page


def search_pages(query, awiki_config):
    try:
        pattern = re.compile(unidecode.unidecode(query).lower())
    except:
        return
    awiki_config = awiki_config or AwikiConfig()
    pages_dir = os.path.join(awiki_config.project_root, awiki_config.pages_dir)
    for page_name in os.listdir(pages_dir):
        page = Page(page_name)
        if not page.exists:
            continue
        meta, html, md = page.load()
        # search meta and md
        for val in [*meta.values(), page_name]:
            if pattern.search(
                unidecode.unidecode(val or page_name).lower(), re.IGNORECASE
            ):
                yield page_name
                break
        else:
            print(unidecode.unidecode(md))
            if pattern.search(unidecode.unidecode(md).lower(), re.IGNORECASE):
                yield page_name
