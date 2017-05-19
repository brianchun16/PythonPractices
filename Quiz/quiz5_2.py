
option = 'Y'

while option == 'Y':
	c1 = raw_input('Enter a character: ')
	i1 = int(raw_input('Enter an integer: '))

	for x in range(0, i1):
		print(c1 * (x + 1))

	c2 = raw_input('Enter a character: ')

	for x in range(0, i1):
		print(c2 * (i1 - x))

	option = raw_input("Would you like to continue?(Y/N) : ")
	
print('Bye')
