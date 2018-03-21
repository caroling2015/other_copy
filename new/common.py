# -*- encoding: utf-8 -*-
from conf import *
import requests
import json
from rw_csv import w_text

def get(url):
    resp = requests.get(url, headers=headers)
    return resp.json()

def post(url, data):
    resp = requests.post(url, data=json.dumps(data), headers=headers)
    return resp.json()

def delete(url):
    resp = requests.delete(url,headers=headers)
    return resp.json()

def put(url):
    resp = requests.put(url,headers=headers)
    return resp.json()

# account
def get_balance(coin):
    url = 'http://' + host + '/api/trader/balance/%s'%coin
    return get(url)

def list_balances():
    url = 'http://' + host + '/api/trader/balances'
    return get(url)


def list_deposit(asset,page=0):
    url = 'http://' + host + '/api/trader/deposits/%s/%d'%(asset,page)
    return get(url)


def list_withdrawal(asset,page=0):
    url = 'http://' + host + '/api/trader/withdrawals/%s/%d'%(asset,page)
    return get(url)

# order
def create_order(data):
    url = 'http://'+ host + '/api/trader/order'
    return post(url,data)


def cancel_orders(trading_pair,order_id):
    url = 'http://' + host + '/api/trader/order/%s/%s'%(trading_pair,order_id)
    return delete(url)


def list_active_orders(trading_pair):
    url = 'http://' + host + '/api/trader/orders/%s'%trading_pair
    return get(url)


def list_history_orders(trading_pair,order_id):
    url = 'http://' + host + '/api/trader/history/%s/%s'%(trading_pair,order_id)
    return get(url)


def list_history_trades(trading_pair,page=0):
    url = 'http://' + host + '/api/trader/historys/%s/%d'%(trading_pair,page)
    return get(url)


def list_trading_pairs():
    url = 'http://' + host + '/api/trader/trading_pairs'
    return get(url)

def cancel_orders_by_pair(pair):
    info = list_active_orders(pair)
    if info['status']['success']==0:
        w_text(info['status']['message'])
        return
    if info['result']!=[]:
        for each in info['result']:
            w_text("---Start cancel order:%s---" % each['id'])
            cancel_orders(pair, each['id'])
    else:
        w_text("There is no order in %s" % pair)