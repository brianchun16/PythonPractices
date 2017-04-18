class Course(object):

	def __init__(self):
		self.students = [] #collection/list
		self.grades = {} #dictionary
		self.is_sorted = True #boolean t/f

	def add_student(self, student):
		if student in self.students :
			raise ValueError('Duplicate student ')
		self.students.append(student)
		self.grades[student.get_id_num()] = []
		self.is_sorted = False

	def add_grade(self, student, grade):
		try:
			self.grades[student.get_id_num()].append(grade)
		except:
			raise ValueError('Student not in mapping')

	def get_grades(self, student):
		try:
			return self.grades[student.get_id_num()][:]
		except:
			raise ValueError('Student not in mapping')

	def all_students(self):
		if not self.is_sorted:
			self.students.sort()
		return self.students[:]

	def grade_report(self):
		report = ''

		for s in self.all_students():
			tot = 0.0
			num_grades = 0

			for g in self.get_grades(s):
				tot += g.score
				num_grades += 1

			try:
				average = tot/num_grades
				report = report + '\n'\
						+ str(s.name) + '\'s mean grade is '\
						+ str(average)
			except ZeroDivisionError:
				report = report + '\n'\
						+ str(s) + ' has no grades'
						
		return report

