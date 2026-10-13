# Write a program to perform searching activity using Linear and Binary Search.

a = [10, 20, 30, 40, 50]
x = int(input("Enter number: "))

if x in a:
    print("Linear Search: Found")
else:
    print("Linear Search: Not Found")

low = 0
high = len(a) - 1

while low <= high:
    mid = (low + high) // 2

    if a[mid] == x:
        print("Binary Search: Found")
        break
    elif x > a[mid]:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("Binary Search: Not Found")