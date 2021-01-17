#!usr/bin/python3

names = input("Enter names seperated by commas: ").title().split(',')
assignments = input("Enter assignment counts seperated by commas: ").split(',')
grades = input("Enter grades seperated by commas: ").split(',')

assignment_list = []
grade_list = []

# appends each assignment number in assignments [] to a [] of integers
for assignment in assignments:
    assignment_list.append(int(assignment))

# appends each grade number in grades [] to a [] of integers
for grade in grades:
    grade_list.append(int(grade))

message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

# iterates through each set of names, assignments, and grades to print each student's message
for name, assignment, grade in zip(names,assignment_list,grade_list):
    print(message.format(name, assignment, grade, grade + assignment * 2))
