from pagetools.utils.name import maketitle,makename
from pagetools.utils.warn import warn
def bibmake(dc,name=None,tp='article'):
    print("bibmake")
    if name is None:
        if 'name' in dc:
            name=dc['name']
        else:
            name=''
            warn(
                'Missing name, will be set to \'\''
            )
    try:
        title=makename(dc['authors'],dc['year'],maketitle(name))
    except:
        title=name
    bib_export=f'@{tp}{{{title},\n'
    if 'name' in dc:
        del dc['name']
    for key in dc:
        bib_export+=f'\t{key}={{{dc[key]}}},\n'
    bib_export+='}'
    return bib_export,name
    
