import xml.etree.ElementTree as etree

class XMLElement:
    def __init__(self,orig):
        self._original=orig
        self.children=[XMLElement(e) for e in list(orig)]
        self.name=orig.tag.split('}')[1]
        self.text=etree.tostring(self._original,encoding='utf8',method='text').decode()
        self.raw=etree.tostring(self._original).decode()
    def find_child(self,kid):
        for  k in self.children:
            if k.name==kid:
                return k
            n=k.find_child(kid)
            if n:
                return n
        return None
    def find_children(self,kid):
        found=[]
        for k in self.children:
            if k.name==kid:
                found.append(k)
            n=k.find_children(kid)
            found.extend(n)
        return found
    def __getitem__(self,kid):
        return self.find_children(kid)
    def __getattr__(self,kid):
        return self.find_child(kid)
    def __iter__(self):
        return iter(self.children)
def parse(text):
    return XMLElement(etree.fromstring(text.strip()))
