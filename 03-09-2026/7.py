# Write a python program to simulate a digital lock system.
# The lock should ask the user to enter a 4-digit PIN. if the entered PIN does not contain exactly 4-digits,
# the program should display an error message and ask again. if the entered PIN is correct, the lock should open.
# otherwise, the program should ask the user to try again


pin = input("Enter PIN: ")

while len(pin) != 4:
    print("Enter exactly 4 digits")
    pin = input("Enter PIN: ")

if pin == "1234":
    print("Lock Open")
else:
    print("Wrong PIN")