from lib.ibkr import IBKR
import json
from datetime import datetime
import re
from lib.utils.reAuth import reAuthenticate


def test():
    ibkr = IBKR()
    # print(ibkr.__dict__)
    # ibkr.connect()
    print(ibkr.getPortfolioSummary())
    # ibkr.getPortfolioDeltaTWS()

    # ibkr.executeHedgeTemp(1)

    # ibkr.getPortfolioDeltaTWS()

    # print(ibkr.getPortfolioDelta())
    # pf = ibkr.getPortfolioDelta()
    # print(pf)
    # reAuthenticate()

    # data = ibkr.getMarketData()
    # print(data) 
    # print(data[1][0]["symbol"])
    # Define a regular expression pattern to match the date
    # date_pattern = r"[A-Z]{3}\s+\d{1,2}\s+'\d{2}"

    # # Find the date in the input string
    # match = re.search(date_pattern, data[4])

    # if match:
    #     # Extract the matched date
    #     input_date = match.group(0)

    #     # Parse the input date
    #     date_object = datetime.strptime(input_date, "%b %d '%y")

    #     # Convert to YYYYMMDD format
    #     formatted_date = date_object.strftime("%Y%m%d")

    #     print(formatted_date)
    # else:
    #     print("Date not found in the input string.")

    # order = ibkr.executeTrade(symbol=data[2], secType=data[3], expiry=formatted_date, 
    #                           callStrike=data[0], putStrike=data[1], minLotSize=15, treadeType="S")

    # order = ibkr.executeTrade(conId=data[1][0]["conid"], orderType="MKT", side="DAY",
    #                           tif="tif", quantity=10)

    # order = ibkr.executeTrade(action='BUY', contract=data, quantity=5)
    # print(order)

    # ibkr.connect()

    # res = ibkr.executeTrade("",1,"","","", "")
    # print(res)


test()