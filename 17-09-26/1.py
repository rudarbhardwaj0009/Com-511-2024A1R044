# write a python program to store two points at tuples and calculate the distance between them.

import math

p1 = (2, 3)
p2 = (5, 7)

distance = math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)

print("Distance =", distance)



