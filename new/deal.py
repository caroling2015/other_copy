# -*- encoding: utf-8 -*-
from common import get_balance,create_order,cancel_orders_by_pair
from own_operate import order_fee
from conf import dot,pair,data

# 实现委托卖单，买单成交
def deal(data):
    for each in data:
        coin_one = each['trading_pair'][:-dot] # numerator分子
        coin_two = each['trading_pair'][-dot:] #denominator分母
        before_numerator  = int(get_balance(coin_one)['result']['balance']) #交易前分子币的数量
        before_denominator = int(get_balance(coin_two)['result']['balance']) #交易前分母币的数量
        order = create_order(each)
        print order

        if order['status']['success']!=1:
            print "order fail,Cause %s"%(str(order['status']['message']))
            return

        if each['side']!='SELL' and each['side']!='BUY':
            print "No supporting"
            return

        if each['side']=='SELL':
            after_numerator = int(get_balance(coin_one)['result']['balance']) #交易后分子币的数量
            print 'before deal %s:%d' % (coin_one, before_numerator)
            print 'before deal %s:%d' % (coin_two, before_denominator)
            print 'after deal %s:%d' % (coin_one, after_numerator)
            if each['quantity'] != before_numerator - after_numerator:
                print "Sell:quantity is wrong"
            else:
                print 'Sell order %s suc,waiting bid' % order['result']['order_id']
                print '----------------------------------------------------------------'

        if each['side']=='BUY':
            after_denominator = int(get_balance(coin_two)['result']['balance']) #交易后分母币的数量
            after_numerator = int(get_balance(coin_one)['result']['balance'])
            print 'before deal %s:%d' % (coin_one, before_numerator)
            print 'before deal %s:%d' % (coin_two, before_denominator)
            print 'after deal %s:%d' % (coin_one, after_numerator)
            print 'after deal %s:%d' % (coin_two, after_denominator)
            fee = order_fee(coin_two,each['quantity'],each['limit'])
            sum_fee = int(fee*2*1e8)  #不加int()强制类型转换,导致后面float型与long int型比较时出错
            print 'fee %s:%d'%(coin_two,sum_fee)
            actual_fee = before_denominator - after_denominator
            if sum_fee != actual_fee:# int & long int
                print "Buy:quantity is wrong"
            else:
                print "Buy order %s suc,bid suc"%order['result']['order_id']
                print '----------------------------------------------------------------'

if __name__ == '__main__':
    for each in pair:
        cancel_orders_by_pair(each)
    deal(data)