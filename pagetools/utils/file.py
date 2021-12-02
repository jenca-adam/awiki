import io
def file(fp,*args,**kwargs):
    if isinstance(fp,str):
        try:
            return open(fp,*args,**kwargs)
        except FileNotFoundError:
            return io.StringIO(fp)
    elif isinstance(fp,bytes):
        return io.BytesIO(fp)
    else:
        return fp
def readlines(fp):
    with file(fp) as f:
        x=[i[:-1] for i in f.readlines()]
    return x
def writelines(fp,l):
    with file(fp,'w')as f:
        for i in l:
            f.write(i+'\n')
    return i
