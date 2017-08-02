from building import Building
from elevator import Elevator
from customer import Customer

building = Building()
building.elevator = Elevator()

building.num_of_floors = int(raw_input('Insert the number of floors: '))
building.elevator.num_of_floors = building.num_of_floors

building.elevator.init_currentfloor(building)

num_of_customers = int(raw_input('Insert number of people: '))

for i in range(num_of_customers):
	customer = Customer()
	customer.id = i
	customer.rand_setting(building)

	building.customer_list.append(customer)



while True:
	building.run()

	if building.is_finish:
		break
