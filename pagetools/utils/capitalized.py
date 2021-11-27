from .apply import apply
def serious_capitalize(x):
    return ' '.join(i.capitalize() for i in x.split(' '))
def capitalized(s):
    return apply(serious_capitalize,s)

