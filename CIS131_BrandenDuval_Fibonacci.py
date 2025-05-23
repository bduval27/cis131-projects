'''
script: Recursive Fibonacci Modification
action: modifies section 11.4's recursive fibonacci function to keep track of total nuimber of function calls
author: Branden Duval
date: 03/30/2025
'''

# fibonacci function
def fib(n):
    if n in (0, 1): # base cases 
        return(n, 1)
    else:
        # fib num and count from n - 1 and n - 2
        (fibNum1, fibCount1) = fib(n - 1)
        (fibNum2, fibCount2) = fib(n - 2)
        
        # sums the fi nums and counts and adds 1
        fibNum = fibNum1 + fibNum2
        fibCount = fibCount1 + fibCount2 + 1
        
        # returns fibNum and fibCount
        return(fibNum, fibCount)
    
# for loop starting at 10 and only doing every 10 fibonacci numbers up to 40 (for completeness)
for n in range(10, 41, 10):
    if n != 0: # does not start at 0
        fibNum, fibCount = fib(n) 
        print(f'Fibonacci({n}) = {fibNum} was recursively called {fibCount} times') # displays the results and how many times an increment of 10 was recursively called