import requests
import io
from bs4 import BeautifulSoup as bs
from .get_bib import get_bib_arxiv, get_bib_doi
import re
from awiki.config import AwikiConfig
from awiki.page import Page
import unidecode
import datetime

class ArxivPage:
    def __init__(
        self, title, authors, arxiv_id, doi, jref, comment, abstract, published, awiki_config
    ):
        self.title = title
        self.authors = authors
        self.arxiv_id = re.sub(r"v\d+$", "", arxiv_id)
        self.doi = doi
        self.jref = jref
        self.comment = comment
        self.abstract = abstract
        self.published = published
        self.page_id = self.get_page_id(awiki_config)
        self.myown = awiki_config.name in [unidecode.unidecode(author.split()[-1].lower()) for author in self.authors]
        self.existing_page = self.get_existing_page()
    def get_bibtex(self):
        return get_bib_doi(self.doi) or get_bib_arxiv(self.arxiv_id)

    def get_page_id(self, awiki_config=None):
        awiki_config=awiki_config or AwikiConfig()
        for page_id in self._generate_possible_page_ids():
            if len(page_id)>=awiki_config.max_title_chars:
                return page_id
        return page_id
    
    def _generate_possible_page_ids(self):
        title_items = [
            unidecode.unidecode(self.authors[0].split()[-1]).lower(),
            str(self.published.year),
        ]
        words = re.sub('[^a-zA-Z0-9]',' ',unidecode.unidecode(self.title).lower()).split()
        for w in words:
            yield ''.join(title_items)
            title_items.append(w)
    
    def get_existing_page(self):
        for page_id in self._generate_possible_page_ids():
            page = Page(page_id)
            if page.exists:
                return page

def arxiv_search(query, field, max_results, awiki_config):
    query=unidecode.unidecode(query)
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
            awiki_config
        )
