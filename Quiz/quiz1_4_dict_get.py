performances = {'Ventriloquism':'9:00am', 
               'Snake Charmer': '12:00pm', 
               'Amazing Acrobatics': '2:00pm', 
               'Bearded Lady':'5:00pm'}

# if Bearded Lady(dictinary's key) doesn't exist, this would show an error
# showtime = performances['Bearded Lady']
# the get function(that dict normally has) would not cause an error and assigns None value
showtime = performances.get('Bearded Lady')

if showtime == None:
    print('Performance doesn\'t exist')
else:
    print('The time of the Bearded Lady show is ', showtime)
