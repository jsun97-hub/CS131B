'''
Program:  account.py 
Programmer: Jeffrey Sun
Date: 07/21/2025
Description:  This program defines the Account class, which contains a name and balance attribute
and contains methods for displaying the Account information (attributes) and withdrawing from the 
Account balance.
'''
class Account:
    '''
    Represents a generic bank account with a name and a balance.
    Provides methods to deposit, withdraw, and view account details.
    '''
    def __init__(self, name, balance):
        '''
        Initializes an Account object with a name and balance.
        '''
        self.name = None
        self.balance = 0.0
        self.setName(name)
        self.setBalance(balance)

    def getName(self):
        '''
        Returns the name associated with the account.
        '''
        return self.name

    def setName(self, name):
        '''
        Sets or updates the name for the account.
        '''
        self.name = str(name)

    def getBalance(self):
        '''
        Returns the current balance of the account.
        '''
        return self.balance

    def setBalance(self, balance):
        '''
        Sets or updates the balance for the account.
        Validates that the balance is not negative; sets to 0 if it is.
        '''
        if balance < 0:
            print('Balance must be a positive value. Setting balance to 0.00.')
            self.balance = 0.00
        else:
            self.balance = balance

    def withdraw(self, amount):
        '''
        Withdraws a given amount from the balance.
        Validates that the amount is positive and not greater than the available balance.
        '''
        if amount > self.balance:
            print('Withdrawal amount must be less than or equal to the available balance.')
        elif amount < 0:
            print('Withdrawal amount must be a positive value.')
        else:
            self.balance -= amount

    def deposit(self, amount):
        '''
        Deposits a given amount into the balance.
        Validates that the amount is positive.
        '''
        if amount < 0:
            print('Deposit amount must be a positive value.')
        else:
            self.balance += amount

    def __str__(self):
        '''
        Returns a user-friendly string representation of the account.
        '''
        return f'Account Name: {self.name}\nAccount Balance: {self.balance}'