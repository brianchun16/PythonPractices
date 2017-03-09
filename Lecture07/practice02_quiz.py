# chemistry, english, chinese
# student 1 = chemistry score of 90, english = --, chinese = --
# finish all 3 student

student1_score = {
	'Chem':95,
	'Eng':100,
	'Chi':83
}

student2_score = {
	'Chem':90,
	'Eng':80,
	'Chi':94
}

student3_score = {
	'Chem':85,
	'Eng':90,
	'Chi':97
}

# students_score = [student1_score, student2_score, student3_score]
# print(students_score)

students_dict = {
	'Brian': student1_score,
	'Alex': student2_score,
	'William': student3_score
}

best_english = ' '
best_chemistry = ' '
eng_max = 0
chem_max = 0
avg_max = 0

for x in students_dict.keys():
	s = students_dict[x

	if s['Eng'] > eng_max:
		eng_max = s['Eng']
		best_english = x

	if s['Chem'] > chem_max:
		chem_max = s['Chem']
		best_chemistry = x

	avg = (s['Eng'] + s['Chem'] + s["Chi"]) / 3

	if avg > avg_max:
		avg_max = avg
		best_avg = x


print('Student ', best_english , 'has earned the highest score for English:', eng_max , )
print('Student ', best_chemistry , 'has earned the highest score for Chemistry:', chem_max , )

print('The valedictorian for this year is' , best_avg, "with a score of " , avg_max)


