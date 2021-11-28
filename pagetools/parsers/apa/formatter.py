class APAFormatter():
    @classmethod
    def format(self,authors,year,name,journal,volume=None,number=None,pages=None):
        xstring=f'{authors} ({year}). {name}. {journal}'
        if volume is not None:
            xstring=f'{xstring}, {volume}({number}), {pages}.'
        else:
            xstring+='.'
        return xstring
