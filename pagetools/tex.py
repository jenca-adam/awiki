import httplib2
import special
import os
import json
from bs4 import BeautifulSoup as bs
def pair(id,page):
    url=f'https://overleaf.com/read/{id}/'
    h=httplib2.Http()
    r,c=h.request(url)
    print(json.dumps(r))
    special.home()
    os.chdir('pages/'+page)
    with open('zip.zip','wb')as f:
        f.write(c)
    os.system('unzip zip.zip')

