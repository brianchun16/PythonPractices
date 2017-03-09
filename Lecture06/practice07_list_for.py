techs = ['MIT', 'Caltech']
ivys = ['Harvard', 'Yale', 'Brown']

univs = [techs, ivys]
univs: [['MIT', 'Caltech'], ['Harvard', 'Yale', 'Brown']]

for e in univs: 
	print ('univs contains', e)
	print (' which contains')
	print(e)

	for u in e:
		print('   ', u)


print(techs + ivys)

techs.extend(ivys)
print(techs)
