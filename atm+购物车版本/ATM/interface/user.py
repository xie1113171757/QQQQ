from db import db_handler
from lib import common

user_logger = common.get_logger('user')


def register_interface(name, password, balance=1500):
    user_dic = db_handler.select(name)
    if user_dic:
        return False, '用户已经存在'
    else:
        user_dic = {'name': name, 'password': password, 'locked': False, 'balance': balance, 'credit': balance,
                    'bankflow': [], 'shoppingcart': {}}
        db_handler.save(user_dic)
        user_logger.info('%s 注册了' % name)

        return True, '注册成功'


def login(name, password):
    user_dic = db_handler.select(name)
    if user_dic:
        if password == user_dic['password']:
            return True, '登录成功'
        else:
            return False, '密码错误'
    else:
        return False, '用户不存在'


def lock_user(name):
    user_dic = db_handler.select(name)
    if user_dic:
        user_dic['locked'] = True
        db_handler.save(user_dic)
        user_logger.info('%s 被锁定了' % name)


def un_lock_user(name):
    user_dic = db_handler.select(name)
    if user_dic:
        user_dic['locked'] = False
        db_handler.save(user_dic)
        user_logger.info('%s 被解锁了' % name)
