"""
Create a BankAccount class that stores an account holder's name and balance.
Add instance methods to deposit money, withdraw money, and display the balance.
Do not allow a withdrawl grater than the available balance.
"""

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount Deposited Successfully.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient Balance !!")

    def display(self): 
        
        print("Account Holder : ",self.name)
        print("Account Balance : ",self.balance)


name = input("Enter Account Holder's Name : ")
balance = float(input("Enter initial Balance : "))

acc1 = BankAccount(name, balance)

deposit_amt = float(input("Enter amount to deposit: "))
acc1.deposit(deposit_amt)

withdraw_amt = float(input("Enter amount to withdraw: "))
acc1.withdraw(withdraw_amt)

acc1.display()