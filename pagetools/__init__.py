from . import loadpage,remove,search,steal,special
def add(id):
    print(id)
    try:
        return loadpage.loadpage(id)
    except Exception as e:
        special.home()
        return {'status':'error','response':{'message':str(e),'type':e.__name__}}
def rm(name):
    remove.rm(name)
def search_arxiv(query,fields='all'):
    return search.search(query,fields)
def steal_bib(arxivid,name):
    return steal.steal_bib(arxivid,name)
