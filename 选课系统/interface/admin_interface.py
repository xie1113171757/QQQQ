from db import modles


def admin_regiseter_interface(name, password):
	"""
	注册接口
	:param name:
	:param password:
	:return:
	"""
	obj = modles.Admin.read(name)
	if obj:
		return False, '用户已存在'
	modles.Admin(name, password)
	return True, '注册成功'


def admin_login_interface(name, password):
	"""
	登陆接口
	:param name:
	:param password:
	:return:
	"""
	obj = modles.Admin.read(name)
	if not obj:
		return False, '账号不存在'
	if obj.password == password:
		return True, '登陆成功'
	else:
		return False, '密码不正确请重新输入'


def create_school_interface(admin_name, school_name, addr):
	"""
	创建学校
	:param admin_name:
	:param school_name:
	:param addr:
	:return:
	"""
	obj = modles.School.read(school_name)
	if obj:
		return False, '学校已经存在'
	else:
		modles.Admin.create_school(admin_name, school_name, addr)
		return True, '创建学校成功'


def create_teacher_interface(admin_name, teacher_name, password):
	"""
	创建老师
	:param admin_name: 管理员
	:param teacher_name: 老师账号
	:param password: 老师密码
	:return:
	"""
	obj = modles.Teacher.read(teacher_name)
	if obj:
		return False, '老师已存在'
	else:
		modles.Admin.create_teacher(admin_name, teacher_name, password)
		return True, '创建老师成功'


def create_course_interface(admin_name, school_name, course_name):
	"""
	创建课程,与学校绑定
	:param admin_name:
	:param school_name:
	:param course_name:
	:return:
	"""

	user_obj = modles.Admin.read(admin_name)
	time = input('请输入课程的时间:').strip()
	if time.isdigit():
		price = input('请输入课程的价格:').strip()
		if price.isdigit():
			user_obj.create_course(course_name, time, price)

			school_list = modles.School.read(school_name)
			obj = school_list.choose_course(course_name)
			if obj is False:
					return False, '学校已经有这门课程了'
			else:
				return True, '创建成功'
		else:
			print('课程价格必须是数字')
	else:
		print('课程时间必须是数字')