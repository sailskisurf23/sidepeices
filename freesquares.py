def freesquares(board):
    freesquares = []
    for ls in board:
        for x in ls:
            if x != 'X' and x != 'O':
                freesquares.append(x)
    return freesquares

board = [[1,2,'X'],[4,'O',6],[7,8,9]]
print(freesquares(board))
