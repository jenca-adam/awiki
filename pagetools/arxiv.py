from bs4 import BeautifulSoup as bs
import httplib2
import sys
import re
import os
from .special import CachedH
from .pathos import make_authors

class ArXivPage:
    def __init__(self,arxivid):
        os.chdir(os.path.expanduser('~')+'/work/awiki/pages')
        self.arxivid=arxivid
        self.old=False
        if not re.search(r'\d+.\d+',self.arxivid):
            self.old=True
        self.dateline_pattern=r'\D*\d+(\D+)(\d+)'
        self.authors_pattern=r'Authors:(\D*)'
        self.link=f'https://arxiv.org/abs/{arxivid}'
        self.h=CachedH()
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
        _strauthors_prefix='<b style="color:green;">Authors:&nbsp;&nbsp;</b>'
        match=re.search(self.authors_pattern,self.strauthors)
        self.authors=match.groups()[0].split(', ')
        self.strauthors=_strauthors_prefix+make_authors(self.authors)
        print('loading journal refs...',file=sys.__stdout__)
        jrefs=soup.find('td',class_='tablecell jref')
        if not jrefs:
            print(f'WARNING:No journal refs!')
            self.jrefs=''
        else:
            self.jrefs=jrefs.text
        print('loading abstract...')
        self.abstract=soup.find_all('blockquote',class_="abstract mathjax")[0].text[10:]
        os.chdir('..')
    def html(self):
        img='<div class="warning"><img src="/static/img/warning.png/" width=100, height=100/><b>WARNING!</b> This is\
        from old version of ArXiv. This page after adding may not work correctly.</div>'if self.old else ''
        return f'''<html>
                   <head>
                       <title>ArXiv Page: {self.title} ({self.arxivid})</title>
                        <link href="https://fonts.googleapis.com/css?family=Lato%7COpen+Sans&amp;subset=latin-ext" rel="stylesheet"> 

                        <link rel="stylesheet" href="/static/css/pocketgrid.min.css">
                        <link rel="stylesheet" href="/static/css/style.css">
                        <link rel="shortcut icon" href="/static/favicon/favicon.ico">
                        <script type="text/x-mathjax-config">'''+'''
                        MathJax.Hub.Config({
                          tex2jax: {inlineMath: [['$','$'], ['\\(','\\)']]}
                        });
                        </script>

                        <script type="text/javascript" async
                           src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-MML-AM_CHTML">
                        </script>
                        <script type="text/javascript">
                        function postForm(){
                          form=document.getElementById("form")
                          form.submit()
                        }
                        </script>

                        <script src="/static/codemirror/codemirror.js"></script>
                        <link rel="stylesheet" href="/static/codemirror/codemirror.css">
                        <script src="/static/codemirror/mode/markdown/markdown.js"></script>
                        <script src="/static/codemirror/dialog.js"></script>
                        <link rel="stylesheet" href="/static/codemirror/dialog.css">
                        <script src="/static/codemirror/searchcursor.js"></script>
                        <script src="/static/codemirror/vim.js"></script>


                    </head>'''+f'''
                    <body>
                       <div id="container">
                            {img}
                            <a id="arxiv-link" href="{self.link}">View in ArXiv</a>
                                
                            <div id="buttons">
                                <a id="addpage-link" href="/addpage/{self.arxivid}">Add this page</a>
                            </div>
                            <div id="dateline">{self.dateline}</div>
                            <h1>{self.title}</h1>
                            <div id="gap-hidden">
                            <br>
                            <br>
                            </div>

                            <div id="authors">{self.strauthors}</div>
                            <div id="gap-hidden">
                            <br>
                            <br>
                            </div>
                            <hr>

                            <div id="abstract">
                            <h2>Abstract</h2>
                            <div id="abstract-inner" style="font-size:14pt;">
                            {self.abstract}
                            </div>
                            </div>
                        </div>
                    </body>
                    </html>'''

