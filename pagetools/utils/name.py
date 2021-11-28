import unidecode

def makename(authorname,year,artname):
    pn=unidecode.unidecode(authorname.split(' ')[-1].lower())
    return f'{pn}{year}{maketitle(artname)}'
def maketitle(artname,maxchar=12):
    artname=artname.replace(',','').lower()
    words=artname.split(' ')
    t=''
    for word in words:
        if len(word)+len(t)>maxchar:
            break
        t+=word
    return t
        
