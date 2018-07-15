from db import db_handler


class Beaesclass:
	@classmethod
	def read(cls, name):  # cls 是类
		return db_handler.read(name, cls.__name__.lower())

	def write(self):
		db_handler.write(self)


class Admin(Beaesclass):
	def __init__(self, name, password):
		"""
		注册管理员
		:param name:
		:param password:
		"""
		self.name = name
		self.password = password
		self.write()

	def create_school(self, name, addr):
		"""
		创建学校
		:param name:
		:param addr:
		:return:
		"""
		School(name, addr)

	def create_teacher(self, name, password):
		"""
		创建老师
		:param name:
		:param password:
		:return:
		"""
		Teacher(name, password)

	def create_course(self, name, time, price):
		"""
		创建课程
		:param name:
		:param time:
		:param price:
		:return:
		"""
		Course(name, time, price)


class School(Beaesclass):
	def __init__(self, name, addr):
		"""
		实例化学校
		:param name: 学校名
		:param addr: 学校地址
		"""
		self.name = name
		self.addr = addr
		self.course_list = []  # 学校课程
		self.write()

	def choose_course(self, course_name):
		"""
		选择课程加入学校
		:param course_name:
		:return:
		"""
		if course_name in self.course_list:
			return False
		self.course_list.append(course_name)
		self.write()


class Course(Beaesclass):
	def __init__(self, name, time, price):
		"""
		课程实例化
		:param name: 课程名字
		:param time: 时间
		:param price: 价钱
		"""
		self.name = name
		self.time = time
		self.price = price
		self.student_list = []
		self.write()

	def add_student(self, student_name):
		"""
		把学生加入到课程里
		:param student_name:
		:return:
		"""
		if student_name in self.student_list:
			return False
		self.student_list.append(student_name)
		self.write()


class Student(Beaesclass):
	def __init__(self, name, password):
		self.name = name
		self.password = password
		self.school = None
		self.course = []
		self.score = {}
		self.write()

	def choose_school(self, school):
		"""
		选择学校
		:param school:
		:return:
		"""
		self.school = school
		self.write()

	def choose_course_name(self, course):
		"""
		选择课程
		:param course:
		:return:
		"""
		if course in self.course:
			return False
		self.score[course] = 0
		self.course.append(course)
		self.write()


class Teacher(Beaesclass):
	def __init__(self, name, password):
		"""
		老师实例化
		:param name: 账号
		:param password: 密码
		"""
		self.name = name
		self.password = password
		self.course_list = []
		self.write()

	def choose_course(self, course):
		"""
		把选择的课程加到列表里
		:param course: 课程名
		:return:
		"""
		if course in self.course_list:
			return False
		self.course_list.append(course)
		self.write()

	def amend_student_score(self, student_name, course, sum):
		"""
		修改学生分数
		:param student_name: 学生名
		:param course: 课程
		:param sum: 分数
		:return:
		"""
		student_name.score[course] = sum
		student_name.write()
