performances = {'Ventriloquism':'9:00am', 
                'Snake Charmer': '12:00pm', 
                'Amazing Acrobatics': '2:00pm', 
                'Enchanted Elephants':'5:00pm'}

# items calls both the keys and the values
for name, showtime in performances.items():
    # 'sep =' allows you to decide what happens when you print something between commas
    print(name, ':', showtime, sep='')
