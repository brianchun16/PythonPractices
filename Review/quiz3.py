c = raw_input('Enter a character: ')
h = int(raw_input('Enter the height of the triangle: '))

for x in range(1 , h + 1):
	print(c * x)

c = raw_input('Enter a character: ')

for x in range(1 , h + 1):
	rt = h - x + 1
	print(c * rt)
