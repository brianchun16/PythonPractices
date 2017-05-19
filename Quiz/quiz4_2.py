x = int(input('Enter number: '))
y = int(input('Enter number: '))
z = int(input('Enter number: '))

odd_numbers = []

if x % 2 != 0:
	odd_numbers.append(x)
	
if y % 2 != 0:
	odd_numbers.append(y)

if z % 2 != 0:
	odd_numbers.append(z)

if not odd_numbers:
	print('Error')
else:
	odd_max = 0

	for x in odd_numbers:

		if x > odd_max:
			odd_max = x

	print(odd_max)
