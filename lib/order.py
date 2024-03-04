from lib.utils.service import *
from lib.globals.constants import *
from ib_insync import *

def placeOrderREST(conId:int, orderType:str, side:str, tif:str, quantity:int):
    body = {
        "orders":[{
            "conid": conId,
            "orderType": orderType,
            "side": side,
            "tif": tif,
            "quantity": quantity
        }]
    }

    # order_res = post(url=BASE_URL+ODR_PLACE, body=body)
    order_res = get(url=MOCK_ODR_PLACE)

    return order_res


def placeOrderTWS(ib, action, contract, quantity):
    ord = MarketOrder(action=action, totalQuantity=quantity)
    trade = ib.placeOrder(contract, ord)
    ib.sleep(1)
    # print(trade)
    return trade
