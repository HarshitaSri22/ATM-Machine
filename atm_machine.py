import random
import sys 
import time as t
class ATM():
    def __init__(self, name, account_number, balance = 0,check_balance1=5000):
        self.name = name
        self.account_number = account_number
        self.balance = balance
    def account_detail(self):
        print("\n----------ACCOUNT DETAIL----------")
        print(f"Account Holder: {self.name.upper()}")
        print(f"Account Number: {self.account_number}")
        print(f"Available balance: Nu.{self.balance}\n")
         
    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Current account balance: Nu.", self.balance)
        print()
 
    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
           
            print("Insufficient fund!")
            print(f"Your balance is Nu.{self.balance} only.")
            print("Try with lesser amount than balance.")
            print()
        else:
            self.balance = self.balance - self.amount
            print(f"Nu.{amount} withdrawal successful!")
            print("Current account balance: Nu.", self.balance)
            print()

    def transfer_funds(self,check_balance):
        self.check_balance1=5000
        self.check_balance=check_balance
        self.balance=self.balance+self.check_balance
        self.check_balance1=self.check_balance1-self.check_balance
        print(self.balance)
        print(self.check_balance1)



    def transaction(self):      
        print("""
            TRANSACTION 
        *******
            Menu:
            1. Account Detail
            2. Deposit
            3. Withdraw
            4. Transfer Funds
            5.exit
        *******
        """)
        
        while True:
            try:
                option = int(input("Enter 1, 2, 3, 4, 5 :"))
            except:
                print("Error: Enter 1, 2, 3, 4, 5 only!\n")
                continue
            else:
                if option == 1:
                    atm.account_detail()
                elif option == 2:
                    amount = int(input("How much you want to deposit(Nu.):"))
                    atm.deposit(amount)
                elif option == 3:
                    amount = int(input("How much you want to withdraw(Nu.):"))
                    atm.withdraw(amount)
                elif option ==4:
                    check_balance=int(input("Amount to be addedL:"))
                    if (check_balance>5000):
                      print("Enter Amount below 5000")
                    else:
                      atm.transfer_funds(check_balance)
                elif option==5:
                    print("Thanks for choosing us as your bank...Visit us again!")
                    return
                    
                    
print("**WELCOME TO BANK OF PSIT**")
print("_____________________\n")
print("----------ACCOUNT CREATION----------")
name = input("Enter your name: ")
while True:
    try:
        account_number = int(input("Enter your account number: "))
        break
    except ValueError:
        print("Input should be in the form of integer only!")
    
print("Congratulations! Account created successfully......\n")
 
atm =ATM(name, account_number)
c=0
while True:
  n=int(input("Enter Pin:"))
  m=int(input("Re-Enter Pin:"))
  if n==m:
    trans = input("Do you want to do any transaction?(y/n):")
    if trans == "y":
        atm.transaction()
        break
    elif trans == "n":
        print("Thanks for choosing us as your bank...Visit us again!")
        break
    else:
        print("Wrong command!  Enter 'y' for yes and 'n' for NO.\n")
  else:
    c+=1
    if c==3:
        print("You have attempted maximum limit of wrong pin entering!!")
        break
    print("Please re-enter the pin carefully!")
