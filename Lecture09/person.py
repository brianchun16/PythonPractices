class Person(object):
	
	def __init__(self):
		self.name = ""
		self.bday = ""
		self.height = 0	
	# def set_something creates function for adding specific values
	def set_name(self, name):
		self.name = name

	def set_bday(self, bday):
		self.bday = bday

	def set_height(self, height):
		self.height = height
	#combines values in string format
	def __str__(self):
		return "Name : " + self.name + ", Birth: " + self.bday + ", Height: " + str(self.height)
