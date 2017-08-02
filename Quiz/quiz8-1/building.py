from elevator import Elevator

class Building(object):

	def __init__(self , num_of_floors):
		self.num_of_floors = num_of_floors
		self.w_customer_list = []
		self.elevator = Elevator(num_of_floors)
		self.finished = False

	def register_wait_c(self , c):
		self.w_customer_list.append(c)

	def run(self):
		print("====================================================================")
		print("============== Elevator Status =====================")
		print("====================================================================")
		print("E's Cur Floor: ", self.elevator.cur_floor)
		print("E's Direction: ", self.elevator.direction)

		current_floor = self.elevator.cur_floor 

		self.output()
		
		if len(self.w_customer_list) > 0:
			for x in self.w_customer_list[:]:
				if x.cur_floor == current_floor:
					print('******* In Elv *******')
					x.in_elevator = True
					self.elevator.register_customer(x)
					self.w_customer_list.remove(x)
		else:
			if len(self.elevator.register_list) > 0:
				for x in self.elevator.register_list[:]:
					if x.dst_floor == current_floor:
						print('******* Out Elv *******')
						x.finished = True
						self.elevator.cancel_customer(x)
			else: 
				self.finished = True

		self.elevator.move()

	def output(self):
		print("<<<<<<<<<<<<<< Customers Information >>>>>>>>>>>>>>>")

		for c in self.w_customer_list:
			c.print_status()

		for c in self.elevator.register_list:
			c.print_status()

		