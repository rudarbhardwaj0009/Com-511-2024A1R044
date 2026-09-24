# write a python program to check whether a given value is present in a tuple. if present, display its position.

t = (10, 20, 30, 40)

x = int(input("Enter value: "))

if x in t:
    print("Position =", t.index(x))
else:
    print("Not present")