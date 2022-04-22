from .uni import decode
from .strfilt import lowercase
from .alphfilt import alphnum
def rev(name):
    return ' '.join(reversed(name.split(' ')))
def makename(authorname,year,artname):
    print(f'making name from {authorname},{year}, {artname}')
    pn=decode(authorname.split(' ')[-1].lower())
    cc=alphnum(lowercase(f'{pn}{year}{maketitle(artname)}'))
    print(cc)
    return cc
def maketitle(artname,maxchar=12):
    artname=artname.replace(',','').lower()
    words=artname.split(' ')
    t=''
    for word in words:
        t+=word

        if len(word)+len(t)>maxchar:
            break
    return t
        
