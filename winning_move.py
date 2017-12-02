def is_winner(b,winner):
    """Returns string containing the winner if a player has already won the game.
    b is for 'board': list of lists
    winner: string"""

    #b is for board
    XOlist = ['X','O']
    for i in XOlist:
        #Rows
        if b[0][0] == i and b[0][1] == i and b[0][2] == i:
            winner = i
        if b[1][0] == i and b[1][1] == i and b[1][2] == i:
            winner = i
        if b[2][0] == i and b[2][1] == i and b[2][2] == i:
            winner = i
        #Columns
        if b[0][0] == i and b[1][0] == i and b[2][0] == i:
            winner = i
        if b[0][1] == i and b[1][1] == i and b[2][1] == i:
            winner = i
        if b[0][2] == i and b[1][2] == i and b[2][2] == i:
            winner = i
        #Diagonals
        if b[0][0] == i and b[1][1] == i and b[2][2] == i:
            winner = i
        if b[0][2] == i and b[1][1] == i and b[2][0] == i:
            winner = i
    return winner

def play_square(squareplayed, b, XorO):
    """Updates board based on the square played.
    squareplayed: integer
    board: list of lists
    XorO: string"""
    if squareplayed == 1:
        b[0][0] = XorO
    elif squareplayed == 2:
        b[0][1] = XorO
    elif squareplayed == 3:
        b[0][2] = XorO
    elif squareplayed == 4:
        b[1][0] = XorO
    elif squareplayed == 5:
        b[1][1] = XorO
    elif squareplayed == 6:
        b[1][2] = XorO
    elif squareplayed == 7:
        b[2][0] = XorO
    elif squareplayed == 8:
        b[2][1] = XorO
    elif squareplayed == 9:
        b[2][2] = XorO
    else:
        print("play_square ERROR")
    return b

def winning_move(freesquares,board,winner,XorO):
    """Returns an integer by selecting a square which would result in computer win (computer is 'O')"""
    winmove = 0
    for square in freesquares:
        boardposs = board
        boardposs = play_square(square,board,XorO)
        if is_winner(boardposs,winner) == XorO:
            winmove = square
            return winmove
    return winmove

freesquares = [2,3,4,5,6,7,8,9]
boardglobal = [['X',2,3],[4,5,6],[7,8,9]]
winner = 'blank'
XorO = 'O'

print(winning_move(freesquares,boardglobal,winner,XorO))
print(boardglobal)
