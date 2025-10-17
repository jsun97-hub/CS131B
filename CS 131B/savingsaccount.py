'''
Program:  savingsaccount.py 
Programmer: Jeffrey Sun
Date: 07/21/2025
Description:  This program defines the SavingsAccount class, which is a subclass of the account
class and has an additional 'rate' attribute. The SavingsAccount class also has a calculate_interest
function, which multiplies the rate and balance values.
'''
from account import Account
class SavingsAccount(Account):
    '''
    Represents a savings account, a specialized version of an Account.
    Includes an interest rate and a method to calculate interest earned.
    '''
    def __init__(self, name, balance, rate):
        '''
        Initializes a SavingsAccount object.
        '''
        super().__init__(name, balance)
        self.setRate(rate)

    def getRate(self):
        '''
        Returns the interest rate for the account.
        '''
        return self.rate

    def setRate(self, rate):
        '''
        Sets or updates the interest rate for the account.
        Validates that the rate is between 0 and 1.
        '''
        if rate < 0 or rate > 1:
            print('Rate must be a positive value between 0 and 1. Setting rate to 0.')
            self.rate = 0
        else:
            self.rate = rate

    def calculate_interest(self):
        '''
        Calculates the interest earned on the current balance.
        '''
        return self.balance * self.rate

    def __str__(self):
        '''
        Returns a user-friendly string representation of the savings account,
        including the interest rate.
        '''
        baseString = super().__str__()
        return f'{baseString}\nInterest Rate: {self.rate}'