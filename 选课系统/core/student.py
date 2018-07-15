from interface import student_interface, common_interface
from lib import common

student_name = {'name': None}


def student_register():
	"""
	注册
	:return:
	"""
	if student_name['name']:
		print('你已经登陆了')
		return
	while True:
		name = input("请输入账号或者输入q退出:").strip()
		if not name: continue

		if name == 'q': break
		password = input('请输入密码:').strip()
		password1 = input('请确认密码:').strip()
		if password == password1:
			flag, msg = student_interface.student_register_interface(name, password)
			if flag:
				print(msg)
				break
			else:
				print(msg)


def student_login():
	"""
	登陆
	:return:
	"""
	if student_name['name']:
		print('你已经登陆了')
		return
	while True:
		name = input('请输入账号或者输入q退出:').strip()
		if name == 'q': break
		password = input('请输入密码:').strip()
		flag, msg = common.login_common('student', name, password)
		if flag:
			student_name['name'] = name
			print(msg)
			break
		else:
			print(msg)


@common.login_auth('student')
def choose_school():
	"""
	选择学校
	:return:
	"""
	school_list = common_interface.check_all_file('school')
	if not school_list:
		print('请联系管理员创建学校')
		return
	while True:
		for k, school in enumerate(school_list):
			print('%s: %s' % (k, school))
		choice = input('请选择学校序列号或者输入q退出:').strip()
		if choice == 'q': break
		if choice.strip().isalnum():
			choice = int(choice)
			if choice < len(school_list):
				flag, msg = student_interface.choose_school_interface(student_name['name'], school_list[choice])
				if flag:
					print(msg)
					break
				else:
					print(msg)

			else:
				print('输入非法')
		else:
			print('请输入数字')


@common.login_auth('student')
def choose_course():
	"""
	选择课程
	:return:
	"""
	school_list = common_interface.check_all_file('school')
	if not school_list:
		print('请联系管理员创建学校')
		return
	while True:
		for k, school in enumerate(school_list):
			print('%s: %s' % (k, school))
		auth = input('请选择学校序列号或者输入q退出:').strip()
		if auth == 'q': break
		if auth.strip().isalnum():
			auth = int(auth)
			if auth < len(school_list):
				course_list = common_interface.check_all_file('course')
				if not course_list:
					print('没有课程,请联系管理员')
					return
				while True:
					for k, course in enumerate(course_list):
						print('%s : %s' % (k, course))
					choice = input("请选择课程或者输入q退出:").strip()
					if choice == 'q': break
					if choice.strip().isalnum():
						choice = int(choice)
						if choice < len(course_list):
							flag, msg = student_interface.choose_course_interface(school_list[auth], student_name['name'], course_list[choice])
							if flag:
								print(msg)
								break
							else:
								print(msg)
						else:
							print('输入非法')
					else:
						print('请输入序列号')
			else:
				print('输入非法')
		else:
			print('请输入序列号')


@common.login_auth('student')
def check_scores():
	"""
	查看成绩
	:return:
	"""
	course_list = common_interface.check_all_file('course')
	if not course_list:
		print('没有课程,请联系管理员')
		return
	while True:
		for k, course in enumerate(course_list):
			print('%s : %s' % (k, course))
		choice = input("请选择课程或者输入q退出:").strip()
		if choice == 'q': break
		if choice.strip().isalnum():
			choice = int(choice)
			if choice < len(course_list):
				msg = student_interface.check_scores_interface(student_name['name'], course_list[choice])
				print(msg)
				break
			else:
				print('输入非法')
		else:
			print('请输入序列号')


@common.login_auth('student')
def out_name():
	student_name['name'] = None


func_dic = {
	'1': student_register,
	'2': student_login,
	'3': choose_school,
	'4': choose_course,
	'5': check_scores,
	'6': out_name}


def student_run():
	while True:
		print("""
		1,注册
		2,登陆
		3,选择学校
		4,选择课程
		5,查看分数
		6,退出登陆
		""")
		choice = input("请选择你需要的功能或者q退出:").strip()
		if choice == 'q': break
		if choice not in func_dic:
			continue
		func_dic[choice]()
