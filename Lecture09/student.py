#imports person class that specifically only has similarities with student class
from person import Person

class Student(Person):
	#adds grade and id (the differences) as terms
	def __init__(self):
		super(self.__class__, self).__init__()
		self.grade = 0
		self.id = 0

	def set_grade(self, grade):
		self.grade = grade

	def set_id(self, id):
		self.id = id
	#the str function from "Person" is repeated here alongside unique terms (grade id)
	def __str__(self):
		return super(self.__class__, self).__str__() + ", Grade : " + str(self.grade) + ", ID: " + str(self.id)

"""
student = Student()
student.set_name('Brian Chun')
student.set_bday('April 16 2001')
student.set_height(171)
student.set_grade(10)
student.set_id(1000)
print(student)
"""


