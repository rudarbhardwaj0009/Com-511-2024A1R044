# write a program to input numbers in a list and create to seperate

#lists for even and odd numbers.
n=list(map(int,input("Enter Number:").split()))
even=[]
odd=[]
for i in n:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("Even Numbers:",even)
print("Odd Numbers:",odd)






