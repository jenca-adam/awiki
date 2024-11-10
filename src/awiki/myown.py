from .config import AwikiConfig
from .page import Page
import re

pagelink_regex = re.compile(r"(\d+). \[([a-zA-Z0-9_-]+)\]\(\2\)([^\[]*)")
pagename_regex = re.compile(r"[a-zA-Z_-]+(\d+)[a-zA-Z_-]+")
year_regex = re.compile("^#+\s*\d+$")
other_regex = re.compile("^#+\s*\S*")
def get_myown_pages(awiki_config=None):
    awiki_config = awiki_config or AwikiConfig()
    myown = Page(awiki_config.myown)
    pages = {}
    current = "_START"
    _, _ ,myown_md = myown.load()
    after = {}
    for line in myown_md.splitlines():
        if not pagelink_regex.match(line) and not year_regex.match(line):
            if other_regex.match(line) and pages:
                current="_END"
            if current not in after:
                after[current]=[]
            after[current].append(line)
        for num, link, comment in pagelink_regex.findall(line):
            if current=="_END":
                after[current].append(f"{num}. [{link}]({link}) {comment}")
                continue
            current = link
            if not pagename_regex.match(link):
                continue
            year = pagename_regex.search(link).group(1)
            if year not in pages:
                pages[year] = []
            pages[year].append((num, link, comment))
    return pages, after


def write_myown_pages(pages, after, awiki_config=None):
    myown = Page(awiki_config.myown)
    meta, _, _ = myown.load()
    lines = after.get("_START", [])
    for year in sorted(pages.keys(), reverse=True):
        lines.append(f"### {year}")
        for num, link, comment in sorted(pages[year], key = lambda tup:tup[1]):
            lines.append(f"{num}. [{link}]({link}) {comment}")
            lines.extend(after.get(link, []))
    lines.extend(after.get("_END", []))
    myown.save(meta, "\n".join(lines))
