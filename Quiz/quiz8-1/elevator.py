import random

class Elevator(object):

	def __init__(self , num_of_floors):
		self.num_of_floors = num_of_floors
		self.register_list = []
		self.cur_floor = random.randint(1, num_of_floors)
		self.direction = 'Down'
		if self.cur_floor == 1:
			self.direction = 'Up'


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
	

	def register_customer(self , customer):
		self.register_list.append(customer)

	def cancel_customer(self , customer):
		self.register_list.remove(customer)