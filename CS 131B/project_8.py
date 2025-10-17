'''
Program:  project_8.py 
Programmer: Jeffrey Sun
Date: 07/21/2025
Description:  This program tests the Account, SavingsAccount, and CheckingAccount classes.
'''

from account import Account
from savingsaccount import SavingsAccount
from checkingaccount import CheckingAccount

def main():
    baseAccount = Account("Base Account", 1000.00)
    savingAccount = SavingsAccount("Savings Account", 23210.50, 0.01)
    checkingAccount = CheckingAccount("Checking Account", 521.38, 1.25)

    print("--- Initial Account States ---")
    print(baseAccount)
    print(savingAccount)
    print(checkingAccount)

    addInterest = savingAccount.calculate_interest()
    savingAccount.deposit(addInterest)

    print("\n--- Account States After Interest Deposit ---")
    print(baseAccount)
    print(savingAccount)
    print(checkingAccount)
# End main

main()

'''
------------- Sample Output -------------
--- Initial Account States ---
Account Name: Base Account
Account Balance: 1000.0
Account Name: Savings Account
Account Balance: 23210.5
Interest Rate: 0.01
Account Name: Checking Account
Account Balance: 521.38
Transaction Fee: 1.25

--- Account States After Interest Deposit ---
Account Name: Base Account
Account Balance: 1000.0
Account Name: Savings Account
Account Balance: 23442.605
Interest Rate: 0.01
Account Name: Checking Account
Account Balance: 521.38
Transaction Fee: 1.25
----------- End Sample Output -----------
'''