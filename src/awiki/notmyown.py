from .config import AwikiConfig
from .page import Page
import re
from bisect import insort

pagelink_regex = re.compile(r"\[([a-zA-Z0-9_-]+)\]\(\1\)")


def get_notmyown_pages(awiki_config=None):
    awiki_config = awiki_config or AwikiConfig()
    notmyown = Page(awiki_config.notmyown)
    pages = {}
    current = None
    _, _ ,notmyown_md = notmyown.load()
    for link_match in pagelink_regex.findall(notmyown_md):
        if not link_match:
            continue
        letter = link_match[0].upper()
        if letter not in pages:
            pages[letter] = []
        insort(pages[letter], link_match)
    return pages


def write_notmyown_pages(pages, awiki_config=None):
    notmyown = Page(awiki_config.notmyown)
    meta, _, _ = notmyown.load()
    lines = []
    for letter in "ABDEFGHIJKLMNOPQRSTUVWXYZ":
        lines.append(f"### {letter}")
        for page in pages.get(letter, ()):
            lines.append(f"* [{page}]({page})")
    notmyown.save(meta, "\n".join(lines))
