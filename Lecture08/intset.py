# Define IntSet class
class IntSet(object):
	"""docstring for ClassName"""
	def __init__(self):
		# variable for values / the parentheses makes a collection of values
		self.vals = []

	# inserts the "e" value in to set, also checks if its not there
	def insert(self, e):
		if not e in self.vals:
			self.vals.append(e)

	# checks if e is in the value set (True/False)
	def member(self, e):
		return e in self.vals

	# removes e value, if function checks if it is there or not. 
	# else is for when e is not there, prints the statement
	def remove(self, e):
		if self.member(e):
			self.vals.remove(e)
		else:
			print(str(e) + " is not member. cannot remove")

	# when the class is used, it organizes then prints the values
	def __str__(self):
		self.vals.sort()
		return '{' + ",".join(str(x) for x in self.vals) + '}'


intSet1 = IntSet()
intSet1.insert(3)
intSet1.insert(4)
intSet1.insert(5)
print(intSet1)

intSet2 = IntSet()
intSet1.insert(9)
intSet1.insert(4)
intSet1.insert(5)
print(intSet1)