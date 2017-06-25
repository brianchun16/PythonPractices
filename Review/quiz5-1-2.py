numbers = []

while True:
	x = int(raw_input('Enter a number:'))

	if x < 0:
		break

	numbers.append(x)


print(max(numbers))
print(min(numbers))
print(sum(numbers))

print((sum(numbers)) / float(len(numbers)))	