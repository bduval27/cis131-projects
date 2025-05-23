'''
script: Recursive Power Function
action: uses recursion to display exponentation of a number from user input
author: Branden Duval
date: 03/31/2025
'''

# initializes the base and the power as user inputs
base = int(input('Please enter a base integer: ')) 
power = int(input('Please enter the power the base should be raised to: '))

# passes base and power into the exponentation function
def exponentation(base, power):
    if power < 1: # will not accept negative numbers
        raise ValueError('Please enter a power greater than or equal to 1.') # tells the user that negative numbers are not accepted
    elif power == 1: # base case, will terminate when power is equal to 1
        return base
    else:
        return base * exponentation(base, power - 1) # recursive statement to solve the exponentation problem

# input sanitization while loop   
while True:
    try:
        print(f'{base} raised to the power of {base} ({base}^{power}) is equal to: {exponentation(base, power)}') # prints the results
        break # and then stops
    except:
        print('Please enter a non-negative integer') # prompts the user to try again with a positive number
        # and then repeats the user input process
        base = int(input('Please enter a base integer: ')) 
        power = int(input('Please enter the power the base should be raised to: '))