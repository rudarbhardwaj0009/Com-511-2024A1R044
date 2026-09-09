# Write a python program to input four numbers from the user and find the greatest number among them .

a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Enter number 3: "))
d = int(input("Enter number 4: "))

greatest = max(a, b, c, d)

print("Greatest number =", greatest)