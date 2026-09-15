#1. write a python program that asks the user to enter a username and password. the user should get only 3 attempts.
# if the correct credentials are entered, display "Login Successful" and stop the loop.
# if all attempts are used, display "Account Locked ".


username=(input("Enter username : "))
password=input("Enter password : ")
attempts=3
while attempts<=3:
    username=(input("Enter correct_username : "))
    password=input("Enter correct_password : ")
    
    if username==username and password==password:
        print("Login Successful ")
        break
    else:
        attempts=attempts-1
        print("Wrong Details. Attempts left: ", attempts)
        
if attempts== 0:
    print("Account Locked")

