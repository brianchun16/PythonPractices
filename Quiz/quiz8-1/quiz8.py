from customer import Customer
from building import Building
from elevator import Elevator

n = int(raw_input('Enter # of floors: '))

b = Building(n)

cn = int(raw_input('Enter # of customers: '))

for x in range(0, cn):
	c = Customer(x , n)
	b.register_wait_c(c)

while True:
	b.run()

	if b.finished:
		break