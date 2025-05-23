'''
script: Class Average: Writing Grades to a Plain Text File
action: lets the user input any number of grades until the sentinel value is input and saves it to a plain text file
author: Branden Duval
date: 02/24/2025
'''

with open('grades.txt', mode= 'w') as grades: # opens a file titled "grades" to write
    '''
    Function that enables the compiling of grades to a plain text file

    action: writes a plain text file given grade numbers
    input:  user determined grade numbers
    output: text file containing the entered grades
    return: none

    '''
    while True: # first while loop for sentinel value
        while True: # second loop for input sanitization
            try:
                grade = float(input('Please enter grade, -1 to end: ')) # prompts the user for an input, opted for a float in case of a decimal point grade
                break 
            except ValueError:
                print('Please enter a valid number grade.') # warns the user that strings are not accepted
        if grade == -1: # the sentinel value
            grades.write('\n')
            break # breaks if sentinel value entered
        if grade < 0 or grade > 100: # will not accept grades less than 0 or more than 100
            print('Invalid grade')
        else:
            grades.write(f'{grade:.2f}\n') # enters the grade into a plain text file