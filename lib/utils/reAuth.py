import requests
from lib.globals.constants import *

def reAuthenticate():
    response = requests.get(url=BASE_URL+RE_AUTH, verify=False)
    print(response)
    print(response.text)