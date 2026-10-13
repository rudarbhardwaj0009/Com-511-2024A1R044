'''
wap to  store multiple students records as a list of tuples.Each tuple should contain name,roll number, and marks. dispaly std who scored above 75
'''
students = [("Raj", "R019", 90),("Aman", "R020", 65),("Rahul", "R021", 80),("Simran", "R022", 70)]
for student in students:
    if student[2] > 75:
        print(student)