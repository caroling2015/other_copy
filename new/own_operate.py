# -*- encoding: utf-8 -*-
from conf import rate,ETP_min_fee,ETH_min_fee,BCY_min_fee,BTC_min_fee
import random

def trade_fee(quantity,limit):
    quantity = quantity / 1e8
    limit = limit / 1e8
    trade_fee = quantity*limit*rate
    return trade_fee

def order_sum(quantity,limit):
    quantity = quantity / 1e8
    limit = limit / 1e8
    sum = quantity*limit
    return sum

def order_fee(denominator,quantity,limit):
    fee = trade_fee(quantity, limit)
    if denominator == 'ETH':
        fee = fee if fee > ETH_min_fee else ETH_min_fee
    if denominator == 'BTC':
        fee = fee if fee > BTC_min_fee else BTC_min_fee
    if denominator == 'ETP':
        fee = fee if fee > ETP_min_fee else ETP_min_fee
    if denominator == 'BCY':
        fee = fee if fee > BCY_min_fee else BCY_min_fee
    return fee


def get_Data(num,trading_pair):
    random.seed(6)
    data_random = []
    if num < 1:
        print 'num must bigger than 1'
        return
    for i in range(0,num):
        limit = random.randint(5000000,6000000)
        quantity = random.randint(100000000,10000000000)
        side1 = random.choice(["SELL","BUY"])
        side2 = "BUY" if side1 == "SELL" else "SELL"
        data_random.append({"side": side1, "quantity": quantity, "trading_pair": trading_pair, "limit": limit, "type": "LIMIT"})
        data_random.append({"side": side2, "quantity": quantity, "trading_pair": trading_pair, "limit": limit, "type": "LIMIT"})
    return data_random
