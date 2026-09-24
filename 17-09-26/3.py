# write a python program to show that tuple values cannot be changed directly. convert tuple into list,
# update it, and convert it back into tuple


t = (10, 20, 30)

l = list(t)
l[1] = 50

t = tuple(l)

print(t)


