# Take name, branch, and yaer. Generate a code using string concatention, slicing, and repetition.

n = input("Name: ")
b = input("Branch: ")
y = input("Year: ")

print(n[:2] + b[:2] + y[-2:] + " ")