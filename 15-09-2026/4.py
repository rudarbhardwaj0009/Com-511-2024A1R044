# write a python program to print an inverted right-angled triangle using stars.
# * * * *
# * * *
# * *
# *

n = int(input("Enter rows: "))

for i in range(n, 0, -1):
    print("* " * i)
    
      