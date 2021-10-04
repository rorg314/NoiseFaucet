

from math import floor


def BtcToSat(amount:float):
    # 100 million satoshi per btc
    return floor(amount * 100 * 1e6)

def SatToBtc(amount):   
    # 100 million satoshi per btc
    return (amount / (100 * 1e6))

def BtcStr(amount):
    return f"{amount:1.8f}"


