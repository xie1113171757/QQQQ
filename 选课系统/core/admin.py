from interface import admin_interface, common_interface
from lib import common

admin_name = {'name': None}


def admin_regiseter():
	"""
	注册
	:return:
	"""
	while True:
		name = input('请输入账号或者q退出:').strip()
		if not name: continue
		if name == 'q': break
		password = input("请输入密码:").strip()
		password1 = input('请确认密码:').strip()
		if password == password1:
			flag, msg = admin_interface.admin_regiseter_interface(name, password)
			if flag:
				print(msg)
				break
			else:
				print(msg)
		else:
			print('两次密码不正确,请重新输入')


def admin_login():
	"""
	登陆
	:return:
	"""
	while True:
		name = input('请输入账号或者q退出:').strip()
		if name == 'q': break
		password = input('请输入密码:').strip()
		flag, msg = admin_interface.admin_login_interface(name, password)
		if flag:
			admin_name['name'] = name
			print(msg)
			break
		else:
			print(msg)


@common.login_auth('admin')
def create_school():
	"""
	创建学校
	:return:
	"""
	while True:
		school_name = input("请输入学校名字或者q退出:").strip()
		if not school_name:
			print('学校名字必须有')
			continue
		if school_name == 'q': break
		addr = input('请输入学校地址:').strip()
		flag, msg = admin_interface.create_school_interface(admin_name['name'], school_name, addr)
		if flag:
			print(msg)
			break
		else:
			print(msg)


@common.login_auth('admin')
def create_teacher():
	"""
	创建老师
	:return:
	"""
	while True:
		name = input('请输入老师账号或者q退出:').strip()
		if not name: continue
		if name == 'q': break
		password = input('请输入密码:').strip()
		password1 = input('请确认密码:').strip()
		if password == password1:
			flag, msg = admin_interface.create_teacher_interface(admin_name['name'], name, password)
			if flag:
				print(msg)
				break
			else:
				print(msg)
		else:
			print('两次密码不对,请重新输入')


@common.login_auth('admin')
def create_course():
	"""
	创建课程
	:return:
	"""
	school_list = common_interface.check_all_file('school')
	if not school_list:
		print('请联系管理员创建学校')
		return
	while True:
		for k, school in enumerate(school_list):
			print('%s:%s' % (k, school))
		choice = input("请选择学校或者q退出:").strip()
		if choice == 'q': break
		if choice.isdigit():
			choice = int(choice)
			if choice < len(school_list):
				course_name = input('请输入需要创建的课程:').strip()
				if not course_name: continue
				flag, msg = admin_interface.create_course_interface(admin_name['name'], school_list[choice], course_name)
				if flag:
					print(msg)
					break
				else:
					print(msg)
			else:
				print('输入非法')

		else:
			print('请输入数字')


@common.login_auth('admin')
def out_name():
	admin_name['name'] = None


func_dic = {
	'1': admin_regiseter,
	'2': admin_login,
	'3': create_school,
	'4': create_teacher,
	'5': create_course,
	'6': out_name}


def admin_run():
	while True:
		print("""
		1,注册
		2,登陆
		3,创建学校
		4,创建老师 
		5,创建课程
		6,退出登陆
		""")
		choice = input("请选择你需要的功能或者q退出:").strip()
		if choice == 'q': break
		if choice not in func_dic:
			continue
		func_dic[choice]()
