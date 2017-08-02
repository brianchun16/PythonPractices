import random

class Customer(object):
	
	def __init__(self):
		self.cur_floor = 0
		self.dst_floor = 0
		self.id = 0
		self.in_elevator = False
		self.finished = False

	def rand_setting(self, building):
		self.cur_floor = random.randint(1, building.num_of_floors)

		while True:
			self.dst_floor = random.randint(1, building.num_of_floors)

			if self.cur_floor != self.dst_floor:
				break

		
