# write a python program to take an eamil address and print the domain name

# email=input("Enter Email : ")
# print(email[10:])

email= input("Enter email : ")
index = email.find("@")
domain = email[index + 1: ]
print("Domain = ", domain)