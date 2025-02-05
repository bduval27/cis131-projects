'''
script: Guess The Number
action: chooses a number and has the user guess what the number could be
author: Branden Duval
date: 02/03/2025
'''

# necessary library
import random # needed to choose a random number

# main game function
def guessTheNumber():
    '''
    The game itself a long with its rules

    action: compares user guesses to the actual chosen number
    input:  none
    output: informing the user of game status
    return: none
    '''

    # local variable
    counter = 0
    chosenNumber = random.randint(0, 1001) # chooses and stores the random number
    # print(f'{chosenNumber}') # used to test the program
    
    # while loop for input sanitization    
    while True:
        try:
            userGuess = int(input('Guess my number between 1 and 1000 with the fewest guesses. '))
            # first if condition if the user correctly guess under 10 tries    
            if userGuess == chosenNumber and counter > 10:
                print(f'Congratulations. You guessed the number in {counter} tries! You should be able to do better!')
                break
            # second if condition if the user takes more than 10 tries     
            if userGuess == chosenNumber and counter < 10:
                print(f'Congratulations. You guessed the number in {counter} tries! Either you know the secret or you got lucky!')
                break
            # third if condition to help narrow down the number    
            if userGuess > chosenNumber:
                print('Too high. Try again.')
                counter += 1 # adds to the attempts counter
            # fourth if condition to help narrow down the number
            if userGuess < chosenNumber:
                print('Too low. Try again.')
                counter += 1 # adds to the attempts counter
        except ValueError:
            print('Please enter a valid whole number between 1 and 1000.') # gotta reinforce the rules
    
    return

# greetings and farewells function
def startGame():
    '''
    Starts the game and asks if the user would like to play again

    action: greets the user and asks if they would like to play another round after their first round
    input:  none
    output: welcomes user and says goodbye
    return: none
    '''
    
    # says howdy
    print('Welcome!')
    
    # checks for sentinel value of any inputted lowercase "n" at the beginning of a string and if none are found, the game continues
    while True:
        guessTheNumber() # calls the main game function
        response = input('Wanna play again? Please enter Yes or No: ')
        if response[0].lower() == "n":
            break
    
    # says see ya
    print('Goodbye!')

# calls the start game function to loop
startGame() 