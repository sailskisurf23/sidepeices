import random


def lets_play():
    """Ask the user if they want to play.
    Ask User whether they want to play against a person or computer.
    Exit program if they don't want to play."""
    playagain = 'y'
    while playagain == 'y':
        playagain = input("Would you like to play a game of Tic Tac Toe? (y/n): ")
        personorcomp = 1
        if playagain == 'y':
            print("Yay let's play!")
            pvp_pvc = int(input("Would you like to play a person or a computer? (Enter '1' for a person, '2' for a computer): "))
            if pvp_pvc == 1 or pvp_pvc == 2:
                return pvp_pvc
            else:
                print("Error: Please enter 'y' to play again or 'n'")
                lets_play()
        elif playagain == 'n':
            print("Goodbye!")
            sys.exit()
            break
        else:
            print("Error: Please enter 'y' to play again or 'n'")
            lets_play()

def draw_board(board,turn,XorO):
    """Prints the board.
    board: list of lists
    turn: integer
    XorO: string"""
    print(f"Turn: {turn} ; Player: {XorO}")
    print(str(board[0][0]) + " | " + str(board[0][1]) + " | " + str(board[0][2]))
    print("---------")
    print(str(board[1][0]) + " | " + str(board[1][1]) + " | " + str(board[1][2]))
    print("---------")
    print(str(board[2][0]) + " | " + str(board[2][1]) + " | " + str(board[2][2]))

def whose_turn(turn):
    """Returns string 'XorO' which who's turn it is. X always goes first.
    turn: integer"""
    XorO = 'X'
    if turn % 2 == 0:
        XorO = 'O'
    return XorO

def freesquare(board):
    """Returns list of unplayed squares.
    board: list of lists"""
    freesquares = []
    for ls in board:
        for x in ls:
            if x != 'X' and x != 'O':
                freesquares.append(x)
    return freesquares

def player_move():
    """Returns integer value of the user's intended play.
    squareplayed: integer"""
    squareplayed = int(input("Which square would you like to play? (Enter integer 1-9): "))
    return squareplayed

def play_square(squareplayed, board, XorO):
    """Updates board based on the square played.
    squareplayed: integer
    board: list of lists
    XorO: string"""
    if squareplayed == 1:
        board[0][0] = XorO
    elif squareplayed == 2:
        board[0][1] = XorO
    elif squareplayed == 3:
        board[0][2] = XorO
    elif squareplayed == 4:
        board[1][0] = XorO
    elif squareplayed == 5:
        board[1][1] = XorO
    elif squareplayed == 6:
        board[1][2] = XorO
    elif squareplayed == 7:
        board[2][0] = XorO
    elif squareplayed == 8:
        board[2][1] = XorO
    elif squareplayed == 9:
        board[2][2] = XorO
    else:
        raise RuntimeError("")
        print("play_square ERROR")
    return board

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

#AI block
def computer_move(freesquares,board,winner,XorO):
    """Returns an integer with the computer's move
    freesquares: list"""
    winmove = winning_move(freesquares,board,winner,XorO)
    randmove = random_move(freesquares)
    if winmove > 0:
        comp_move = winmove
    else:
        comp_move = randmove
    return comp_move

def random_move(freesquares):
    """Returns an integer by randomly selecting from available squares.
    freesquares: list"""
    randomindex = random.randint(0,len(freesquares)-1)
    randmove = freesquares[randomindex]
    return randmove

def winning_move(freesquares,board,winner,XorO):
    """Returns an integer by selecting a square which would result in computer win (computer is 'O')"""
    winmove = 0
    for square in freesquares:

        # either pass a copy of the board to play_square ...
        from copy import deepcopy
        copyboard = deepcopy(board)
        boardposs = play_square(square,copyboard,XorO)
        won = (is_winner(boardposs,winner) == XorO)

        # .. or 'undo' the last move (not implemented)
        # undo_move(board, ... )

        if won:
            winmove = square
            return winmove
    return winmove

def prevent_win():
    """Returns an integer by selecting a square which would prevent player win (player is 'X')"""
    pass

king = """

     /\/\/\/\\
     |o*o*o*|
     |______|
     | o  o |
    C| _<_  |D
      \_-__/

      """

#Main Block
if __name__ == '__main__':

    #Ask user if they want to play; person or computer?
    pvp_pvc = lets_play()

    #Initialize
    if True:
        turn = 1
        XorO = 'X'
        winner = 'blank'
        board = [[1,2,3],[4,5,6],[7,8,9]]

    #pvp game
    if pvp_pvc == 1:
        while turn <= 9 and winner == 'blank':
            XorO = whose_turn(turn)
            draw_board(board,turn,XorO)
            freesquares = freesquare(board)
            squareplayed = player_move()

            if squareplayed in freesquares:
                print(f"You played {squareplayed}")
            else:
                print(f"Error, you played {squareplayed}, enter a valid square")
                squareplayed = player_move()

            board = play_square(squareplayed,board,XorO)
            winner = is_winner(board,winner)
            turn += 1
        draw_board(board,turn,XorO)

        if winner == 'blank':
            print("It's a tie!")
        else:
            print("")
            print(f"{winner} is the KING OF THE WORLD!!!")
            print(king)

    #pvc game
    elif pvp_pvc == 2:
        while turn <= 9 and winner == 'blank':

            if turn % 2 != 0:
                XorO = whose_turn(turn)
                draw_board(board,turn,XorO)
                freesquares = freesquare(board)
                squareplayed = player_move()
                if squareplayed in freesquares:
                    print(f"You played {squareplayed}")
                else:
                    print(f"Error, you played {squareplayed}, enter a valid square")
                    squareplayed = player_move()
                board = play_square(squareplayed,board,XorO)
                winner = is_winner(board,winner)
                turn += 1

            elif turn % 2 == 0:
                XorO = whose_turn(turn)
                draw_board(board,turn,XorO)
                freesquares = freesquare(board)
                squareplayed = computer_move(freesquares,board,winner,XorO)
                print(f"Computer plays square = {squareplayed}")
                board = play_square(squareplayed,board,XorO)
                winner = is_winner(board,winner)
                turn += 1

        draw_board(board,turn,XorO)
        if winner == 'blank':
            print("It's a tie!")
        else:
            print("")
            print(f"{winner} is the KING OF THE WORLD!!!")
            print(king)
