# This program that will ask a student for their grade in 5 subjects.
history = float(input("grade (a number between 0-100: "))
mathematics = float(input("grade between 0-100: "))
physics = float(input("grade a number between 0-100: "))
chemestry = float(input("grade a number between 0-100: "))
english = float(input("grade a number between 0-100: "))

# Calculation the average grade of student.
average_grade = (history + mathematics + physics + chemestry + english)/5

#print student's average grade.
print(average_grade)

# Classified average grade from A-E
if average_grade > 90:
    print(f"{average_grade} is A")
elif average_grade > 80:
    print(f"{average_grade} is B")
elif average_grade > 70:
    print(f"{average_grade} is C")
elif average_grade > 60:
    print(f"{average_grade} is D")
else: 
    print(f"{average_grade} is E===Failed")