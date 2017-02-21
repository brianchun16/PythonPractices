x = int(input('Enter an integer: '))
x = abs(x)

ans = 0
while ans**3 < x:
	ans = ans+1

if ans**3 == x:
	print('X is a perfect cube')
	print('The X value is: ', ans)
else:
	print('X is not a perfect cube')
	print('The X value is:', ans)
