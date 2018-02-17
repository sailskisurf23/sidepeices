from copy import deepcopy

board = [ [3, 0, 1],
          [3, 0, 1],
          [0, 2, 1],
          [0, 2, 0] ]

attacks = [[2, 1], [2, 2], [ 3, 2], [3, 3],[3, 1]]

def boats_init(board):
    boats_init = set()
    for x in board:
        for i in x:
            if i == 1:
                boats_init.add('boat1')
            if i == 2:
                boats_init.add('boat2')
            if i == 3:
                boats_init.add('boat3')
    return boats_init

def execute_attacks(board, attacks):
    newboard = deepcopy(board)
    for attack in attacks:
        newboard[-attack[1]][attack[0]-1] = 'X'
    return newboard

def boats_sunk(board, newboard):
    boats_new = set()
    for x in newboard:
        for i in x:
            if i == 1:
                boats_new.add('boat1')
            if i == 2:
                boats_new.add('boat2')
            if i == 3:
                boats_new.add('boat3')
    boats_sunk = [x for x in boats_init(board) if x not in boats_new]
    return boats_sunk

def boats_damaged(board, newboard, attacks):
    boats_hit = set()
    for attack in attacks:
        if board[attack[1]-1][attack[0]-1] == 1:
            boats_hit.add('boat1')
        if board[attack[1]-1][attack[0]-1] == 2:
            boats_hit.add('boat2')
        if board[attack[1]-1][attack[0]-1] == 3:
            boats_hit.add('boat3')
    boats_damaged = [x for x in boats_hit if x not in boats_sunk(board,newboard)]
    return boats_damaged

def boats_not_touched(board, newboard, attacks):
    return [x for x in boats_init(board) if x not in boats_damaged(board, newboard, attacks)
    and x not in boats_sunk(board, newboard)]

def points(board, newboard, attacks):
    points = 0
    points += len(boats_sunk(board, newboard))
    points += len(boats_damaged(board, newboard, attacks))/2
    points -= len(boats_not_touched(board, newboard, attacks))
    return points

def damaged_or_sunk (board, attacks):
    newboard = execute_attacks(board, attacks)
    result = {}
    result['sunk'] = len(boats_sunk(board, newboard))
    result['damaged'] = len(boats_damaged(board, newboard, attacks))
    result['not_touched'] = len(boats_not_touched(board, newboard, attacks))
    result['points'] = points(board, newboard, attacks)
    return result






print(attacks)
print(board)
print(execute_attacks(board,attacks))
print(damaged_or_sunk(board,attacks))
