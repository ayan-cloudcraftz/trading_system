from lib.globals.constants import *
from lib.utils.service import get


def contractInfo(conId:str, secType:str, month:str, strike:int, right:str):
    conId = "conid=" + conId
    secType = "secType=" + secType
    month = "month=" + month
    # exchange = "exchange=" + exchange
    strike = "strike=" + str(strike)
    right = "right=" + right

    params = "&".join([conId, secType, month, strike, right])
    request_url = "".join([BASE_URL + CON_DETAILS, "?", params])

    # print(request_url)

    # contract_req = requests.get(url=request_url, verify=False)

    # contract_json = json.dumps(contract_req.json(), indent=2)STK

    contract = get(url=request_url)
    return contract

    # print(contract)

def contractInfoFUT(conId:str, secType:str, month:str):
    conId = "conid=" + conId
    secType = "secType=" + secType
    month = "month=" + month
    exchange = "exchange=" + "SMART"
    # strike = "strike=" + str(strike)
    # right = "right=" + right

    params = "&".join([conId, secType, month, exchange])
    request_url = "".join([BASE_URL + CON_DETAILS, "?", params])

    # print(request_url)

    # contract_req = requests.get(url=request_url, verify=False)

    # contract_json = json.dumps(contract_req.json(), indent=2)STK

    contract = get(url=request_url)
    return contract

# contractInfo("208813719", "STK", "SMART")