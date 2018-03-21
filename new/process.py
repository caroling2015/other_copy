# -*- encoding: utf-8 -*-
from common import get_balance,create_order,cancel_orders_by_pair
from own_operate import order_fee,order_sum
from conf import data_frozen,dot,pair
from rw_csv import w_text

#买单：冻结分母数量=分子单价*分子数量+手续费（小于最低手续费为最低，大于时按实际手续费计算
#卖单：冻结分子的数量 测试委托交易后，未成交前，下单数量是否从balance中移到frozen,是则冻结成功
# numerator 分子币
# denominator 分母币

def order_frozen(data_frozen):
    for each in data_frozen:
        w_text(str(each))
        coin_one = each['trading_pair'][:-dot]
        coin_two = each['trading_pair'][-dot:]
        # 交易前分子币冻结数量
        before_numerator  = int(get_balance(coin_one)['result']['frozen'])
        # 交易前分母币冻结数量
        before_denominator = int(get_balance(coin_two)['result']['frozen'])
        order = create_order(each)
        w_text('Frozen %s before SELL/Buy:%d'%(coin_one,before_numerator)+\
               '\n'+ 'Frozen %s before SELL/Buy:%d' % (coin_two,before_denominator))
        if order['status']['success']!=1:
            if str(order['status']['message'])== 'ERR_ASSET_NOT_EXISTS':
                w_text('In Account, there is no %s'%coin_one)
                return
            print order
            w_text("Order fail,Cause %s" % str(order['status']['message']))
            return
        if each['side']!= 'BUY' and each['side']!= 'SELL':
            w_text("Not supporting")
            return
        if each['side']== 'SELL':
            # 交易后分子币冻结数量
            after_numerator = int(get_balance(coin_one)['result']['frozen'])
            w_text('Frozen %s after SELL/Buy:%d' % (coin_one, after_numerator))
            if each['quantity'] != after_numerator - before_numerator:
                w_text("Frozen fail after SELL,quantity is wrong")
                w_text('-------------------------------------------------------')
            else:
                w_text('Sell order %s suc,waiting bid' % order['result']['order_id'])
                w_text('-------------------------------------------------------')
        if each['side']== 'BUY':
            # 交易后分母币冻结数量
            after_denominator = int(get_balance(coin_two)['result']['frozen'])
            w_text('Frozen %s after SELL/Buy:%d' % (coin_two, after_denominator))
            fee = order_fee(coin_two, each['quantity'], each['limit'])
            # 不加int()强制类型转换,导致后面float型与long int型比较时出错
            sum = int((fee + order_sum(each['quantity'], each['limit'])) * 1e8)
            actual_sum = after_denominator - before_denominator
            w_text('fee of %s:%d' % (coin_two, sum))
            w_text('actual fee:%d' % (actual_sum))
            # type : int & long int
            if sum != actual_sum:
                w_text("Frozen fail after Buy,quantity is wrong")
                w_text('-------------------------------------------------------')
            else:
                w_text("Buy order %s suc,waiting bid" % order['result']['order_id'])
                w_text('-------------------------------------------------------')

if __name__ == '__main__':
    for each in pair:
        cancel_orders_by_pair(each)
    # order_frozen(data_frozen)


