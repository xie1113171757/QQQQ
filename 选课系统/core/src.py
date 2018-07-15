


from core import admin,student,teacher


func_dic = {
	'1': admin.admin_run,
	'2': teacher.teacher_run,
	'3': student.student_run
	}



def run():
	while True:
		print("""
		1,管理员视图
		2,老师视图
		3,学生视图
		""")
		choice = input("请选择你需要的功能或者q退出:").strip()
		if choice == 'q': break
		if choice not in func_dic:
			continue
		func_dic[choice]()