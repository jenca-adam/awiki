class BibEntry:
    def __init__(self,entry):
        print(entry)
        self.__dict__.update(entry)
    def __repr__(self):
        return f'BibEntry({self.ID})'
class BibFile:
    def __init__(self,entries,name='<unknown>'):
        self.entries=[BibEntry(entry) for entry in entries]
        self.name=name
    def __getitem__(self,i):
        return self.entries[i]
    def __getattr__(self,a):
        try:
            return getattr(self.entries[0],a)
        except (IndexError,AttributeError):
            raise AttributeError from None
    def __repr__(self):
        return f'<BibFile from {self.name}>'
