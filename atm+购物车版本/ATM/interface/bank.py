from  db import db_handler
from lib import common
bank_logger=common.get_logger('bank')

def get_balance(name):
    user_dic = db_handler.select(name)
    return user_dic['balance']


def transfer_interface(from_name, to_name, account):
    if from_name == to_name:
        return False,'不能向自己转账'
    to_dic = db_handler.select(to_name)
    if to_dic:
        from_dic = db_handler.select(from_name)
        if account > from_dic['balance']:
            return False, '您的余额不足'
        else:
            from_dic['balance'] -= account
            from_dic['bankflow'].append('您向%s转账 %s 元' % (to_dic['name'], account))
            to_dic['bankflow'].append('您收到%s 转账 %s 元' % (from_dic['name'], account))
            to_dic['balance'] += account
            db_handler.save(from_dic)
            db_handler.save(to_dic)
            bank_logger.info('向%s转账 %s 元' % (to_dic['name'], account))
            return True, '转账成功'
    else:
        return False, '对方不存在'


def withdraw_interface(name, account):
    user_dic = db_handler.select(name)
    if user_dic['balance'] >= account * 1.05:
        user_dic['balance'] -= account * 1.05
        db_handler.save(user_dic)
        return True, '取款成功'
    else:
        return False, '余额不足，不能取现'


def repay_interface(name, account):
    user_dic = db_handler.select(name)
    user_dic['balance'] += account
    user_dic['bankflow'].append('%s 还款 %s 元'%(name,account))
    db_handler.save(user_dic)
    return True, '还款成功'

def consume_interfaec(name,cost):
    user_dic = db_handler.select(name)
    if user_dic['balance'] >=cost:
        user_dic['balance']-=cost
        user_dic['bankflow'].append('消费 %s 元'%cost)
        db_handler.save(user_dic)

        return True,'消费成功'
    else:
        return False,'余额不足'

def check_record_interface(name):
    user_dic=db_handler.select(name)
    return user_dic['bankflow']