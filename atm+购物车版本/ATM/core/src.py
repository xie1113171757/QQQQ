from interface import user, bank, shop
from lib import common

user_data = {
    'name': None
}


def login():
    print('登录')
    if user_data['name']:
        print('您已经登录')
        return
    error_coutn = 0
    while True:
        name = input('请输入用户名：')
        if name == 'q': break
        password = input('请输入密码：')
        flag, msg = user.login(name, password)
        if flag:
            user_data['name'] = name
            print(msg)
            break
        else:
            print(msg)
            error_coutn += 1
            if error_coutn > 3:
                user.lock_user(name)
                print('尝试太多，用户锁定')
                break

def register():
    print('注册')
    if user_data['name']:
        print('已经登录不能注册')
        return
    while True:
        name = input('请输入名字:').strip()
        if name == 'q': break
        password = input('请输入密码：').strip()
        conf_password = input('请确认密码：').strip()
        if password == conf_password:
            flag, msg = user.register_interface(name, password)
            if flag:
                print(msg)
                break
            else:
                print(msg)
        else:
            print('两次密码不一致')


@common.login_auth
def check_balance():
    print('查看余额')
    balance = bank.get_balance(user_data['name'])
    print(balance)


@common.login_auth
def transfer():
    print('转账')
    while True:
        to_name = input('请输入对方帐号：').strip()
        if to_name == 'q': break
        account = input('请输入转账金额：').strip()
        if account.isdigit():
            account = int(account)
            flag, msg = bank.transfer_interface(user_data['name'], to_name, account)
            if flag:
                print(msg)
                break
            else:
                print(msg)
        else:
            print('请输入数字')


@common.login_auth
def withdraw():
    print('取款')
    while True:
        account = input('输入取款金额：').strip()
        if account.isdigit():
            account = int(account)
            flag, msg = bank.withdraw_interface(user_data['name'], account)
            if flag:
                print(msg)
                break
            else:
                print(msg)
        else:
            print('请输入数字')


@common.login_auth
def repay():
    print('还款')
    account = input('请输入还款金额：').strip()
    if account == 'q': return
    if account.isdigit():
        account = int(account)
        flag, msg = bank.repay_interface(user_data['name'], account)
        if flag:
            print(msg)
        else:
            print(msg)
    else:
        print('请输入数字')


@common.login_auth
def check_record():
    print('查看流水')
    bankflow = bank.check_record_interface(user_data['name'])
    for flow in bankflow:
        print(flow)


@common.login_auth
def shopping():
    '''
    1 先循环打印出商品
    2 用户输入数字选择商品（判断是否是数字，判断输入的数字是否在范围内）
    3 取出商品名，商品价格
    4 判断用户余额是否大于商品价格
    5 余额大于商品价格时，判断此商品是否在购物车里
        5.1 在购物车里，个数加1
        5.1 不在购物车里，拼出字典放入（｛‘good’：｛‘price’：10，‘count’：1｝｝）
    6 用户余额减掉商品价格
    7 花费加上商品价格
    8 当输入 q时，购买商品
        8.1 消费为0 ，直接退出
        8.2 打印购物车
        8.3 接受用户输入，是否购买 当输入y，直接调购物接口实现购物
    :return:
    '''
    print('购物')
    goods_list = [
        ['coffee', 10],
        ['chicken', 20],
        ['iphone', 8000],
        ['macPro', 15000],
        ['car', 100000]
    ]
    user_balance = bank.get_balance(user_data['name'])
    cost = 0
    shopping_cart = {}
    while True:
        for i, goods in enumerate(goods_list):
            print('%s : %s' % (i, goods))
        buy = input('请输入要购买的商品（数字）').strip()
        if buy.isdigit():
            buy = int(buy)
            if buy >=len(goods_list):continue
            goods_name = goods_list[buy][0]
            goods_price = goods_list[buy][1]
            if user_balance >= goods_price:
                if goods_name in shopping_cart:
                    shopping_cart[goods_name]['count'] += 1
                else:
                    shopping_cart[goods_name] = {'price': goods_price, 'count': 1}
                user_balance-=goods_price
                cost+=goods_price
                print('%s 加入了购物车' % goods_name)
            else:
                print('余额不足')
                continue
        elif buy =='q':
            if cost == 0: break
            print(shopping_cart)
            confim = input('确认购买？（y/n）').strip()
            if confim =='y':
                flag,msg=shop.shopping_interface(user_data['name'],shopping_cart,cost)
                if flag:
                    print(msg)
                    break
                else:
                    print(msg)
            else:
                print('什么也没买')
                break
        else:
            print('输入非法')



@common.login_auth
def check_shoppingcart():
    print('查看购买商品')
    shopping_cart = shop.check_shoppingcart(user_data['name'])
    if shopping_cart:
        print(shopping_cart)


func_dic = {
    '1': register,
    '2': login,
    '3': check_balance,
    '4': transfer,
    '5': withdraw,
    '6': repay,
    '7': check_record,
    '8': shopping,
    '9': check_shoppingcart

}


def run():
    while True:
        print('''
        1 注册
        2 登录
        3 查看余额
        4 转账
        5 取款
        6 还款
        7 查看流水
        8 购物
        9 查看购买商品
        ''')
        choice = input('请选择>>:').strip()
        if choice not in func_dic: continue
        func_dic[choice]()
