bal = int(raw_input('Enter balance: '))
mmpr = float(raw_input('Enter minimum monthly payment rate: '))
int_r = float(raw_input('Enter annual interest rate: '))

for x in xrange(1 , 13):
	mmp = mmpr * bal
	int_p = round((int_r / 12) * bal, 2)
	p_paid = round(mmp - int_p, 2)
	bal = round(bal - p_paid, 2)

	print('Month: %d, %s' % (x, "!!!"))
	print(mmp)
	print(p_paid)
	print(bal)


#	print('Month ' + str(x) + ': ')
#	print(round(mmp , 2))
#	print(round(p_paid , 2))
#	print(round(bal , 2))
