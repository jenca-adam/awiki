from httplib2 import Http
import re
import urllib.parse
from .special import CachedH
from .xml import element as xml
h=CachedH()
pattern=r'/abs/(.*?)$'
def search(query,fields='all'):
    resp,raw=h.request(f'http://export.arxiv.org/api/query?search_query={fields}:'+urllib.parse.quote(query)+'&start=0&max_results=500')
    parsed=xml.parse(raw)
    entries=parsed['entry']
    #print(entries[0].id)
    
    detail_results=[[entry.title.text,','.join([a.find_child('name').text for a in entry['author']]),entry.id.text.split('/abs/')[1]] for entry in entries]
    return detail_results
