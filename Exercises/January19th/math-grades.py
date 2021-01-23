# Author: Gatlin Lawson

#Gather Grades
assignments = float(input("Assignements Grade: "))
exercises = float(input("Exercises Grade: "))
midterm = float(input("Midterm Grade: "))
final = float(input("Final Grade: "))

finalGrade = assignments * .5 + exercises * .2 + midterm * .15 + final * .15

print(f"Final grade is {finalGrade}")