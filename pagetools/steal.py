from bs4 import BeautifulSoup as bs
import httplib2
h=httplib2.Http()
def steal_bib(arxivid,name):
    resp,cont=h.request(f'https://api.semanticscholar.org/arXiv:{arxivid}')

    semantic_soup=bs(cont,'html.parser')
    try:
        bib_cite=semantic_soup.find('pre').text
    except AttributeError:
        bib_cite='@article{'+name+','+'\n'+'}'
    return(bib_cite)
