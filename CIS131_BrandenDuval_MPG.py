'''
    script: Miles Per Gallon calculator
    action: a. asks for miles driven
            b. asks for gallons used
            c. calculates miles per gallon for one trip
            d. calculates the over all miles per gallon from the entirety of the data entered
    author: Branden Duval
    date: 02/02/2025
'''

# global variables
gallonsUsed = 0
milesDriven = 0
milesPerGallon = 0

# main function
def overallMPG():
    '''
    Calculates the average miles per gallon for a single tank and finally displays average mpg for all tanks entered
    
    action: prompts user to enter the values related to their miles and gallons per tank
            adds the numbers together
            returns the overall miles per gallon
    input:  none
    output: prints out a single tanks miles per gallon
    return: overallMPG
    '''
    
    # local variables
    totalMPG = 0
    counter = 0

    # the meat of the function
    while True: # first while loop for sentinel value
        while True: # second while loop for input sanitization
            try:
                gallonsUsed = float(input('Enter the gallons used (-1 to end): '))
                break
            except ValueError: # will not except strings
                print('Please enter a valid number or -1 to end.') # firmly prompts the user
        if gallonsUsed == -1: # sentinel value
            break
        milesDriven = int(input('Enter the miles driven: '))
        if milesDriven < 0: # can't drive negative miles
            print('Please enter a positive number.') # firmly prompts the user
        else:
            milesPerGallon = milesDriven / gallonsUsed # calculates miles per gallon as M/G
            totalMPG += milesPerGallon # adds all MPG after each pass
            print(f'The miles/gallon used for this tank was {milesPerGallon:.6f}')
            counter += 1 # counts how many times the program has looped

    return totalMPG / counter # returns the average MPG for all tanks entered
        
print(f'The overall average miles/gallon was {overallMPG():.6f}') # prints the results of the entered data