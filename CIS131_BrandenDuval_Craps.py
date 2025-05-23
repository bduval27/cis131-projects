'''
script: Craps script mod
action: modifies the Craps script from fig04_02 to roll one million times and report back with the results
author: Branden Duval
date: 02/11/2024'''

# necessary module
import random

# global variables and dictionary
games_won = 0
games_lost = 0
wins_roll_dict = {}

def craps_game():
    '''
    New function to loop the program one million times
    
    action: makes it possible for the script to run more than once
    input: none
    output: none (print statements commented out)
    return: whether a roll is won or lost 
    '''

    # adds a roll every loop
    number_of_rolls = 1

    def roll_dice():
        """Roll two dice and return their face values as a tuple"""
        die1 = random.randrange(1, 7)
        die2 = random.randrange(1, 7)
        return (die1, die2) # pack die face values into a tuple

    def display_dice(dice):
        """Display one roll of the two dice."""
        die1, die2 = dice # unpack the typle in to variables die1 and die2
        # print(f'Player rolled {die1} + {die2} = {sum(dice)}')

    die_values = roll_dice() # first roll
    display_dice(die_values)

    # determine game status and point, based on first roll
    sum_of_dice = sum(die_values)

    if sum_of_dice in (7, 11): # win
        game_status = 'WON'
    elif sum_of_dice in (2, 3, 12): # lose
        game_status = 'LOST'
    else: # remember point
        game_status = 'CONTINUE'
        my_point = sum_of_dice
        # print('Point is', my_point)

    # continue rolling until player wins or loses
    while game_status == 'CONTINUE':
        number_of_rolls += 1
        die_values = roll_dice()
        display_dice(die_values)
        sum_of_dice = sum(die_values)

        if sum_of_dice == my_point: # win by making point
            game_status = 'WON'
        elif sum_of_dice == 7: # lose by rolling 7
            game_status = 'LOST'

    # display "wins" or "loses" message
    if game_status == 'WON':
        # print('Player wins')
        return 1, number_of_rolls # 1 == win
    else:
        # print('Player loses')
         return 0, number_of_rolls # 0 == loss
    
# new for loop to run for 1,000,000 games     
for i in range(1_000_000):
    game_status, number_of_rolls = craps_game()

    if game_status == 1:
        games_won += 1
    else:
        games_lost += 1

# updates the dictionary with the games played and dice rolled
    if number_of_rolls in wins_roll_dict:
        wins_roll_dict[number_of_rolls] += 1
    elif number_of_rolls not in wins_roll_dict:
        wins_roll_dict[number_of_rolls] = 1

# cumulative win percentage
cumulative_win_sum = 0

# turns values into percents
for k, v in sorted(wins_roll_dict.items()):
    percent_of_games_won = (v / 1_000_000) * 100
    cumulative_win_sum += percent_of_games_won
    wins_roll_dict[k] = [percent_of_games_won, cumulative_win_sum]

# print statements to show percentages of games won/lost
print(f'Percentage of wins: {(games_won / 1_000_000) * 100}%')
print(f'Percentage of losses: {(games_lost / 1_000_000) * 100}%')
print('Rolls\ton this roll\tof games resolved')

# for loop to prin the results of each roll
for k, v in sorted(wins_roll_dict.items()):
    # print('Rolls\ton this roll\tof games resolved')
    print(f'{k}\t{v[0]:.2f}\t\t{v[1]:.2f}')