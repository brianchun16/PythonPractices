import sys

num = [] 

for x in range(0,10):
	num.append(int(raw_input('Enter number: ')))

has_even = False
even_min = sys.maxint

for x in num:
	if x % 2 == 0:
		has_even = True
		if x < even_min: 
			even_min = x

if has_even == False:
	print('No even number found')

else:
	print(even_min)
