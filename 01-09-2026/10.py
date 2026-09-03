
# write a program to take a 10-digit mobile number and display only the last 4 digits . replace the first 6 digits with ******

number=input("Enter 10 digit number :  ")
n="******"+number[-4:]
print(n)


