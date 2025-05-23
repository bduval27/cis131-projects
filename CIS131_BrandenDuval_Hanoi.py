'''
script: Towers of Hanoi
action: displays the least amount of moves to complete the Towers of Hanoi game
author: Branden Duval
date:   04/07/2025
'''

# main function
def towersOfHanoi(n, peg1, peg2, peg3): # takes in n as the number of disks, peg 1 as the starting peg, peg 2 as the final peg, and peg 3 as the temporary holding peg
    '''
    Game function that displays the steps needed to complete the Tower of Hanoi game
    
    action: displays the least amount of steps needed to complete the Tower of Hanoi game
    input:  n as number of disks, pegs 1, 2, and 3
    output: prints the results
    return: none
    '''

    if n == 0: # base case
        print(f'{peg1} --> {peg2}') # if the base case is reached, display this (at the end)
    else: # if the base case is not hit display this
        towersOfHanoi(n - 1, peg1, peg3, peg2) 
        print(f'{peg1} --> {peg2}') 
        towersOfHanoi(n - 1, peg3, peg2, peg1)

n = 2 # set as 2 because I had set the base case as 0 first and n == 0 looks nicer to me
towersOfHanoi(n, '1', '3', '2') # calls the game function with
