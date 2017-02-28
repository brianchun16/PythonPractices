def find_extreme_divisors (n1, n2):
	min_val, max_val = None, None
	for i in range(1, min(n1, n2) + 1):
		if n1 % i == 0 and n2 % i == 0:
			if min_val == None or i < min_val:
				min_val = i
			if max_val == None or i> max_val:
				max_val = i
	return (min_val, max_val)

min_divisor, max_divisor = find_extreme_divisors(100, 200)
print(min_divisor, max_divisor)

