# Write a python program to input marks of 10 students. store only valid marks between 0 abd 100 in a list. skip invalid marks

marks = []

for i in range(10):
    m = int(input("Enter marks: "))
    if 0 <= m <= 100:
        marks.append(m)

print(marks)