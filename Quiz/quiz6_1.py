bal = float(raw_input('Enter balance: '))
interest_r = float(raw_input('Enter credit card interest rate: '))
mmp_rate = float(raw_input('Enter minimum monthly payment rate: '))

for x in range(1, 13):

	mmp_final = round(mmp_rate * bal , 2)
	interest_p = round((interest_r / 12) * bal , 2)
	principal = round(mmp_final - interest_p , 2)
	bal = round(bal - principal , 2)

	print('Month ' , str(x))
	
	print(mmp_final)
	print(principal)
	print(bal)
