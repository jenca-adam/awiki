from httplib2 import Http
from bs4 import BeautifulSoup as bs
h=Http()
def search(query,fields='all'):
    resp,content=h.request(f'https://arxiv.org/search?query={query}&searchtype={fields}')
    soup=bs(content,'html.parser')
    results=soup.find_all('li',class_='arxiv-result')
    detail_results=[[res.find('p', class_='title is-5 mathjax').text,res.find('p',class_='authors').text]for res in results]
    return detail_results
