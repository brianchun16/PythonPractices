import sys

num_integers = int(input('Enter the number of integers you want to input: '))

even_min = None #sys.maxint
real_integers = []

for x in range(0,num_integers):
	input_num = int(input('Enter integer: '))

	if input_num % 2 == 0:
		real_integers.append(input_num)

		if even_min == None or input_num < even_min:
			even_min = input_num

if not real_integers:
	print('Error')
else:
	print(even_min)
