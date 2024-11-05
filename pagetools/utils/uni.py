import importlib
if importlib.util.find_spec('unidecode')is None:
    decode=lambda s:importlib.import_module('unicodedata').normalize('NFKD',s).encode('ascii','ignore').decode('ascii')
else:
    decode=lambda s:importlib.import_module('unidecode').unidecode(s)
    
