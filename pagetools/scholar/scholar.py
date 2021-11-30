from bs4 import BeautifulSoup as bs
from pagetools.utils.ffx import fxget
from pagetools.utils.haskey import haskey
from pagetools.utils.args import encode_url_args
from pagetools.parsers.apa2bib import apa2bib
import time
class Citations:
    def __init__(self,schid):
        self.citeurl=f'https://scholar.google.com/scholar?q=info:{schid}:scholar.google.com/&output=cite'
        content=fxget(self.citeurl)
        print(content)
        soup=bs(content,'html.parser')
        self.cites_clean=tuple(soup.find_all(class_='gs_citr'))
        self.mla,self.apa,self.iso690=[i.text for i in self.cites_clean]
        print()
        print()
        print(self.apa)
        self.bibtex=apa2bib(self.apa)
class Item:
    def __init__(self,title,link,authorline,abstract,schid):
        self.title=title
        self.link=link
        self.authors=[aut.strip() for aut in authorline.split(',')]
        self.abstract=abstract
        self.id=schid
    def get_citations(self):
        time.sleep(1)
        return Citations(self.id)
class Results:
    def __init__(self,items):
        self.items=[]
        for item in items:
            self.items.append(Item(item.find('h3').a.text,item.find('h3').a['href'],item.find('div',class_='gs_a').text,item.find('div',class_='gs_rs').text,item['data-cid']))
    def __getitem__(self,i):
        return self.items[i]
    def __iter__(self):
        return iter(self.items)
    def __contains__(self,tem):
        return tem in self.items

def scholar_parse(html):
    soup=bs(html,'html.parser')
    items=soup.find_all('div',class_='gs_r gs_or gs_scl')
    return Results(items)
def scholar_search(**kwargs):
    if not kwargs:
        raise ValueError('empty search parameters')
    url=f'https://scholar.google.com/scholar_lookup{encode_url_args(kwargs)}'
    return scholar_parse(fxget(url)),url
