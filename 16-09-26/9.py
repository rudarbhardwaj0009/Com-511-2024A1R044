# write a python program to input two lists and create a third list containing common elements.

a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

c = []

for x in a:
    if x in b:
        c.append(x)

print(c)