import re
from pagetools.utils.warn import warn
from pagetools.utils.uni import decode
from pagetools.parsers.bib_export import bibmake
jref_pattern=re.compile(r'(?P<authors>(\D+\s\D+)+,?\s)-\s(?P<journal>.*),\s(?P<year>(19|20)\d\d)\s-\s(?P<publisher>.*)$')
def jref_parse(jref):
    return jref_pattern.search(decode(jref)).group_dict()

def  jref2bib(jref,name=None):
    try:
        parsed=jref_parse(jref)
    except AttributeError:
        warn(
           'jref does not match pattern'
                )
        return bibmake({},name)
    return bibmake(parsed,name)
