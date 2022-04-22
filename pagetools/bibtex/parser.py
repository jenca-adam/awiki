from pybtex.database.input import bibtex
from .bibfile import *
from ..utils.strfilt import lowercase
def getdb(bib):
    parser=bibtex.Parser()
    pf=parser.parse_string(bib)
    return pf
def parse(bib):
    db=getdb(bib)
    return BibEntry(list(db.lower().entries.values())[0].fields)
def get_name(bib):
    return lowercase(bib.splitlines()[0].split('{')[-1].strip())
