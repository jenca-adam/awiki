from .bib_export import bibmake
from .apa.parser import APAParser
from .apa.authorjoin import join

def apa2bib(apa_string):
    apadict=APAParser(apa_string).parsed
    apadict['authors'].reverse()
    apadict['authors']=join(apadict['authors'])
    return bibmake(apadict)
