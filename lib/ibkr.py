from lib.contractDetails import contractSearch
# from lib.contractInfo import contractInfo
from lib.marketSnapshot import *
from lib.optionStrike import optionStrike
from lib.order import placeOrderTWS
from lib.getAtmStrike import getAtmStrike
from lib.portfolioDelta import getPortfolioSummary
from ib_insync import *
from lib.contractInfo import *


class IBKR:

    def __init__(self) -> None:
        self.ib = IB()
        ackw = self.ib.connect('127.0.0.1', 7497,  clientId=1000)
        print(ackw)
        pass

    # def __del__(self):
        # print("disconnected")
        # self.ib.disconnect()

    def connect(self) -> None:
        self.ib = IB()
        ackw = self.ib.connect('127.0.0.1', 7497,  clientId=1000)
        print(ackw)
    
    def getMarketData(self, secType:str, symbol:str) -> list:
        print(secType, symbol)
        contract_data = contractSearch(symbol=symbol, secType=secType)
        # return contract_data
        # print(contract_data)

        expiry = contract_data[0]['opt'].split(";")[0]
        # print(expiry)
        # print(contract_data[0]["conid"])
        # print(contract_data[0]["sections"][0]["exchange"])
        month = contract_data[0]["sections"][1]["months"].split(";")[0]
        conId = contract_data[0]["conid"]
        print(conId)
        print(month)

        if (secType == "STK"):
            marketData = marketSnapshotStock(conId=conId, fields="7295,7296,70,71,7308,7309")
            return [marketData, contract_data]
        
        elif (secType == "OPT"):
            strikes = optionStrike(conId=conId, secType=secType, month=month)

            # return strikes
            
            # return strikes
            marketData = []
            # print(strikes)
            # print(strikes["call"])

            # for strike in strikes["call"]:
            # print(strikes["call"][0])
            contract_info = contractInfo(conId=conId, secType=secType, month=month, strike=strikes["call"][0], right="C")
            # print(contract_info)
            # return contract_info
            print(contract_info[0]["conid"])
            expiry_detail = contract_info[0]["desc2"]

            strike_conid = contract_info[0]["conid"]
            
            try:
                marketSnapshotOption(conId=strike_conid, fields="70,71,73,31,7308")
                market_snapshot = marketSnapshotOption(conId=strike_conid, fields="70,71,73,31,7308")
            # print(spot_price[0]["73"])
            except:
                spot_price = 0
            print(market_snapshot)
            # print(spot_price[0]["31"])
            spot_price = market_snapshot[0]["31"]

            if (spot_price[0] == "C" or spot_price[0] == "H"):
                spot_price = spot_price[1 : len(spot_price)]
                print(spot_price)

            atm_strike_call = getAtmStrike(spot=spot_price, strikes=strikes["call"])
            atm_strike_put = getAtmStrike(spot=spot_price, strikes=strikes["put"])

            return [atm_strike_call, atm_strike_put, symbol, secType, expiry_detail, expiry]
            
            
            # for strike in strikes['call'][0]:
            #     marketData.append(marketSnapshotOption(conId=contract_data[0]["conid"], 
            #                                       strike=strike, month=contract_data[0]["sections"][0]["months"],
            #                                        right="C", fields="7295,7296,70,71,7308,7309"))
                
            # for strike in strikes['put'][0]:
            #     marketData.append(marketSnapshotOption(conId=contract_data[0]["conid"], 
            #                                       strike=strike, month=contract_data[0]["sections"][0]["months"],
            #                                        right="P", fields="7295,7296,70,71,7308,7309"))
            
            # marketData.append(contract_data)
            return marketData

        elif (secType == "FUT"):
            print(expiry)
            data = contractInfoFUT(conId=conId, secType=secType, month=expiry)
            # marketData = marketSnapshotFuture(conId=conId, 
            #                                   month=expiry, 
            #                                   fields="7295,7296,70,71,7308,7309")
            # return [marketData, contract_data]
            return data
            pass

        else:
            print(secType)
            return None

    def executeTradeTWS(self, symbol:str, secType:str, expiry:str, 
                     callStrike:str, putStrike:str, minLotSize:int, treadeType:str):

        if (treadeType == "L"):
            action = "BUY"
        else:
            action = "SELL"

        contract = Contract(secType=secType, symbol=symbol, lastTradeDateOrContractMonth=expiry,
                            strike=float(callStrike), right="C", multiplier="100", exchange="SMART")
        q_contract = self.ib.qualifyContracts(contract)[0]
        print(q_contract)
        order_res_call = placeOrderTWS(ib=self.ib, action=action, contract=q_contract, quantity=minLotSize)

        contract = Contract(secType=secType, symbol=symbol, lastTradeDateOrContractMonth=expiry,
                            strike=float(putStrike), right="P", multiplier="100", exchange="SMART")
        q_contract = self.ib.qualifyContracts(contract)[0]
        order_res_put = placeOrderTWS(ib=self.ib, action=action, contract=q_contract, quantity=minLotSize)

        return [order_res_call, order_res_put]
    
    def executeTradeREST():
        pass
    
    def executeHedgeREST(self, data, lot):
        pf_delta = self.getPortfolioDelta()
        actual_pf_delta = pf_delta * (-1)

        if (actual_pf_delta < 0):
            if (lot / abs(actual_pf_delta) < 1):
                #execute trade BUY
                contract = Contract(secType="FUT", symbol=data.symbol, lastTradeDateOrContractMonth=data.expiry)
                q_contract = self.ib.qualifyContracts(contract)[0]
                order_res = placeOrderTWS(ib=self.ib, action="BUY", contract=q_contract, 
                                          quantity=max(lot, int(abs(actual_pf_delta) / lot) * lot))
                return order_res
            pass
        else:
            if (lot / abs(actual_pf_delta) < 1):
                #execute trade SELL
                pass
            pass
    
    def getPortfolioDeltaREST(self):
        positions = getPortfolioSummary()
        # return data
        # return getPortfolioGreek(ib=self.ib)
        # cont = Contract(secType="OPT", symbol='BANKNIFTY', lastTradeDateOrContractMonth='20240424', strike=44000.0, right='C', exchange='NSE')
        # q_cont = self.ib.qualifyContracts(cont)[0]

        # self.ib.reqMarketDataType(4)
        
        pf_delta = 0
        for position in positions:
            delta = getMarketSnapshotInd(conId=position["conid"], fields="7308")[0]["7308"]
            pf_delta += (delta * position["position"])

        return pf_delta
        cd = Contract(secType='OPT', symbol='BANKNIFTY', lastTradeDateOrContractMonth='20240327', strike=44000.0, right='C', multiplier='1', exchange='NSE', currency='INR')
        q_cd = self.ib.qualifyContracts(cd)

        # print(q_cd)

        self.ib.reqMarketDataType(4)
        data = self.ib.reqMktData(q_cd[0], "", False, False, [])
        print(data.modelGreeks)
        self.ib.sleep(3)
        data = self.ib.reqMktData(contract=q_cd[0], genericTickList='', snapshot=False, regulatorySnapshot=False, mktDataOptions=[])
        # print(data)
        print(data.modelGreeks)

        count = 0
        # while True:
        #     data = self.ib.reqMktData(q_cd[0], "", False, False, [])
        #     print(count, data.modelGreeks)
        #     count += 1
        #     if (data.modelGreeks != None):
        #         return

        # return data

    def getPortfolioDeltaTWS(self) -> float:
        pf_positions = self.ib.reqPositions()
        pf_delta = 0
        for position in pf_positions:
            # print(position.contract)
            if (str(type(position.contract)) == "<class 'ib_insync.contract.Option'>"):
                # print(position.contract.conId)
                greeks = getMarketSnapshotInd(conid=position.contract.conId, fields="7308")
                print(greeks)
                delta = float(greeks[0]["7308"])
                pf_delta += (delta * position.position)
                pass
            else:
                pf_delta += position.position

        return pf_delta
    
    def getPortfolioSummary(self):
        pf_positions = self.ib.reqPositions()
        # stocks = []
        # options = []
        # futures = []
        data = {
            "option":None,
            "future":None,
            "stock":None
        }

        for position in pf_positions:
            # print(position.contract)
            temp = {}
            if (str(type(position.contract)) == "<class 'ib_insync.contract.Option'>"):
                # temp["secType"] = "Option"
                data["option"]["symbol"] = position.contract.symbol
                data["option"]["expiry"] = position.contract.lastTradeDateOrContractMonth
                data["option"]["strike"] = position.contract.strike

                # stocks.append(temp)
            
            elif (str(type(position.contract)) == "<class 'ib_insync.contract.Future'>"):
                # temp["secType"] = "Future"
                data["future"]["symbol"] = position.contract.symbol
                data["future"]["expiry"] = position.contract.lastTradeDateOrContractMonth

                # futures.append(temp)
            
            elif (str(type(position.contract)) == "<class 'ib_insync.contract.Stock'>"):
                # temp["secType"] = "Stock"
                data["stock"]["symbol"] = position.contract.symbol

                # stocks.append(temp)

            else:
                # temp["secType"] = str(type(position.contract))
                pass

        return data


    def refreshMarketData(self, symbol:str, secType:str):
        pass

    def executeHedgeTWS(self, lot:int):
        pf_delta = self.getPortfolioDeltaTWS()
        actual_pf_delta = pf_delta * (-1)

        print(actual_pf_delta)

        contract = Contract(secType="FUT", symbol="ES", lastTradeDateOrContractMonth="20240315", 
                            multiplier="50", exchange="CME", currency="USD")
        q_contract = self.ib.qualifyContracts(contract)[0]

        if (actual_pf_delta < 0):
            if (abs(actual_pf_delta) >= lot):
                #execute trade BUY
                order_res = placeOrderTWS(ib=self.ib, action="BUY", contract=q_contract, 
                                          quantity=int(abs(actual_pf_delta)))
                return order_res
            elif (lot / abs(actual_pf_delta) < 2):
                order_res = placeOrderTWS(ib=self.ib, action="BUY", contract=q_contract, 
                                          quantity=lot)
                return order_res
            else:
                print("Hedge not executed")
        else:
            if (abs(actual_pf_delta) >= lot):
                #execute trade SELL
                order_res = placeOrderTWS(ib=self.ib, action="SELL", contract=q_contract, 
                                          quantity=int(abs(actual_pf_delta)))
                return order_res
            elif (lot / abs(actual_pf_delta) < 2):
                order_res = placeOrderTWS(ib=self.ib, action="SELL", contract=q_contract, 
                                          quantity=lot)
                return order_res
            else:
                print("Hedge not executed")

        return