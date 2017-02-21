left_operand = 2
right_operand = 1

while left_operand <= 9:
	print(left_operand, '---------------------------')
	while right_operand < 10:
		print(left_operand , "*" , right_operand , " =" , left_operand * right_operand)
		right_operand = right_operand + 1

	left_operand = left_operand + 1
	right_operand = 1
	
