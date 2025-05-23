'''
script: Recursive Fibonacci Modification
action: modifies section 11.4's recursive fibonacci function to keep track of total nuimber of function calls
author: Branden Duval
date: 03/30/2025
'''

# fibonacci function itself
def fibonacci(n):
    if n in (0, 1): # base cases
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# counter initialized to 0
counter = 0

# for loop that displays the values of fibonacci from 0 - 40
for n in range(41):
    counter += 1 # adds 1 to the counter everytime a fibonacci function is displayed because trying it any other way results in the terminal endlessly displaying 0 for some reason
    if n % 10 == 0: # if the number can be neatly divided by 10 
        print(f'\nCall {counter}:\nFibonacci({n}) = {fibonacci(n)}\n') # prints the results and the calls called for calls that are multiples of 10
    else:
        print(f'Fibonacci({n}) = {fibonacci(n)}') # prints the results regardless