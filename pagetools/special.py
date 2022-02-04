import os
import httplib2
httplib2.debuglevel=1
aw='awiki.adam' if 'awiki.adam' in os.getcwd() else 'awiki'
def listrm(l,item):
    try:
        l.remove(item)
    except:pass
    return l
def pagepath(p):
    return os.path.join(os.path.expanduser('~'),f'work/{aw}/pages',p)
def home():
    os.chdir(os.path.join(os.path.expanduser('~'),f'work/{aw}'))
def CachedH():
    return httplib2.Http(os.path.join(os.path.expanduser('~'),f'work/{aw}','.cache'))
def empty(page):
    pp=pagepath(page)
    if os.path.isdir(pp):
        return not bool(listrm(os.listdir(pp),'geckodriver.log'))
    else:
        return not open(pp,'rb').read()
