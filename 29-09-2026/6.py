# Write a Python program to create records of students. Store each student record as a dictionary containing roll number,
# name, branch, and marks. Store all records of students in a list and search for a student using roll number. Roll numbers must be unique.

students = []

n = int(input("Enter number of students: "))

for i in range(n):
    roll = input("Enter roll number: ")

    if any(s["roll"] == roll for s in students):
        print("Roll number already exists")
        continue

    name = input("Enter name: ")
    branch = input("Enter branch: ")
    marks = int(input("Enter marks: "))

    students.append({
        "roll": roll,
        "name": name,
        "branch": branch,
        "marks": marks
    })

roll = input("Enter roll number to search: ")

for s in students:
    if s["roll"] == roll:
        print(s)
        break
else:
    print("Student not found")