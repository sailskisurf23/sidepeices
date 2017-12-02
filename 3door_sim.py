#want to model simulation of 3 doors fallacy - Monty Hall problem

import random as r

def montysim(switch):
    doors = ['Door1','Door2','Door3']
    winning_door = r.choice(doors)
    first_pick = r.choice(doors)
    dummy_door_poss = [e for e in doors if e not in [winning_door, first_pick]]
    dummy_door = r.choice(dummy_door_poss)
    if switch == False:
        second_pick = first_pick
    else:
        second_pickls = [e for e in doors if e not in [dummy_door, first_pick]]
        second_pick = second_pickls[0]
    return second_pick == winning_door

def runsim(num,switch=False):
    contestants = 0
    winners = 0
    for x in range(num):
        contestants += 1
        result = montysim(switch)
        if result == True:
            winners +=1
    return contestants, winners

contestants, winners = runsim(1000,True)

print(f"Out of {contestants} contestants, there were {winners} winners")
