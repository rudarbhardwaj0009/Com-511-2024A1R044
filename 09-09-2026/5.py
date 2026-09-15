
# 5. Write a python program to input a number and reverse it using arithemetic operations only.

n = int(input("Enter number: "))
r = 0

while n > 0:
    r = r * 10 + n % 10
    n = n // 10

print(r)