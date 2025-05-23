'''
script: Telephone Number Game
action: generates random strings of letters based on a given phone number
author: Branden Duval
date: 02/10/2025
'''

def getLetterCombo():
    '''
    The meat of the program
    
    action: prompts the user for a 7 character long number
            throws the number into an empty list
            passes the new list onto the next function
    input:  user phone number
    output: user phone number
    return: returns the list of possible letter combos
    '''
    
    # dictionary of numbers to letters
    numberDict = {
        '2': ['A', 'B', 'C'],
        '3': ['D', 'E', 'F'],
        '4': ['G', 'H', 'I'],
        '5': ['J', 'K', 'L'],
        '6': ['M', 'N', 'O'],
        '7': ['P', 'R', 'S'],
        '8': ['T', 'U', 'V'],
        '9': ['W', 'X', 'Y'],
    }

    userPhoneNumber2 = [] # empty list for the user input 
    userPhoneNumber = input('Please enter a 7 character long phone number: ')
    if len(userPhoneNumber) != 7: # makes sure that the user input is the right length
        print('Please enter a phone number that is 7 characters in length.')
    for digit in userPhoneNumber:
        if digit not in numberDict: # prompts the user to try again
            print('Please exclude hyphens, area codes, and numbers 0 or 1.')
            return
        userPhoneNumber2.append(numberDict[digit])

    return cartesian_product(*userPhoneNumber2)
    

def cartesian_product(*args): # takes in the letters based off of what numbers the user entered as a list of lists
    '''
    Function used to combine letter combinations
    
    action: takes the letters from the dictionary and combines them into as many combinations as possible
    input: userPhoneNumber2
    output: print statements for results
    return: the list of letter combinations
    '''
    
    product = args[0] # sets product to the first item in the list

    for arg in args[1:]: # for every list AFTER the first list
        temp = [] # creates an empty temporary list
        for p in product: # for every letter IN the work done thus far starting with the first possible letter
            for a in arg: # for every letter in this current list
                temp.append(p + a) # adds the letter from the work done thus far and adds the letter from the current list together
        product = temp # updates product with the work done thus far with each loop 
    
    return product # returns the new list of letter combinations

result = getLetterCombo() # set new variable result to the first function 
print('There are ', len(result), 'possible letter combinations for this number!') # prints the number of results by measuring the length of variable result
print(result) # prints the results