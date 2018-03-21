# -*- encoding: utf-8 -*-
#----------------------用户账户---------------------------------------
##52 environment  tester_tt02@163.com
host = '52.53.159.206'
signature='qr4n8a7g744m63hwb8v39yatswwzuyx239bzy8jmhdzh67jya7qnbb'
apikey='e34acfd4d2b45ea3af247786a9ceb387'

##54 environment  tester_tt01@163.com
# host = '54.183.77.249'
# signature='26f5jrpaqb6ptdw7r4xhfftjar818bfa9sqkytuv6w98qvvp1fv5v1'
# apikey='5559ab1a5fe117c6462351f7810adfff'
#--------------------------------------------------------------------

# 费率及最小交易费全局参数
ETP_min_fee = 0.01                     #ETP最小交易费
ETH_min_fee = 0.001                    #ETH最小交易费
BTC_min_fee = 0.0001                   #BTC最小交易费
BCY_min_fee = 0.1
rate = 0.001                           #交易费率
dot = 3                                #分母位数

headers = {
    'signature': '%s' % signature,
    'apikey': '%s' % apikey,
    'Content-Type': 'application/json',
    'host': '%s' % host
}


# *****************************适用场景*******************************
# data适用于卖买匹配的交易
# 1.撤消或购买掉测试环境的所有委买委卖订单,确保运行前当前交易对下无委托订单
# 2.必须先卖后买
# 3.买卖数量及单价一致，完全成交
# 4.适用于过功能测试
# *******************************************************************
# data_frozen适用于卖买不匹配的交易
# 1.撤消或购买掉测试环境的所有委买委卖订单,确保运行前当前交易对下无委托订单
# 2.必须先卖后买
# 3.买卖数量及单价一致，完全成交
# 4.适用于过功能测试

pair = ['CLETP','CLETH','CLBTC']    #待测试交易对

data = [
    # {"side":"SELL","quantity":10000000000, "trading_pair":pair[0], "limit": 50000000,"type":"LIMIT"},
    # {"side":"BUY","quantity": 10000000000, "trading_pair":pair[0], "limit": 50000000,"type":"LIMIT"},
    # {"side":"SELL","quantity":1000000000, "trading_pair":pair[0], "limit": 50000000,"type":"LIMIT"},
    # {"side":"BUY","quantity": 1000000000, "trading_pair":pair[0], "limit": 50000000,"type":"LIMIT"},
    # {"side":"SELL","quantity":800000000, "trading_pair":pair[0], "limit": 50000000,"type":"LIMIT"},
    # {"side":"BUY","quantity": 800000000, "trading_pair":pair[0], "limit": 50000000,"type":"LIMIT"},
    #---------------------------------------------
    {"side": "SELL", "quantity": 1230000000, "trading_pair": pair[1], "limit": 5000000, "type": "LIMIT"},
    {"side": "BUY",  "quantity": 1230000000, "trading_pair": pair[1], "limit": 5000000, "type": "LIMIT"},
    {"side": "SELL", "quantity": 1000000000, "trading_pair": pair[1], "limit": 5000000, "type": "LIMIT"},
    {"side": "BUY",  "quantity": 1000000000, "trading_pair": pair[1], "limit": 5000000, "type": "LIMIT"},
    {"side": "SELL", "quantity": 800000000, "trading_pair": pair[1], "limit": 5000000, "type": "LIMIT"},
    {"side": "BUY",  "quantity": 800000000, "trading_pair": pair[1], "limit": 5000000, "type": "LIMIT"},
    # ---------------------------------------------
    {"side": "SELL", "quantity": 1230000000, "trading_pair": pair[2], "limit": 500000, "type": "LIMIT"},
    {"side": "BUY",  "quantity": 1230000000, "trading_pair": pair[2], "limit": 500000, "type": "LIMIT"},
    {"side": "SELL", "quantity": 1000000000, "trading_pair": pair[2], "limit": 500000, "type": "LIMIT"},
    {"side": "BUY",  "quantity": 1000000000, "trading_pair": pair[2], "limit": 500000, "type": "LIMIT"},
    {"side": "SELL", "quantity": 800000000, "trading_pair": pair[2], "limit": 500000, "type": "LIMIT"},
    {"side": "BUY",  "quantity": 800000000, "trading_pair": pair[2], "limit": 500000, "type": "LIMIT"},

]

data_frozen = [
    # {"side":"SELL","quantity":100000000, "trading_pair":pair[0], "limit": 600000000,"type":"LIMIT"},
    # {"side":"BUY","quantity": 100000000, "trading_pair":pair[0], "limit": 500000000,"type":"LIMIT"},
    {"side":"SELL","quantity":100000000, "trading_pair":pair[1], "limit": 60000000,"type":"LIMIT"},
    {"side":"BUY","quantity": 100000000, "trading_pair":pair[1], "limit": 50000000,"type":"LIMIT"},
    {"side":"SELL","quantity":100000000, "trading_pair":pair[2], "limit": 6000000,"type":"LIMIT"},
    {"side":"BUY","quantity": 100000000, "trading_pair":pair[2], "limit": 5000000,"type":"LIMIT"}
]





