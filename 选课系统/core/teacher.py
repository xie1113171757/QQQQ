from lib import common
from interface import teacher_interface, common_interface

teacher_name = {'name': None}


def teacher_login():
	"""
	登陆
	:return:
	"""
	while True:
		name = input('请输入账号或输入q退出:').strip()
		if name == 'q': break
		password = input('请输入密码:').strip()
		flag, msg = common.login_common('teacher', name, password)
		if flag:
			teacher_name['name'] = name
			print(msg)
			break
		else:
			print(msg)


@common.login_auth('teacher')
def check_all_course():
	"""
	查看所有课程
	:return:
	"""

	course_list = common_interface.check_all_file('course')
	if not course_list:
		print('请联系管理员创建课程')
		return
	for k in course_list:
		print(k)


@common.login_auth('teacher')
def choose_course():
	"""
	选择教授的课程
	:return:
	"""
	course_list = common_interface.check_all_file('course')
	if not course_list:
		print('请联系管理员创建课程')
		return
	while True:
		for k,course in enumerate(course_list):
			print('%s: %s' % (k, course))
		chioce = input('请选择课程或者q退出:').strip()
		if chioce == 'q': break
		if chioce.strip().isdigit():
			chioce = int(chioce)
			if chioce < len(course_list):
				flag, msg = teacher_interface.choose_course_interface(teacher_name['name'], course_list[chioce])
				if flag:
					print(msg)
					break
				else:
					print(msg)

			else:
				print('输入非法')
		else:
			print('请输入序列号')


@common.login_auth('teacher')
def check_course_student():
	"""
	查看课程下的学生
	:return:
	"""
	course_list = common_interface.check_all_file('course')
	if not course_list:
		print('请联系管理员创建课程')
		return
	while True:
		for k, course in enumerate(course_list):
			print('%s: %s' % (k, course))
		chioce = input('请选择课程或者q退出:').strip()
		if chioce == 'q': break
		if chioce.strip().isdigit():
			chioce = int(chioce)
			if chioce < len(course_list):
				msg = teacher_interface.check_course_student_interface(course_list[chioce])
				print(msg)
				return
			else:
				print('输入非法')
		else:
			print('请输入序列号')


@common.login_auth('teacher')
def amend_student_score():
	"""
	修改学生成绩
	:return:
	"""
	course_list = common_interface.check_all_file('course')
	if not course_list:
		print('请联系管理员创建课程')
		return
	while True:
		for k, course in enumerate(course_list):
			print('%s: %s' % (k, course))
		auth = input('请选择课程或者q退出:').strip()
		if auth == 'q': break
		if auth.strip().isdigit():
			auth = int(auth)
			if auth < len(course_list):
				student_list = common_interface.check_all_file('student')
				if not student_list:
					print('请联系管理员招聘学生')
					return
				while True:
					for k, student in enumerate(student_list):
						print('%s: %s' % (k, student))
					choice = input('请选择要修改的学生序号或者输入q退出:').strip()
					if choice == 'q': break
					if choice.strip().isdigit():
						choice = int(choice)
						if choice < len(student_list):
							sum = input('请输入你要打的分数:').strip()
							if not sum.isalnum():
								print('必须是数字')
								continue
							flag, msg = teacher_interface.amend_student_score_interface(teacher_name['name'], course_list[auth], student_list[choice], sum)
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





@common.login_auth('teacher')
def out_name():
	teacher_name['name'] = None


func_dic = {
	'1': teacher_login,
	'2': check_all_course,
	'3': choose_course,
	'4': check_course_student,
	'5': amend_student_score,
	'6': out_name}


def teacher_run():
	while True:
		print("""
		1,登陆
		2,查看所有课程
		3,选择课程
		4,查看课程下的学生
		5,修改学生分数
		6,退出登陆
		""")
		choice = input("请选择你需要的功能或者q退出:").strip()
		if choice == 'q': break
		if choice not in func_dic:
			continue
		func_dic[choice]()
