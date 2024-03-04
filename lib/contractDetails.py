from lib.globals.constants import *
from lib.utils.service import *


def contractSearch(symbol:str, secType:str) -> dict:
    body = {"symbol":symbol, "secType":secType, "name":False}

    contract = post(url=BASE_URL+CON_SEARCH, body=body)
    # contract = get(url=MOCK_CON_SEARCH)

    # print(contract)
    return contract