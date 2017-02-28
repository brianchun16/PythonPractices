techs = ['MIT', 'Caltech']
ivys = ['Harvard', 'Yale', 'Brown']

univs = [techs, ivys]
univs1 = [['MIT', 'Caltech'], ['Harvard', 'Yale', 'Brown']]

print 'univs =', univs
print univs == univs1

techs.append('Princeton')

print 'univs =', univs
print 'univs1 =', univs1
print univs == univs1
