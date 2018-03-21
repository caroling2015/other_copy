import random
from common import create_order

pair = ['JRCETP','JRCETH','JRCBTC']

def get_Data(num,trading_pair):
    random.seed(6)
    data_random = []
    if num < 1:
        print 'num must bigger than 1'
        return
    for i in range(0,num):
        limit = random.randint(50000000,60000000)
        quantity = random.randint(100000000,10000000000)
        side1 = random.choice(["SELL","BUY"])
        side2 = "BUY" if side1 == "SELL" else "SELL"
        data_random.append(
            {"side": side1, "quantity": quantity, "trading_pair": trading_pair, "limit": limit, "type": "LIMIT"})
        data_random.append(
            {"side": side2, "quantity": quantity, "trading_pair": trading_pair, "limit": limit, "type": "LIMIT"})
    return data_random

new_Data = get_Data(10,pair[1])
for each in new_Data:
    print each
    info = create_order(each)
    print 'order:%d created!'%info['result']['order_id']
