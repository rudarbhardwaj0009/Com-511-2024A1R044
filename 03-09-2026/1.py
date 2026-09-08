#take a student full name and roll number. generate email using first 3 letters of first name, first 3 letters of last name, and last 3 characters of roll 

name = input("Enter name: ")
roll = input("Enter roll no: ")

a = name.split()

email = a[0][:3] + a[-1][:3] + roll[-3:]

print(email.lower())