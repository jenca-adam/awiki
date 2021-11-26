from selenium.webdriver import Firefox, FirefoxOptions
import time
import os
from bs4 import BeautifulSoup as bs
import requests
def old_steal_bib(arxivid):
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
def steal_bib(arxivid):#the new one(semantic scholar)
    print(arxivid)
    url=f'https://api.semanticscholar.org/arXiv:{arxivid}'
    dwdd=requests.get(url).text
    soup=bs(dwdd,'html.parser')
    tarelem=soup.find('pre',class_='bibtex-citation')
    return tarelem.text

