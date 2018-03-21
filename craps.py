# Create a function to simulate the probability of a given number of games of craps.
#
# The Rules:
# You roll two 6-sided dice.
# If the roll adds up to 2, 3, or 12, the player loses that game.
# If the roll adds up to 7 or 11, the player wins.
# If the roll adds up to any other number, the player re-rolls until either:
#   1) The first roll amount is rolled again, which is a win
#   2) A 7 is rolled, which is a loss
#
# Return the win percentage.

import random as rd
import numpy as np

def roll():
    return rd.randint(1,7) + rd.randint(1,7)

def play_craps():
    roll1 = roll()
    if roll1 in [2,3,12]:
        return False
    elif roll1 in [7,11]:
        return True
    else:
        while True:
            roll_again = roll()
            if roll_again == roll1:
                return True
            elif roll_again == 7:
                return False

def play_lotsa_craps(n=1000):
    return np.mean([play_craps() for i in range(n)])

print(roll())
