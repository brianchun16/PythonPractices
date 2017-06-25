import sys

cnt = 0
n_max = 0
n_min = sys.maxint
n_sum = 0
a = 0

while True:
	x = int(raw_input('Enter a number: '))
	
	if x < 0:
		break

	cnt = cnt + 1
	n_sum = n_sum + x
	a = n_sum / (cnt * 1.0)

	if n_max < x:
		n_max = x

	if n_min > x:
		n_min = x

print(n_max)
print(n_min)
print(n_sum)
print(a)