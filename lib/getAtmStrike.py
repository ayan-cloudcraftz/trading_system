import sys

def getAtmStrike(spot:str, strikes):
    diff = sys.float_info.max
    curr_strike = None
    for strike in strikes:
        # print(contract.strike)
        if (abs(float(strike) - float(spot)) < diff):
            curr_strike = float(strike)
            diff = abs(float(strike) - float(spot))
    
    return curr_strike