#!/usr/bin/env python3
import httplib2
from bs4 import BeautifulSoup
import sys
import re
import colorama
import os
import shutil
BLUE=colorama.Fore.BLUE
RESET=colorama.Style.RESET_ALL
BOLD = '\033[1m'
RED=colorama.Fore.RED
GREEN=colorama.Fore.GREEN
CYAN=colorama.Fore.CYAN
YELLOW=colorama.Fore.YELLOW
dateline_pattern=r'\D*\d+(\D+)(\d+)'
title_pattern=r'<h1 class="title mathjax"><span class="descriptor">Title\:</span>(\D*)<'
authors_pattern=r'Authors:(\D*)'
linkstr_pattern=r'^https?://arxiv.org/abs/(\d+.\d+)$'
h=httplib2.Http('.cache')
base=os.getcwd()
for link in sys.argv[1:]:
    if link in ['--force','--new','--test']:
        continue
    data={}
    print(f'requesting {link}...',file=sys.__stdout__)
    response,content=h.request(link)
    print(f'parsing {link}...',file=sys.__stdout__)
    soup=BeautifulSoup(content,'html.parser')
    print('loading date...',file=sys.__stdout__)
    dateline=str(soup.find_all('div',class_='dateline')[0].text)
    match=re.search(dateline_pattern,dateline)
    dategroups=match.groups()
    month=dategroups[0]
    year=dategroups[1]
    data['date']=month,year
    print('loading title...',file=sys.__stdout__)
    title=str(soup.find_all('h1',class_='title mathjax')[0])

    match=re.search(title_pattern,title)
    raw_title=match.groups()[0]
    data['title']=raw_title
    print('loading authors...',file=sys.__stdout__)
    authors=str(soup.find_all('div',class_='authors')[0].text)
    match=re.search(authors_pattern,authors)
    authors=match.groups()[0].split(',')
    data['authors']=authors
    print('loading journal refs...',file=sys.__stdout__)
    jrefs=soup.find('td',class_='tablecell jref')
    if not jrefs:
        print(f'WARNING:\n{RED}No journal refs!{RESET}')
        data['jrefs']=''
    else:
        jrefs=jrefs.text
        data['jrefs']=str(jrefs)
    print(f'{BOLD}Start of informative output{RESET}')
    print(f'{BLUE}')
    i=0
    for chunk in data.values():
        if isinstance(chunk,list):
            print(f'{GREEN}')
            print(*chunk,sep='\n')
            print(f'{BLUE}')
        elif isinstance(chunk,tuple):
            print(f'{CYAN}')
            print(*chunk)
            print(f'{BLUE}')
        elif chunk:
            print(chunk)
        else:
            print(f'{RED}Data for {list(data.keys())[i]} not found{BLUE}')
        i+=1
    print(f'{RESET}')
    print(f'{BOLD}End of informative output{RESET}')
    print('__________________________________________________')
    print(f'{GREEN}Writing page.md{RESET}')
    authorname=data['authors'][0].split(' ')[1].lower()
    yearname=data['date'][1]
    thingname=data['title'].split(' ')[0].lower().replace(',','')
    word=1
    while len(thingname)<5:
        thingname+=data['title'].split(' ')[word].lower().replace(',','')
        word+=1
    name=''.join([authorname,yearname,thingname])
    print(f'{YELLOW}Directory name:{name}{RESET}')
    try:
        os.mkdir(name)
        os.chdir(name)
    except FileExistsError:
        if '--force' in sys.argv:
            os.chdir(name)
        elif '--new' in sys.argv:
            continue
        else:
            def fun():
                get=input(f'directory {name} already exists. auto-rewrite?(y/n)')
                
                if get == 'n':return 'continue'
                elif get == 'y':
                    os.chdir(name)
                    return
                else:
                    print('invalid option')
                    fun()
            a=fun()
            if a=='continue':
                continue
    linkmatch=re.search(linkstr_pattern,link)
    linkid=linkmatch.groups()[0]
    print(linkid)
    linkstr=f'[arxiv:{linkid}]({link})'
    pagestring=f'title: {name}\n---\n\n\n## Reference\n\n\t{(", ").join(data["authors"])}; {data["title"]};{data["jrefs"]}; {" ".join(data["date"])}\n\n\n{linkstr}'
    print(f'{name}/page.md:\n\n{CYAN}{pagestring}{RESET}')
    print(os.getcwd())
    with open('page.md','w')as f:
        f.write(pagestring)
    if '--test'in sys.argv:
        if input(f'Remove {name}?(y/n)')=='y':
            os.chdir(base)
            shutil.rmtree(name)
            print(f'{GREEN}Done{RESET}')

    
   
