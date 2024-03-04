from lib.ibkr import IBKR

def displayMenu():
    print("##########################################################################################")
    print("MENU")
    print("1. Execute Straddle")
    print("2. Execute Hedge")
    print("3. Portfolio Summary")
    print("4. Exit")
    print("##########################################################################################")

def main():
    ibkr = IBKR()
    # data = ibkr.getMarketData(secType="OPT", symbol="SPX")
    # print(data)
    print("Please Enter Symbol & Sec Type: ")
    symbol = input("Symbol: ")
    secType = input("Sec Type: ")

    market_data = ibkr.getMarketData(symbol=symbol, secType=secType)
    print(market_data)
    
    while True:
        displayMenu()
        choice = input("Enter your choice: ")

        if choice == "1":
            tradeType = input("Enter Trade Type (L/S): ")
            lot = input("Enter Lot Size: ")
            print(symbol)
            print(secType)
            print(market_data[5])
            print(market_data[0])
            print(market_data[1])
            trade_res = ibkr.executeTradeTWS(symbol=symbol, secType=secType, expiry=market_data[5], 
                              callStrike=market_data[0], putStrike=market_data[1], minLotSize=lot, treadeType=tradeType)
            print(trade_res)

        elif choice == "2":
            lot = int(input("Enter Minimum Lot Size: "))
            trade_res = ibkr.executeHedgeTWS(lot)
            print(trade_res)

        elif choice == '3':
            pf_delta = ibkr.getPortfolioSummary()
            print(pf_delta)

        elif choice == '4':
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please enter a valid option.")
    pass
    

if __name__ == "__main__":
    main()