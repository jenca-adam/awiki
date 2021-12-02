import shutil
import os
from . import special
def rm(name):
    base=os.getcwd()
    special.home()
    os.chdir('pages/myown')
    with open('page.md')as f:
        lines=list(f.readlines())
        for line in lines:
            if f'[{name}]({name})' in line:
                lines.remove(line)
                myown=True
                break
        else:
            myown=False
    print(myown)
    os.chdir('..')
    print(os.getcwd())
    try:

        shutil.rmtree(name)
    except:pass
    if myown:
        os.chdir('myown')
        with open('page.md','w')as f:
            f.writelines(lines)
    else:
        os.chdir('notmyown')
        with open('page.md')as f:
            cont=f.read()
        cont=cont.replace(f'[{name}]({name}),' ,'')
        with open('page.md','w')as f:
            f.write(cont)
    os.chdir(base)
            
