from bs4 import BeautifulSoup as bs
from pagetools.utils.ffx import fxget
from pagetools.utils.haskey import haskey
from pagetools.utils.args import encode_url_args
class Citations:
    def __init__(self,schid):
        self.citeurl=f'https://scholar.google.com/scholar?q=info:{schid}:scholar.google.com/&output=cite'
        content=fxget(self.citeurl)
        print(content)
        soup=bs(content,'html.parser')
        self.cites_clean=tuple(soup.find_all(class_='gs_citr'))
        self.mla,self.apa,self.iso690=self.cites_clean
        self.cites_advanced=[]
        for i in soup.find_all('a',class_='gs_citi'):
            c=i['href']
            self.cites_advanced.append(fxget(c))
        self.bibtex,self.endnote,self.refman,_=tuple(self.cites_advanced)
class Item:
    def __init__(self,title,link,authorline,abstract,schid):
        self.title=title
        self.link=link
        self.authors=[aut.strip() for aut in authorline.split(',')]
        self.abstract=abstract
        self.id=schid
        self.citations=Citations(schid)
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
    return scholar_parse(fxget(url))
