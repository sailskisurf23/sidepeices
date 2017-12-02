#1. Write a function that rolls two sets of dice to model players playing a game with dice.
#It will accept two arguments, the number of dice to roll for the first player, and the number of dice to roll
#for the second player. Then, the function will do the following:

 #* Model rolling the appropriate number of dice for each player.
 #* Sum the total values of the corresponding dice rolls.
 #* Print which player rolled the higher total.
 #* Return the total sum of each players rolls in a tuple.


#Add functionality to Game
    #Adjust game for any number of players
    #Ask user how many players there are
    #For each player ask how many rolls they get and then print each roll along with their sum
    #After last player, print winner(s)
    #Ask user if they want to play again

import random
import sys

def rolls_result(numrolls):
    '''Roll a 6 sided die 'numrolls' times, returns sum of rolls and list of results'''
    sumrolls = 0
    result_list = []
    for i in range(numrolls):
        result = random.randint(1,6)
        sumrolls += result
        result_list.append(result)
    return sumrolls, result_list

def dice(playerscores):
    '''Input the score for each player, return list of winner(s)'''
    maxscore = max(playerscores)
    winnerlist = []
    for i in range(len(playerscores)):
        if playerscores[i] == maxscore:
            winnerlist.append(f"Player{i+1}")
    return winnerlist

def winnerstring(winnerlist):
    '''Input the list of winners, return a string exclaiming the winner1(s)'''
    if len(winnerlist) == 1:
        return f"{winnerlist[0]} is the winner!!!"
    elif len(winnerlist) > 1:
        winstring = " are winners!!!"
        for i in winnerlist:
            winstring = i + ", " + winstring
        return winstring
    else:
        return "Something's wrong, there are no winners..."

if __name__ == '__main__':
    #Ask user if they want to play ()
    playagain = 'y'
    while playagain == 'y':
        playagain = input("Would you like to play a game of dice? (y/n): ")

        if playagain == 'n':
            print("Goodbye!")
            sys.exit()

        #Ask user for number of players
        num_of_players = int(input("Input number of players: "))
        print("Thanks!")

        #Ask user how many times each player rolls;
        #Show them their score
        numrollslist = []
        playerscores = []
        for x in range(1,num_of_players+1):
            numrolls = int(input(f"Input number of times Player{x} rolls: "))
            numrollslist.append(numrolls)
            score = rolls_result(numrolls)
            playerscores.append(score[0])
            print(score)

        #Determine winners
        winnerlist = dice(playerscores)

        #Print list of winners
        print("The scores are: " + str(playerscores))
        print(winnerstring(winnerlist))
        print("")
