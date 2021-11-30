from .apply import apply
from .uni import decode
def serious_capitalize(x):
    return ' '.join(i.capitalize() for i in x.split(' '))
def capitalized(s):
    return apply(serious_capitalize,s)
def normalize_lower(query):
    return apply(lambda x:decode(x).lower(),query)
