#from selenium.webdriver import Firefox, FirefoxOptions
#import time
#import os
#from bs4 import BeautifulSoup as bs
import requests
#from .scholar.bibex import export_bib
from pagetools.arxiv import ArXivPage
from pagetools.scholar.scholar import scholar_search
''' This file contained just wrapper for scholar.bibex.export_bib and other implementations of the same function.
Dead branch. Useful when Scholar is down, or if I find a better way to do this.'''
def steal_VERY_old_bib(arxivid):
    opt=FirefoxOptions()
    #opt.headless=True #new version incompatible with current Firefox:(
    opt.add_argument('--headless')
    print('initializing driver...')
    ffx=Firefox(options=opt)
    print('loading arxiv site...')
    ffx.get(f'https://arxiv.org/abs/{arxivid}')
    ffxf=ffx.find_element_by_css_selector
    schc=ffxf('.cite-ads')
    print('redirecting to harvard adsabs')
    ffx.get(schc.get_attribute('href'))
    print('loading citations..')
    time.sleep(1.5)
    citesvg=ffxf('.gs_or_cit')
    citesvg.click()
    time.sleep(1)
    print('downloading bib')
    bibtexlink=ffxf('a.gs_citi:nth-child(1)')
    bibtexlink.click()
    
    ffx.switch_to.window(ffx.window_handles[-1])
    bib_cite=ffxf('pre').text
    del ffx

    os.remove('geckodriver.log')
    return(bib_cite)
def steal_even_older_bib(arxivid):#the less old one(semantic scholar)
    print(arxivid)
    url=f'https://api.semanticscholar.org/arXiv:{arxivid}'
    dwdd=requests.get(url).text
    soup=bs(dwdd,'html.parser')
    tarelem=soup.find('pre',class_='bibtex-citation')
    return tarelem.text
def steal_old_bib(arxivid):    
    title=ArXivPage(arxivid).title
    return export_bib(title)
def steal_bib(arxivid,**kwargs):
    if 'arxiv_id' not in kwargs:
        kwargs['arxiv_id']=arxivid #TODO???
    results,uri=scholar_search(**kwargs)
    result=results[0]
    
    return result.get_citations().bibtex,result.link,uri
    

