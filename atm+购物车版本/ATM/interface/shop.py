from db import db_handler
from interface import bank
from lib import common

shop_logger=common.get_logger('shop')

def check_shoppingcart(name):
    user_dic = db_handler.select(name)
    shop_logger.info('%s 查看了购物车'%name)
    return user_dic['shoppingcart']


def shopping_interface(name, shopping_cart,cost):
    flag,msg= bank.consume_interfaec(name,cost)
    if flag:
        user_dic = db_handler.select(name)
        user_dic['shoppingcart'] = shopping_cart
        db_handler.save(user_dic)
        shop_logger.info('%s 购买了商品' % name)
        return True, '购买成功'
    else:
        return False,msg


