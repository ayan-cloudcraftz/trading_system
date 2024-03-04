from lib.utils.makeUrl import makeUrl1
from lib.utils.service import get
from lib.globals.constants import *
from ib_insync import *

def marketSnapshotStock(conId, fields):
    conId = "conids=" + str(conId)
    fields = "fields=" + fields

    request_url = makeUrl1(paramList=[conId, fields], baseUrl=BASE_URL, endpoint=MKT_SNAP)

    # market_snap = get(url=request_url)
    market_snap = get(url=MOCK_MKT_SNAP)

    # print(market_snap)
    return market_snap

# marketSnapshot(conId="265598,8314", fields="31,55,84,86")

def marketSnapshotOption(conId, fields):
    conId = "conids=" + str(conId)
    fields = "fields=" + fields
    # month = "month=" + ""
    # right = "right=" + right
    # strike = "strike=" + strike
    

    request_url = makeUrl1(paramList=[conId, fields, ""], baseUrl=BASE_URL, endpoint=MKT_SNAP)

    # market_snap = get(url=request_url)
    market_snap = get(url=request_url)

    # print(market_snap)
    return market_snap

def marketSnapshotFuture(conId, month, fields):
    conId = "conids=" + str(conId)
    fields = "fields=" + fields
    month = "month=" + month

    request_url = makeUrl1(paramList=[conId, fields], baseUrl=BASE_URL, endpoint=MKT_SNAP)

    market_snap = get(url=request_url)
    # market_snap = get(url=MOCK_MKT_SNAP)

    print(market_snap)
    return market_snap

def getMarketSnapshotInd(conid:str, fields:str):
    conId = "conids=" + str(conid)
    fields = "fields=" + fields
    
    request_url = makeUrl1(paramList=[conId, fields, ""], baseUrl=BASE_URL, endpoint=MKT_SNAP)

    get(url=BASE_URL+PF_ACC)
    market_snap = get(url=request_url)

    # print(market_snap)
    return market_snap

def marketSnapshotTWS(ib:IB, contract:Contract):
    ib.reqMarketDataType(4)
    marketData = ib.reqMktData(contract=contract, genericTickList="", snapshot=False, 
                               regulatorySnapshot=False, mktDataOptions=[])
    # return marketData.modelGreeks.delta
    if marketData.modelGreeks:
        print(marketData.modelGreeks)
    # return marketData.modelGreeks.delta
    pass