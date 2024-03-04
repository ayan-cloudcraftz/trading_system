from lib.utils import calculate
from lib.marketSnapshot import marketSnapshotTWS
from lib.utils.service import *
from lib.globals.constants import *

def getPortfolioGreek(ib):
    portfolio = ib.reqPositions()
    portfolioDelta = 0

    for trade in portfolio:
        # print(trade.contract.lastTradeDateOrContractMonth)
        className = str(type(trade.contract))
        
        #?OPTION
        if (className == "<class 'ib_insync.contract.Option'>"):
            q_con = ib.qualifyContracts(trade.contract)[0]
            pf_greek = marketSnapshotTWS(ib=ib, contract=q_con)
            # portfolioDelta += calculate(pf_greek.DELTA, position=trade.position)
            # print("here")
            # return

        #?FUTURE
        elif (className == "<class 'ib_insync.contract.Future'>"):
            portfolioDelta += trade.position

        #?STOCK
        elif (className == "<class 'ib_insync.contract.Stock'>"):
            portfolioDelta += trade.position

    print(f"PORTFOLIO DELTA: {portfolioDelta}")

    return portfolioDelta

def getPortfolioSummary():
    pf = get(url=BASE_URL+PF_ACC)
    # print(pf)
    data = get(url=BASE_URL+PF_SUMM)
    # print(data)