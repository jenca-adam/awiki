from .notraised import notraised
def haskey(item,key):
    if hasattr(item,'__contains__'):
        return key in item
    elif hasattr(item,'__getitem__'):
        
        return notraised(lambda:item[key],LookupError)
    raise TypeError('invalid type for haskey')
