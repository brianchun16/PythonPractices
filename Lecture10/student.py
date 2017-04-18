class Student(object):
	def __init__(self, id_num, name):
		self.id_num = id_num
		self.name = name

	def get_id_num(self):
		return self.id_num

#student = Student(1234, 'Brian')
#print(student.get_id_num())