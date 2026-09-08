# Take a password and check lenght, presence of @, and whether first and last characters are different

p = input("Password: ")

print(len(p) >= 8)
print("@" in p)
print(p[0] != p[-1])



