def is_in(s1, s2):
	if (s2 in s1) or (s1 in s2):
		return True
	else:
		return False

s1 = raw_input('Enter a word: ')
s2 = raw_input('Enter a word: ')

result = is_in(s1, s2)

if result:
	print('One string exists in the other.')

else:
	print('X')