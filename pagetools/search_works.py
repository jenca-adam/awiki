import re,os

def search(q):
    results=[]
    os.chdir(os.path.expanduser('~')+'/work/awiki/pages/')
    for work in os.listdir():
        if work in ['myown','notmyown','index']:continue
        try:
            os.chdir(work)
        except NotADirectoryError:
            continue
        
        try:
            with open('page.md')as f:
                m=f.read() 
                if re.search(q,m):
                    results.append((work,'/view/'+work,'/edit/'+work))
                elif re.search(q.lower(),m):
                
                    results.append((work,'/view/'+work,'/edit/'+work))
                elif re.search(q.capitalize(),m):
                    results.append((work,'/view/'+work,'/edit/'+work))
                elif re.search(q.lower().capitalize(),m):
                    results.append((work,'/view/'+work,'/edit/'+work))
                elif re.search(q.upper(),m):
                    results.append((work,'/view/'+work,'/edit/'+work))
        except IOError:
            pass
        os.chdir('..')
    os.chdir(os.path.expanduser('~')+'/work/awiki/')

    return results
                    
