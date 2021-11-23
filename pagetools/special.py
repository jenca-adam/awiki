import os
import httplib2
def home():
    os.chdir(os.path.join(os.path.expanduser('~'),'work/awiki'))
def CachedH():
    return httplib2.Http(os.path.join(os.path.expanduser('~'),'work/awiki','.cache'))
