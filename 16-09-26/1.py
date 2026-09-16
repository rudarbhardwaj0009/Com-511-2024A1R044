# write a pytho program to input marks of n students in alist. display highest marks, lowestmarks, average marks, and number of students who passed.

n = int(input("Enter n: "))
a = list(map(int, input("Enter marks: ").split()))

print("Highest:", max(a))
print("Lowest:", min(a))
print("Average:", sum(a)/n)
print("Passed:", sum(m >= 40 for m in a))


# Write a python program to input marks of 10 students. store only valid marks between 0 abd 100 in a list. skip invalid marks

# write a python program to input numbers in a list and find the second largest number.

# Write a python program to input a list of numbers and create a new list containing only unique elements.