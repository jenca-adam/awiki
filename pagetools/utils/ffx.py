import requests
import random
def fxget(url):
    return requests.get(url,headers={'user-agent':f'AWIKI/{random.randrange(18290)}'}).text

