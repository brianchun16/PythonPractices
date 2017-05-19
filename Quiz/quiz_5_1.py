num_integers = int(input('Enter the number of integers you want to input: '))
int_values = []

for x in range(0,num_integers):
	input_n = int(input('Enter integers: '))
	
	if input_n >= 0:
		cube_root_n = input_n ** (1. / 3.)
	else:
		cube_root_n = abs(input_n) ** (1. / 3.)
		cube_root_n = cube_root_n * -1

	print(cube_root_n)


	