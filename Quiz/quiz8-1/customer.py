import random

class Customer(object):
	
	def __init__(self , id , num_of_floors):
		self.cur_floor = random.randint(1, num_of_floors)
		self.id = id
		self.in_elevator = False
		self.finished = False

		while True:
			self.dst_floor = random.randint(1, num_of_floors)

			if self.cur_floor != self.dst_floor:
				break

	def print_status(self):
		print("Customer " + str(self.id) + " ==============")
		print("C Floor: " + str(self.cur_floor))
		print("D Floor: " + str(self.dst_floor))
		print("In Elv : " + str(self.in_elevator))
		print("Is Finish : " + str(self.finished))