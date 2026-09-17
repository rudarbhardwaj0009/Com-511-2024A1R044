# Write a python program to input a list of numbers and create a new list containing only unique elements.

a = list(map(int, input("Enter numbers: ").split()))

b = list(set(a))

print(b)