import os
import click
import time
from bs4 import BeautifulSoup as bs
from .page import Page
from .pagetools.bibtools import Bib
from .pagetools.arxiv import arxiv_search


def get_page_arxiv_id(metadata, html):
    if "arxiv_id" in metadata:
        return metadata["arxiv_id"]
    else:
        soup = bs(html, "html.parser")
        for link in soup.find_all("a"):
            if (
                link.text.startswith("arxiv:")
                and link.has_attr("href")
                and link["href"].startswith("https://arxiv.org/abs/")
            ):
                return link["href"].split("/abs/", 1)[1]


def fix_page_archive_prefix(
    page_name, fix_metadata, fix_arxiv_bib, awiki_config, wait_time=0
):
    page = Page(page_name, awiki_config)
    if not page.exists:
        click.echo(
            click.style(f"Couldn't load page {page_name}", fg="bright_red", bold=True)
        )
        return
    page_metadata, html, markdown = page.load()
    arxiv_id = get_page_arxiv_id(page_metadata, html)
    if not arxiv_id:
        click.echo(
            click.style(f"{page_name} has no arxiv page", fg="yellow", bold=False)
        )
        return
    click.echo(
        click.style(
            click.style(f"{page_name}: ", bold=True) + f"{arxiv_id=}",
            fg="bright_green",
        )
    )
    bib_path = os.path.join(page.root, "bib.bib")
    bib = None
    if not os.path.exists(bib_path):
        click.echo(
            click.style(
                f"{page_name} has no bib.bib, creating a fallback",
                fg="bright_yellow",
                bold=False,
            )
        )
        bib = Bib("article", page_name, {})

    else:
        with open(bib_path, "r") as f:
            try:
                bib = Bib.parse(f)
            except Exception as e:
                click.echo(
                    click.style(
                        f"{page_name}: couldn't read bib: {str(e)}. Refusing to overwrite!",
                        fg="bright_red",
                        bold=True,
                    )
                )
                return
    bib.fields.setdefault("archivePrefix", "arXiv")
    bib.fields.setdefault("eprint", arxiv_id)

    if "/" in arxiv_id:
        primary_class = arxiv_id.split("/")[0]
        bib.fields.setdefault("primaryClass", primary_class)

    if not fix_metadata:
        with open(bib_path, "w") as f:
            f.write(bib.serialise(style=awiki_config.bibtex_style))
        return
    time.sleep(wait_time)
    arxiv_pages = list(arxiv_search(arxiv_id, "id", 1, awiki_config, True))
    if not arxiv_pages:
        click.echo(
            click.style(
                f"{page_name}: {arxiv_id} not found. not adding metadata",
                fg="yellow",
            )
        )
        return
    arxiv_page = arxiv_pages[0]
    if fix_metadata:
        arxiv_metadata = arxiv_page.get_metadata()
        arxiv_metadata.update(page_metadata)
        page.save(arxiv_metadata, markdown)
    if fix_arxiv_bib:
        arxiv_bib = arxiv_page.get_bibtex()
        for field, value in arxiv_bib.fields.items():
            bib.fields.setdefault(field, value)
    with open(bib_path, "w") as f:
        f.write(bib.serialise(style=awiki_config.bibtex_style))


def fix_archive_prefix(awiki_config, fix_metadata, fix_arxiv_bib):
    for page_name in os.listdir(
        os.path.join(awiki_config.project_root, awiki_config.pages_dir)
    ):
        fix_page_archive_prefix(
            page_name,
            fix_metadata,
            fix_arxiv_bib,
            awiki_config,
            3 * (fix_metadata or fix_arxiv_bib),
        )
