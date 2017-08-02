class Building(object):

	def __init__(self):
		self.num_of_floors = 0
		self.customer_list = []
		self.elevator = None
		self.is_finish = True

	def run(self):
		print("====================================================================")
		print("============== Elevator Status =====================")
		print("====================================================================")
		print("E's Cur Floor: ", self.elevator.cur_floor)
		print("E's Direction: ", self.elevator.direction)

		c_elv = self.elevator.cur_floor
		for x in self.customer_list:
			if x.finished == False:
				if x.cur_floor == c_elv and x.in_elevator == False:
					x.in_elevator = True
					print(str(x.id) + " -> Elevator")
				if x.dst_floor == c_elv and x.in_elevator == True:
					x.finished = True
					print(str(x.id) + " -> Destination")


		self.output()

		self.is_finish = True
		for c in self.customer_list:
			if c.finished == False:
				self.is_finish = False

		self.elevator.move()

	def output(self):
		print("<<<<<<<<<<<<<< Customers Information >>>>>>>>>>>>>>>")

		for c in self.customer_list:
			print("Customer " + str(c.id) + " ==============")
			print("C Floor: " + str(c.cur_floor))
			print("D Floor: " + str(c.dst_floor))
			print("In Elv : " + str(c.in_elevator))
			print("Is Finish : " + str(c.finished))

		print("")
		print("")