from db import modles


def student_register_interface(name, password):
	"""
	学生注册接口
	:param name:
	:param password:
	:return:
	"""
	obj = modles.Student.read(name)
	if obj:
		return False, '此账号已存在'
	modles.Student(name, password)
	return True, '注册成功'


def choose_school_interface(student_name, school_name):
	"""
	选择学校
	:param student_name: 学生名
	:param school_name: 学校名
	:return:
	"""
	obj = modles.Student.read(student_name)
	if obj.school is None:
		obj.choose_school(school_name)
		return True, '选择学校成功'
	else:
		return False, '已经选择了学校'


def choose_course_interface(school_name, student_name, course_name):
	"""
	选择课程
	:param student_name: 学生名
	:param course_name: 课程名
	:return:
	"""
	obj = modles.Student.read(student_name)
	if obj.school == school_name:
		course = obj.choose_course_name(course_name)

		if course is False:
			return False, '你已经选择了这门课程'
		else:
			course_obj = modles.Course.read(course_name)  # 拿到课程对象
			course_obj.add_student(student_name)   # 关联学生
			return True, '选择课程成功'
	else:
		return False, '请先联系管理员更改学校'


def check_scores_interface(student_name, course_name):
	"""
	查看成绩
	:param student_name:
	:param course_name:
	:return:
	"""
	obj = modles.Student.read(student_name)
	if course_name in obj.score:
		return obj.score[course_name]
	else:
		return False, '该学生还没有选择这门课程'
