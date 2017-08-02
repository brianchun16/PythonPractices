import random

class Elevator(object):
	
	def __init__(self):
		self.num_of_floors = 0
		self.register_list = []
		self.cur_floor = 0
		self.direction = 'Down'

	def move(self):
		if self.direction == 'Down' and self.cur_floor > 1:
			self.cur_floor = self.cur_floor - 1
		elif self.direction == 'Down' and self.cur_floor == 1:
			self.direction = 'Up'
			self.cur_floor = self.cur_floor + 1
		elif self.direction == 'Up' and self.cur_floor < self.num_of_floors:
			self.cur_floor = self.cur_floor + 1
		elif self.direction == 'Up' and self.cur_floor == self.num_of_floors:
			self.direction = 'Down'
			self.cur_floor = self.cur_floor - 1
	
	def register_customer(self):
		print('')

	def cancel_customer(self):
		print('')

	def init_currentfloor(self , building):
		self.cur_floor = random.randint(1, building.num_of_floors)

		if self.cur_floor == 1:
			self.direction = 'Up'		
