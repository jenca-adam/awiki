import string

def lowercase(s):
    return ''.join(list(filter(lambda x:x in string.ascii_lowercase+string.digits,s)))
