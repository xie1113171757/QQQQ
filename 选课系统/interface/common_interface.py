import os
from conf import setting


def check_all_file(user_type):
	"""
	遍历所有文件夹,找到我需要的那个
	:return:
	"""
	path = os.path.join(setting.BASE_DB, user_type)
	if not os.path.exists(path):  # 如果没有这个文件夹,那么生成这个文件夹
		os.mkdir(path)
	file_path = os.listdir(path)
	return file_path



