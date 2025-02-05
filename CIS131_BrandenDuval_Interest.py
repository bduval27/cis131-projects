# 7% interest calculator
# Branden Duval
# January 27, 2025
# This program calculates interest at 7% with a $1000 principle and shows the amount after 10, 20, 30 years and can be easily changed if needed

'''
compound interest rate formula
p = principle
r = rate
n = number of years
a = amount
'''

# Declare variables
p = 1000 # principle amount invested
r = .07  # current interest rate

# the calculator function
def investment(p, r, n):  
    a = p * (1 + r) ** n # the compound interest formula of a = p(1 + r)^n   

    return a

# shows the results to the user
print(f'Your investment after 10 years: {investment(p, r, 10):.2f}') # shows the total after 10 years
print(f'Your investment after 20 years: {investment(p, r, 20):.2f}') # shows the total after 20 years
print(f'Your investment after 30 years: {investment(p, r, 30):.2f}') # shows the total after 30 years