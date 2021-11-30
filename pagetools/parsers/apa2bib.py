from .bib_export import bibmake
from .apa.parser import APAParser
from .apa.authorjoin import join
from pagetools.utils.name import rev
def apa2bib(apa_string):
    apadict=APAParser(apa_string).parsed
    apadict['authors']=rev(apadict['authors'][0])  
    return bibmake(apadict)
