# write a python program to input numbers in a list and find the second largest number.

a = list(map(int, input("Enter numbers: ").split()))

a.sort()
print("Second largest:", a[-2])