'''
script: Telephone Number Game
action: generates random strings of letters based on a given phone number and writes it to a plain text file
author: Branden Duval
date: 02/25/2025
'''

# new function to open a plain text file to write to
with open('LetterGenerator.txt', mode= 'w') as phoneNumber:
    '''
    Opens a plain text file to write the results to

    action: opens a plain text file to write
    input:  the results from the functions within
    output: a text file including the results and number of results from the program
    return: none
    '''

    # first function to prompt user and sanitize the input
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
            if digit not in numberDict: # if the digit is not listed or defined within the dictionary 
                print('Please exclude hyphens, area codes, and numbers 0 or 1.') # an error message is displayed
                return
            userPhoneNumber2.append(numberDict[digit]) # creates a list of lists

        return word_generator(*userPhoneNumber2) # passes userPhoneNumber2 to the word_generator function and returns its results

    # second function used to translate the phone number provided
    def word_generator(*args):
        '''
        This function is used to translate the digits in userPhoneNumber2 to their corresponding letters within the dictionary

        action: translates a phone number into various letter combinations
        input:  userPhoneNumber2 as *args
        output: results that is printed and displayed to the user
        return: product as a list of letter combinations
        '''

        product = [] # creates an empty list to store the letter combinations

        for firstDigit in args[0]: # for the first digit in userPhoneNumber2
            for secondDigit in args[1]: # for the second digit in userPhoneNumber2
                for thirdDigit in args[2]: # for the third digit in userPhoneNumber2
                    for fourthDigit in args[3]: # for the fourth digit in userPhoneNumber2
                        for fifthDigit in args[4]: # for the fifth digit in userPhoneNumber2
                            for sixthDigit in args[5]: # for the sixth digit in userPhoneNumber2
                                for seventhDigit in args[6]: # for the seventh and final digit in userPhoneNumber2
                                    product.append(firstDigit + secondDigit + thirdDigit + fourthDigit + fifthDigit + sixthDigit + seventhDigit) # adds all the digits together and then goes back to the first for loop to start again for a new letter combination
                                    for word in product: # for each letter combination
                                        phoneNumber.write(f'{word}\n') # write it as its own word on its own line

        return product # returns the results 

    result = getLetterCombo() # set new variable result to the first function 
    print(f'Success! {len(result)} words written to file "LetterGenerator.txt!"') # gives the user confirmation that the script performed successfully