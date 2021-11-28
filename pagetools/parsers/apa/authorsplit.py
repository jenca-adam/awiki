from pagetools.utils.ellipsis import ellipsize
def split(authorstring):
    authorstring=ellipsize(authorstring.replace('&',''))
    splitted=[]
    splitted_cache=[]
    for ix,item in enumerate(authorstring.split(',')):
        if ix%2==1:
            splitted.append(splitted_cache[ix-1]+', '+item.strip())
        splitted_cache.append(item.strip())
    return splitted
        
    
