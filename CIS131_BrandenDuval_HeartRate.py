# Target Heart-Rate Calculator
# Branden Duval
# January 27, 2025
# This program calculates a user's target heart rate given their age

# declare variables
userAge = 0
maxHeartRate = 0
targetHeartRateMin = 0
targetHeartRateMax = 0

# function to calculate the users heart rate
def calculateHeartRate():
    while True: # santizes inputs until user enters a valid value
        try:
            userAge = int(input('Please enter your age to begin: ')) # asks the user for their age
        except ValueError: # ensures that strings and floats cant be entered
            print('Please enter a valid age in the form of a digit.') 
        if userAge < 0 or userAge > 123: # ensure that realistic ages can be input
            print('Fun fact: the verified oldest living person lived to be 122 years old.') # Jeanne Calment 1875 - 1997 RIP
            print('Please enter a valid age in the form of a digit.')
        else:
            break
    maxHeartRate = 220 - userAge # formula courtesy of the American Heart Association
    print('Your maximum heart-rate is: ', maxHeartRate) # prints the result of the users maximum heart rate
    targetHeartRateMin = maxHeartRate * .5 # finds the lowest possible target heart rate
    targetHeartRateMax = maxHeartRate * .85 # finds the highest possible target heart rate
    print('Your target Heart-Rate range is anywhere from ', targetHeartRateMin, ' to', targetHeartRateMax) # prints the results of the target heart rate
    
    return 

# calls the heart rate calculator function 
calculateHeartRate()