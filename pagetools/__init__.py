from . import loadpage,remove,search,steal,special
import os
import shutil
def add(id):
    special.home()
    old=set(os.listdir('pages'))
    print(id)
    clup=[]
    try:
        return loadpage.loadpage(id)
    except Exception as e:
        special.home()
        print('Cleaning up...')
        clup=os.listdir('pages')
        x=[]
        for i in clup:
            if special.empty(i):
                x.append(i)
                shutil.rmtree(special.pagepath(i))
                print(f'Cleaned up {i}')
            else:
                #print(f'{i} is not empty')
                clup.remove(i)
        if not clup:
            print('nothing to clean up...')
        return {'status':'error','response':{'message':str(e),'type':e.__class__.__name__},'cleanup':x}
def rm(name):
    remove.rm(name)
def search_arxiv(query,fields='all'):
    return search.search(query,fields)
def steal_bib(arxivid,name):
    return steal.steal_bib(arxivid,name)
