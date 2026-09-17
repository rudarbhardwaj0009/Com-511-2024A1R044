# write a pytho program to input marks of n students in alist. display highest marks, lowestmarks, average marks, and number of students who passed.

n = int(input("Enter n: "))
a = list(map(int, input("Enter marks: ").split()))

print("Highest:", max(a))
print("Lowest:", min(a))
print("Average:", sum(a)/n)
print("Passed:", sum(m >= 40 for m in a))
