from course import Course
from grade import Grade
from student import Student


# makes an instance for Course
course = Course()

# creates 3 students
student1 = Student(1, 'Brian')
student2 = Student(2, 'Alex')
student3 = Student(3, 'Ben')

course.add_student(student1)
course.add_student(student2)
course.add_student(student3)
#print(len(course.all_students()))

grade1_1 = Grade(91, 'math')
grade1_2 = Grade(93, 'eng')

grade2_1 = Grade(74, 'math')
grade2_2 = Grade(80, 'eng')

grade3_1 = Grade(90, 'math')
grade3_2 = Grade(50, 'eng')

# uses add_grade method from course to append in values established above
course.add_grade(student1, grade1_1)
course.add_grade(student1, grade1_2)

course.add_grade(student2, grade2_1)
course.add_grade(student2, grade2_2)

course.add_grade(student3, grade3_1)
course.add_grade(student3, grade3_2)

print(course.grade_report())

