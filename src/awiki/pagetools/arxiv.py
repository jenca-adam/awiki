import requests
import io
from bs4 import BeautifulSoup as bs
from .get_bib import get_bib_arxiv, get_bib_doi
from . import bibtools
import re
from awiki.config import AwikiConfig
from awiki.page import Page
from awiki.markdown_templates import get_md_template
from awiki.myown import get_myown_pages, write_myown_pages
from awiki.notmyown import get_notmyown_pages, write_notmyown_pages
import unidecode
import datetime
import collections
import os

Author = collections.namedtuple("Author", ("first_names", "last_name"))


class ArxivPage:
    def __init__(
        self,
        title,
        authors,
        arxiv_id,
        doi,
        jref,
        comment,
        abstract,
        published,
        awiki_config,
    ):
        self.title = title
        self.authors = authors
        self.author_names = [Author(*(author.rsplit(None, 1))) for author in authors]
        self.arxiv_id = re.sub(r"v\d+$", "", arxiv_id)
        self.doi = doi
        self.jref = jref
        self.comment = comment
        self.abstract = abstract
        self.published = published
        self.page_id = self.get_page_id(awiki_config)
        self.myown = awiki_config.name in [
            unidecode.unidecode(author.split()[-1].lower()) for author in self.authors
        ]
        self.existing_page = self.get_existing_page()
        self.awiki_config = awiki_config

    def get_bibtex(self):
        bib = get_bib_doi(self.doi) or get_bib_arxiv(self.arxiv_id)
        if bib is None:
            return bibtools.Bib.plain(self.page_id)
        try:
            parsed = bibtools.Bib.parse_string(bib)
        except:
            return bibtools.Bib.plain(self.page_id)
        parsed.citekey = self.page_id
        return parsed

    def get_page_id(self, awiki_config=None):
        awiki_config = awiki_config or AwikiConfig()
        for page_id in self._generate_possible_page_ids():
            if len(page_id) >= awiki_config.max_title_chars:
                return page_id
        return page_id

    def _generate_possible_page_ids(self):
        title_items = [
            unidecode.unidecode(self.authors[0].split()[-1]).lower(),
            str(self.published.year),
        ]
        words = re.sub(
            "[^a-zA-Z0-9]", " ", unidecode.unidecode(self.title).lower()
        ).split()
        for w in words:
            yield "".join(title_items)
            title_items.append(w)

    def get_existing_page(self):
        for page_id in self._generate_possible_page_ids():
            page = Page(page_id)
            if page.exists:
                return page

    def add(self):
        if self.existing_page is not None:
            return self.existing_page.page_name
        page = Page(self.page_id)
        page.makedir()
        page_template = get_md_template("page")
        markdown = page_template.render(page=self)
        metadata = {
            "title": self.title,
            "authors": list(self.authors),
            "arxiv_id": self.arxiv_id,
        }
        if self.jref:
            metadata["jref"] = self.jref
        if self.doi:
            metadata["doi"] = self.doi
        if self.comment:
            metadata["arxiv_comment"] = self.comment
        if self.published:
            metadata["published"] = self.published.timestamp()
        bibtex = self.get_bibtex()
        # write bib
        with open(os.path.join(page.root, "bib.bib"), "w") as f:
            f.write(bibtex.serialise(style=self.awiki_config.bibtex_style))
        # write page
        page.save(metadata, markdown)
        # edit myown / notmyown
        if self.myown:
            myown_pages, after=get_myown_pages(self.awiki_config)
            if str(self.published.year) not in myown_pages:
                myown_pages[self.published.year]=[]
            myown_pages[str(self.published.year)].append(("1",self.page_id,""))
            write_myown_pages(myown_pages, after, self.awiki_config)
        else:
            notmyown_pages=get_notmyown_pages(self.awiki_config)
            if self.page_id[0].upper() not in notmyown_pages:
                notmyown_pages[self.page_id[0].upper()]=[]
            notmyown_pages[self.page_id[0].upper()].append(self.page_id)
            write_notmyown_pages(notmyown_pages, self.awiki_config)
        #done
        return self.page_id


def arxiv_search(query, field, max_results, awiki_config):
    query = unidecode.unidecode(query.replace(";", " AND "))
    url = f"https://export.arxiv.org/api/query?search_query={field}:{query}&max_results={max_results}"
    content = requests.get(url).content
    soup = bs(content, "xml")  # yes, barbaric
    for entry in soup.findAll("entry"):
        yield ArxivPage(
            entry.title.text,
            tuple(q.find("name").text for q in entry.find_all("author")),
            entry.id.text.split("abs/", 1)[1],
            getattr(entry.find("arxiv:doi"), "text", None),
            getattr(entry.find("arxiv:journal_ref"), "text", None),
            getattr(entry.find("arxiv:comment"), "text", None),
            getattr(entry.summary, "text", "No abstract."),
            datetime.datetime.fromisoformat(
                getattr(entry.published, "text", "1970-01-01T00:00:00")
            ),
            awiki_config,
        )
