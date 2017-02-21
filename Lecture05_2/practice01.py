def multitable_19():

	x = int(input('Enter an integer ranging from 2-19: '))
	y = 1
	if 1 < x < 20:
		while y < 20:
			print(x, "*" , y , " =" , x * y)
			y = y + 1

	else: 
		print('That number is not valid.')

multitable_19()