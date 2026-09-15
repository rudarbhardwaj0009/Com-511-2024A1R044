# 2. Write a python program to input a number and check whether it is prime or not . 
# A number is prime if it has no divisor other than 1 and itself.

n = int(input("Enter number: "))

for i in range(2, n):
    if n % i == 0:
        print("Not Prime")
        break
else:
    print("Prime")