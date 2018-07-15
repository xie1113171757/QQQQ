from db import modles


def check_all_course_interface(teacher_name):
	"""
	查看老师所有课程
	:param teacher_name:
	:return:
	"""
	obj = modles.Teacher.read(teacher_name)
	return obj.course_list


def choose_course_interface(teacher_name, course_name):
	"""
	老师选择课程
	:param teacher_name:
	:param course_name:
	:return:
	"""
	obj = modles.Teacher.read(teacher_name)

	course = obj.choose_course(course_name)
	if course:
		return True, '选择课程成功'
	else:
		return False, '老师已经有了这门课程'


def check_course_student_interface(course_name):
	"""
	查看课程下的学生
	:param course_name:
	:return:
	"""
	course = modles.Course.read(course_name)
	if course_name in course.student_list:
		return course.student_list[course_name]


def amend_student_score_interface(teacher_name, student_name, course_name, sum):
	"""
	修改学生课程分数
	:param teacher_name:
	:param student_name:
	:param sum:
	:return:
	"""
	obj = modles.Teacher.read(teacher_name)
	course = modles.Course.read(course_name)
	if course:
		obj.amend_student_score(student_name, course_name, sum)
		return True, '修改分数成功'
	else:
		return False, '没有这门课程'
