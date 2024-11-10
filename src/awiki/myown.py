from .config import AwikiConfig
from .page import Page
import re

pagelink_regex = re.compile(r"(\d+). \[([a-zA-Z0-9_-]+)\]\(\2\)([^\[]*)")
pagename_regex = re.compile(r"[a-zA-Z_-]+(\d+)[a-zA-Z_-]+")

def get_myown_pages(awiki_config=None):
    awiki_config = awiki_config or AwikiConfig()
    myown = Page(awiki_config.myown)
    pages = {}
    current = None
    _, _ ,myown_md = myown.load()
    for line in myown_md.splitlines():
        for num, link, comment in pagelink_regex.findall(line):
            if not pagename_regex.match(link):
                continue
            year = pagename_regex.search(link).group(1)
            if year not in pages:
                pages[year] = []
            pages[year].append((num, link, comment))
    return pages


def write_myown_pages(pages, awiki_config=None):
    myown = Page(awiki_config.myown)
    meta, _, _ = myown.load()
    lines = []
    for year in sorted(pages.keys(), reverse=True):
        lines.append(f"### {year}")
        for num, link, comment in pages[year]:
            lines.append(f"{num}. [{link}]({link}){comment}")
    myown.save(meta, "\n".join(lines))
