# Create a database using lists and tuples. Each student record must contain roll number, name, branch, and CGPA.
# Store each record as a tuple inside a list. Display all records and search for a student using roll number.

# Conditions:
# Each record should be stored as a tuple.
# Complete database should be stored as a list.
# Roll numbers must be unique.

students = []

n = int(input("Enter number of students: "))

for i in range(n):
    roll = input("Enter roll number: ")

    if any(s[0] == roll for s in students):
        print("Roll number already exists")
        continue

    name = input("Enter name: ")
    branch = input("Enter branch: ")
    cgpa = float(input("Enter CGPA: "))

    students.append((roll, name, branch, cgpa))

print("\nStudent Records:")
for s in students:
    print(s)

roll = input("\nEnter roll number to search: ")

for s in students:
    if s[0] == roll:
        print("Student found:", s)
        break
else:
    print("Student not found")