import sys

x = int(raw_input("Enter a number: "))
y = int(raw_input("Enter a number: "))
z = int(raw_input("Enter a number: "))

has_odd = False
odd_max = -sys.maxint - 1

if x % 2 == 1:
	has_odd = True
	if x > odd_max:
		odd_max = x 

if y % 2 == 1:
	has_odd = True
	if y > odd_max:
		odd_max = y
	
if z % 2 == 1:
	has_odd = True
	if z > odd_max:
		odd_max = z

if has_odd == False:
	print('No odd number found')

else: 
	print(odd_max)
	