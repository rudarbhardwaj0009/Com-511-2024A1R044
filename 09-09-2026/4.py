# 4. Writa a python program to check whether a nuber is perfect number. A number is perfect if the sum of 
# its proper divisors is equal to the number itself.

n = int(input("Enter number: "))
s = 0

for i in range(1, n):
    if n % i == 0:
        s += i

if s == n:
    print("Perfect")
else:
    print("Not Perfect")
    

