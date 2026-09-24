#6.Write a Pyhton program to rotate a list one position to the right.
n = list(map(int, input("Enter elements: ").split()))

n = [n[-1]] + n[:-1]

print("Rotated list:", n)
