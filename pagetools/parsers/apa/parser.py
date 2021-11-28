import parse
from . import authorsplit as aspl
class APAParser:
    def __init__(self,string):
        print(string)
        self.string=string
        self.parsed=parse.parse('{authors} ({year}). {name}. {journal}, {volume}({number}),{pages}.',string)         
        if self.parsed is None or True:
            self.parsed=parse.parse('{authors} ({year}). {name}. {journal}.',string)
        self.__dict__.update(self.parsed.named)
        self.parsed=self.parsed.named
        self.parsed['authors']=aspl.split(self.parsed['authors'])
        self.authors=aspl.split(self.authors)
