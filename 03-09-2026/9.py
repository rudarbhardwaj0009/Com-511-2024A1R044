# write a python program to create a simple password validation system.
# The program should repeatedly ask the user to enter a pssword untila valid password is entered.
# A password will be considered valid only if it has at least 8 characters and contain the @ symbol.
# Once the user enters a valid password, the program should diaplay "Password accepted". and stop otherwisw, 
# it should display " Weak Password. Try Again" and ask for thge password again.

p = input("Password: ")

while len(p) < 8 or "@" not in p:
    print("Weak Password. Try Again")
    p = input("Password: ")

print("Password accepted")












# Write a python program to input four numbers from the user and find the greatest number among them .