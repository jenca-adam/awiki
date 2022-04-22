import requests
import random
def fxget(url):
    print('Requesting '+url)
    return requests.get(url,headers={'user-agent':f'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:99.0) Gecko/20100101 Firefox/99.0'}).text

