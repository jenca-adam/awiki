import requests
import random
def fxget(url):
    return requests.get(url,headers={'user-agent':f'Mozilla/5.0 (X11; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0'}).text
