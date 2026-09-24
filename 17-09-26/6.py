
# write a python program to store one student data as a tuple: name, roll number, and marks. display grade based on marks.

student = ("Ravi", 101, 85)

marks = student[2]

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 50:
    grade = "C"
else:
    grade = "F"

print("Name:", student[0])
print("Roll No:", student[1])
print("Grade:", grade)