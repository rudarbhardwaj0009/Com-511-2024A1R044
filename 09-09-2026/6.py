# 6. Write a python program to input a decimal number and convert it into binary without using the built-in bin() function.

n = int(input("Enter number: "))
b = ""

while n:
    b = str(n % 2) + b
    n = n // 2
print(b)