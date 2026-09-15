# 3. Write a python program to input two numbers and find thier greatest common divisor using a loop.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

while b:
    a, b = b, a % b

print("GCD =", a)