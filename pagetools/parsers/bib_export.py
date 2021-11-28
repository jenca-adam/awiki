from pagetools.utils.name import maketitle,makename
def bibmake(dc,tp='article'):
    title=makename(maketitle(dc['authors']),dc['year'],dc['name'])
    bib_export=f'@{tp}{{{title},\n'
    del dc['name']
    for key in dc:
        bib_export+=f'\t{key}={{{dc[key]}}},\n'
    bib_export+='}'
    return bib_export
    
