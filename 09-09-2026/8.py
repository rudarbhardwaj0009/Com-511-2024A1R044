# 8. Write a python program to repeatedly calculate the sum of digits of a number unit teh result becomes a single digit.
# Example: 9875 -> 9+8+7+5=29 -> 2+9=11 -> 1+1=2

n = int(input("Enter number: "))

while n > 9:
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    n = s
print(n)