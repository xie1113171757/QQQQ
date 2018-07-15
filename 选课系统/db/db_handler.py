import os
import pickle
from conf import setting


def write(cls):
	"""
	写入
	:return:
	"""
	path = os.path.join(setting.BASE_DB, cls.__class__.__name__.lower())
	if not os.path.exists(path):
		os.mkdir(path)
	path_file = os.path.join(path, cls.name)
	with open(path_file, 'wb')as f:
		pickle.dump(cls, f)
		f.flush()
		return True


def read(name, user_type):
	"""
	读
	:param name:
	:return:
	"""
	path = os.path.join(setting.BASE_DB, user_type)
	if not os.path.exists(path):
		os.mkdir(path)
	path_file = os.path.join(path, name)
	if os.path.exists(path_file):
		with open(path_file, 'rb')as f:
			return pickle.load(f)
	else:
		return False
