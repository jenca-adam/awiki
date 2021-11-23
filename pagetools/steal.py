from selenium.webdriver import Firefox, FirefoxOptions
import time
import os
def steal_bib(arxivid,name):
    opt=FirefoxOptions()
    opt.headless=True
    ffx=Firefox(options=opt)
    os.remove('geckodriver.log')
    ffx.get(f'https://arxiv.org/abs/{arxivid}')
    ffxf=ffx.find_element_by_css_selector
    schc=ffxf('.cite-google-scholar')
    ffx.get(schc.get_attribute('href'))
    time.sleep(1.5)
    citesvg=ffxf('.gs_or_cit')
    citesvg.click()
    time.sleep(1)
    bibtexlink=ffxf('a.gs_citi:nth-child(1)')
    bibtexlink.click()
    ffx.switch_to.window(ffx.window_handles[-1])
    bib_cite=ffxf('pre').text
    return(bib_cite)
