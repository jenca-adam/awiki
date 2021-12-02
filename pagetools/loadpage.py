#!/usr/bin/env python3

import httplib2
from bs4 import BeautifulSoup as bs
import sys
import re
import colorama
import os
import shutil
from . import arxiv,special
from .bibtex import steal_bib,parse
from .common.exceptions import PageExistsError
from .utils.capitalized import capitalized,normalize_lower
from .utils.file import *
from .utils.name import makename,maketitle
from urllib.parse import urlsplit
BLUE=colorama.Fore.BLUE
RESET=colorama.Style.RESET_ALL
BOLD = '\033[1m'
RED=colorama.Fore.RED
GREEN=colorama.Fore.GREEN
CYAN=colorama.Fore.CYAN
YELLOW=colorama.Fore.LIGHTYELLOW_EX
MAGENTA=colorama.Fore.MAGENTA
dateline_pattern=r'\D*\d+(\D+)(\d+)'
title_pattern=r'<h1 class="title mathjax"><span class="descriptor">Title\:</span>(\D*)<'
authors_pattern=r'Authors:(\D*)'
linkstr_pattern=r'/?(.*?)$'
h=special.CachedH()
base=os.getcwd()

def loadpage(id):
    link=id
    os.chdir(f'{base}/pages')
    print(id)
    try:

        page=arxiv.ArXivPage(id)
    except IndexError:
        special.home()
        return {'status':'error','response':{'message':'No such page','type':id}}
    print(f'{BOLD}Start of informative output{RESET}')
    print(page.title)
    print(page.month,page.year)
    print(page.strauthors)
    print(page.abstract)
    print(f'{BOLD}End of informative output{RESET}')
    print('__________________________________________________')
    print(f'{GREEN}Writing page.md{RESET}')
    authorname=page.authors[0].split(' ')[-1].lower()
    thingname=maketitle(page.title)
    
    linkmatch=re.search(linkstr_pattern,link)
    linkid=linkmatch.groups()[0]
    print(linkid)
    print(f'{YELLOW}Stealing BibTex...{RESET}')
    bibtex,l,schlink=steal_bib(linkid)
    lpage=urlsplit(l).netloc
    print(f'BibTex is:\n{bibtex}')
    print(f'{BLUE}Parsing BibTex...{RESET}')
    bt_data=parse(bibtex)
    print(f'{MAGENTA}Page from year {bt_data.year}{RESET}')
    page.year=int(bt_data.year)
    page.jrefs=bt_data.journal
    name=makename(authorname,page.year,thingname)
    print(f'{YELLOW}Directory name:{name}{RESET}')

 
    try:
        os.mkdir(os.path.expanduser('~')+'/work/awiki/pages/'+name)
        os.chdir(os.path.expanduser('~')+'/work/awiki/pages/'+name)
    except FileExistsError as err:
        print(f'{RED}dir {name} already exists.Skipping.{RESET}')
        special.home()
        #return {'status':'error','response':{'message':str(err),'type':'FileExistsError'}}
        raise PageExistsError(
        f'''page {name!r} already exists! Awiki will automatically try to clean up empty pages. If
        you see "CLEANUP: ****" in green color, refreshing page should work, but not always.''') 
    linkstr=f'[arxiv:{linkid}](https://arxiv.org/abs/{linkid})\n[View at {lpage}]({l})\n[View at Google Scholar]({schlink}) '

    pagestring=f'title: {name}\n---\n\n\n## Reference\n\n{(", ").join(page.authors)},{page.title},{page.jrefs},{page.month}\b{page.year},\n\n## Abstract \n{page.abstract}\n\n{linkstr}'
    print(f'{name}/page.md:\n\n{CYAN}{pagestring}{RESET}')
    print(os.getcwd())
    with open('page.md','w')as f:
        f.write(pagestring)
    with open('bib.bib','w')as f:
        f.write(bibtex)
    if 'jencova' in ''.join(normalize_lower(page.authors)):
        mypath='myown' 
    else:
        mypath='notmyown'
    cmypath=f'{GREEN}myown{RESET}'if mypath == 'myown' else f'{YELLOW}notmyown{RESET}'
    print(f'page {name} should go to {cmypath}')
    writein=True
    os.chdir('..')
    if writein:
        print(f'{MAGENTA}Writing in {cmypath}/{CYAN}page.md{RESET}')
        print('__________________________________________________')
        os.chdir(os.path.expanduser('~')+'/work/awiki/pages/'+mypath)
        if mypath=='myown':
            mylinkstr=f'1. [{name}]({name})'
            lines=readlines('page.md')
            if f'### {page.year}' not in lines:
                lines.append(f'### {page.year}')
                lines.append(mylinkstr)
            else:
                if f'### {page.year-1}' not in lines:
                    lines.append(mylinkstr)
                else:
                    lines.insert(lines.index(f'### {page.year-1}')-1,mylinkstr)

            writelines('page.md',lines) 
            if '-v' in sys.argv:
                with open('page.md')as f:
                    print(f.read())
        else:
            mylinkstr=f'[{name}]({name}),\n'

            with open('page.md','r')as f:
                lines=list(f.readlines())
            alphabetindex=lines.index(f'### {name[0].upper()}\n')+1
            lines.insert(alphabetindex,mylinkstr)
            with open('page.md','w')as f:
                f.writelines(lines)
            if '-v' in sys.argv:
                print(*lines)
        print(f'{GREEN}Done{RESET}')
        os.chdir(base)
        return {'status':'OK','response':{'message':'OK'}}
   
