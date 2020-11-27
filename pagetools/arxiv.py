from bs4 import BeautifulSoup as bs
import httplib2
import sys
import re
import os
class ArXivPage:
    def __init__(self,arxivid):
        os.chdir('/home/anna/work/awiki/pages')
        self.dateline_pattern=r'\D*\d+(\D+)(\d+)'
        self.authors_pattern=r'Authors:(\D*)'
        self.link=f'https://arxiv.org/abs/{arxivid}'
        self.h=httplib2.Http()
        print(f'requesting {self.link}...',file=sys.__stdout__)
        response,content=self.h.request(self.link)
        print(f'parsing {self.link}...',file=sys.__stdout__)
        soup=bs(content,'html.parser')
        print('loading date...',file=sys.__stdout__)
        self.dateline=str(soup.find_all('div',class_='dateline')[0].text)
        match=re.search(self.dateline_pattern,self.dateline)
        dategroups=match.groups()
        self.month=dategroups[0]
        self.year=dategroups[1]
        print(self.month,self.year)
        print('loading title...',file=sys.__stdout__)
        self.title=str(soup.find_all('h1',class_='title mathjax')[0].text).replace('Title:','')
        print('loading authors...',file=sys.__stdout__)
        self.strauthors=str(soup.find_all('div',class_='authors')[0].text)
        match=re.search(self.authors_pattern,self.strauthors)
        self.authors=match.groups()[0].split(', ')
        print('loading journal refs...',file=sys.__stdout__)
        jrefs=soup.find('td',class_='tablecell jref')
        if not jrefs:
            print(f'WARNING:No journal refs!')
            self.jrefs=''
        else:
            self.jrefs=jrefs.text
        print('loading abstract...')
        self.abstract=soup.find_all('blockquote',class_="abstract mathjax")[0].text
