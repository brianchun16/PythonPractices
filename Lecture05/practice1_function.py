def print_name(first_name, last_name, reverse = False):
	if reverse:
		print(last_name + ", " + first_name)
	else:
		print(first_name, last_name)


print_name('Brian', 'Chun')
print_name('Brian', 'Chun', True)
print_name('Brian', 'Chun', reverse = True)

# Error!
# print_name('Brian', True, last_name = 'Chun')