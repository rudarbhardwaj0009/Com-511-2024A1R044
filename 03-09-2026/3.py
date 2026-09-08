# Take a email adress and print username, domain, and reversed domain

e = input("Email: ")
a = e.split("@")

print(a[0])
print(a[1])
print(a[1][::-1])