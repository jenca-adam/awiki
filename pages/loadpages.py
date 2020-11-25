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
YELLOW=colorama.Fore.LIGHTYELLOW_EX
MAGENTA=colorama.Fore.MAGENTA
dateline_pattern=r'\D*\d+(\D+)(\d+)'
title_pattern=r'<h1 class="title mathjax"><span class="descriptor">Title\:</span>(\D*)<'
authors_pattern=r'Authors:(\D*)'
linkstr_pattern=r'^https?://arxiv.org/abs/\D*/?(\d+.\d+)$'
h=httplib2.Http('.cache')
base='/home/anna/work/awiki/pages'
os.chdir(base)
diacritic_dict={
    'á':'a',
    "ä":"a",
    "é":"e",
    "ě":"e",
    "í":"i",
    "ó":"o",
    "ô":"o",
    "ú":"u",
    "ü":"u",
    "ľ":"l",
    "ĺ":"l",
    "ŕ":"r",
    "ř":"r",
    "ñ":"n",
    "ň":"n",
    "ů":"u",
    "ö":"o",
    "ë":"e",
    "û":"u",
    "č":"c",
    "ť":"t",
    "ď":"d",
    "ž":"z",
    "ý":"y",
    "ï":"i",
}
for link in sys.argv[1:]:
    if link in ['--force','--new','--test','-v']:
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
    authorname=''.join([diacritic_dict[char] if char in diacritic_dict else char for char in authorname ])
    yearname=data['date'][1]
    thingname=data['title'].split(' ')[0].lower().replace(',','')
    word=1
    while len(thingname)<7:
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
            print(f'{RED}dir {name} already exists.Skipping.{RESET}')
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
    with open('bib.bib','w')as f:
        f.write('@article{'+name+',\n}')
    if 'Anna Jenčová' in data['authors'] or 'Anna Jencova' in data['authors']:
        mypath='myown'
    else:
        mypath='notmyown'
    cmypath=f'{GREEN}myown{RESET}'if mypath == 'myown' else f'{YELLOW}notmyown{RESET}'
    print(f'page {name} should go to {cmypath}')
    writein=True
    if '--test'in sys.argv:
        if input(f'Remove {name}?(y/n)')=='y':
            os.chdir(base)
            shutil.rmtree(name)
            writein=False
    os.chdir(base)
    if writein:
        print(f'{MAGENTA}Writing in {cmypath}/{CYAN}page.md{RESET}')
        print('__________________________________________________')
        os.chdir(mypath)
        if mypath=='myown':
            with open('page.md','a')as f:
                mylinkstr=f'1. [{name}]({name})\n'

                f.write(mylinkstr)
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

    
   
