'''
Program:  checkingaccount.py 
Programmer: Jeffrey Sun
Date: 07/21/2025
Description: This program defines the CheckingAccount class, which is a subclass of the Account
class and has an additional 'fee' attribute. The CheckingAccount class also overrides the Account
class' withdraw and deposit methods to subtract the fee from the balance if the transaction is
successful. 
'''
from account import Account
class CheckingAccount(Account):
    '''
    Represents a checking account, a specialized version of an Account.
    Includes a per-transaction fee and overrides deposit/withdraw methods.
    '''
    def __init__(self, name, balance, fee):
        '''
        Initializes a CheckingAccount object.
        '''
        super().__init__(name, balance)
        self.setFee(fee)

    def getFee(self):
        '''
        Returns the transaction fee for the account.
        '''
        return self.fee

    def setFee(self, fee):
        '''
        Sets or updates the transaction fee for the account.
        Validates that the fee is not negative.
        '''
        if fee < 0:
            print('Fee must be a positive value. Setting fee to 0.')
            self.fee = 0
        else:
            self.fee = fee

    def withdraw(self, amount):
        '''
        Withdraws a given amount, plus a transaction fee, from the balance.
        Delegates the transaction and validation to the parent class.
        '''
        totalAmount = amount + self.fee
        super().withdraw(totalAmount)

    def deposit(self, amount):
        '''
        Deposits a given amount and subtracts a transaction fee.
        Validates that the final balance will not be negative.
        '''
        if self.balance + amount - self.fee < 0:
            print('Total balance after deposit must be greater than the fee.')
        else:
            super().deposit(amount)
            self.balance -= self.fee
            
    def __str__(self):
        '''
        Returns a user-friendly string representation of the checking account,
        including the transaction fee.
        '''
        baseString = super().__str__()
        return f'{baseString}\nTransaction Fee: {self.fee}'