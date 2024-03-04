from lib.globals.constants import *
from lib.utils.service import get

def optionStrike(conId:str, secType:str, month:str):
    conId = "conid=" + str(conId)
    secType = "secType=" + secType
    month = "month=" + month
    # exchange = "exchange=" + "SMART"

    params = "&".join([conId, secType, month])
    request_url = "".join([BASE_URL + CON_STRIKE, "?", params])

    # print(request_url)

    strikes = get(url=request_url)
    # strikes = get(url=MOCK_CON_STRIKE)
    # print(strikes)
    return strikes

    # print(strikes)

# optionStrike(conId="265598", secType="OPT", month="MAR24", exchange="SMART")

