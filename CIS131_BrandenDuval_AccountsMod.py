'''
script: Modify Accounts Class to have read-only properties
action: ensures that the name and balance of the account are read-only
author: Branden Duval
date: 03/03/2025
'''

from decimal import Decimal

class Account:
    '''Account Class for maintaining a bank account balance.'''

    def __init__(self, name, balance):
        '''Initialize an Account object.'''
        
        # if balance is less than 0.00, raise an exception
        if balance < Decimal('0.00'):
            raise ValueError('Initial balance must be >= to 0.00.')

        self._name = name # added an _ to make the variable private
        self._balance = balance # added an _ to make the variable private

    # getter for name to make it read-only
    @property
    def name(self):
        '''
        action: makes the name off the account read-only
        input:  none
        output: none
        return: account name
        '''
        return self._name

    # getter for balance to make it read-only   
    @property
    def balance(self):
        '''
        action: makes the balance of the account read-only
        input:  none
        output: none
        return: account balance
        '''
        return self._balance

    def deposit(self, amount):
        '''Deposit money to the account.'''

        # if amount is less than 0.00, raise an exception
        if amount < Decimal('0.00'):
            raise ValueError('Amount must be positive.')
        
        self.balance += amount

    def withdraw(self, amount):
        '''Withdraw money from the account.'''

        # if the amount is greater than balance, raise an exception
        if amount > self._balance:
            raise ValueError('Amount must be <= to balance.')
        elif amount < Decimal('0.00'):
            raise ValueError('Amount must be positive.')
        
        self.balance -= amount