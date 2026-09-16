# write a python program to print a right-angled triangle using stars
# *
# * *
# * * *
# * * * *


n = int(input("Enter rows: "))

for i in range(1, n + 1):
    print("* " * i)