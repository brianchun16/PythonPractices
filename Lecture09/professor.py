from person import Person

class Professor(Person):
	def __init__(self):
		super(self.__class__,self).__init__()
		self.major = ''
		self.wage = 0
		
	def set_major(self, major):
		self.major = major
	
	def set_wage(self, wage):
		self.wage = wage

	def __str__(self):
		return super(self.__class__,self).__str__() + ", Major : " + self.major + ", Wage : " + str(self.wage)

professor = Professor()
professor.name = 'Jonghoon Chun'
#professor.set_name('Jonghoon Chun')
professor.set_bday('December 30')
professor.set_height(177)
professor.set_major('Computer Science')
professor.set_wage(1000)
print(professor)