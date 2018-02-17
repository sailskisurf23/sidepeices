import random, sys
from copy import deepcopy


def start_game():
    playagain = 'y'
    while playagain == 'y':
        playagain = input("Would you like to play a game of Tic Tac Toe? (y/n): ")
        if playagain == 'y':
            print("Yay let's play!")
            pvp_pvc = int(input("""Would you like to play a person or a computer? 
            (Enter '1' for a person, '2' for a computer):""" ))
            XorO = input("Would you like to play as X or O? (Enter 'X' or 'O'):")
            if (pvp_pvc == 1 or pvp_pvc == 2) and (XorO == 'X' or XorO == 'O'):
                return pvp_pvc, XorO
            else:
                print("Error, invalid entry: Please enter 'y' to play again or 'n'")
                start_game()
        elif playagain == 'n':
            print("Goodbye!")
            sys.exit()
        else:
            print("Error, invalid entry: Please enter 'y' to play again or 'n'")
            start_game()

class TTTGame():
    """Keeps track of the game:
    Whose turn"""

    def __init__(self,turn=1,XorO='X',player='X'):
        self.turn = turn
        self.XorO = XorO
        self.player = player

    def whose_turn(self):
        pass

    def get_player_move(self):
        pass

    def get_computer_move(self):
        pass


class TTTBoard():
    """Keeps track of what the board is doing / looks like"""

    def __init__(self, board=list(range(1, 10)), turn='1'):
        self.board = board
        self.turn = turn

    def __str__(self):
        return self.draw_board()

    def draw_board(self, turn=1, XorO='O'):
        return (f"""
        Turn: {turn} ; Player: {XorO} \n
        {self.board[0]} | {self.board[1]} | {self.board[2]}
        ---------\n
        {self.board[3]} | {self.board[4]} | {self.board[5]}
        ---------\n
        {self.board[6]} | {self.board[7]} | {self.board[8]}
        """)

    def play_square(self, squareplayed=1, XorO='O'):
        if squareplayed == 1:
            self.board[0] = XorO
        elif squareplayed == 2:
            self.board[0] = XorO
        elif squareplayed == 3:
            self.board[0] = XorO
        elif squareplayed == 4:
            self.board[0] = XorO
        elif squareplayed == 5:
            self.board[0] = XorO
        elif squareplayed == 6:
            self.board[0] = XorO
        elif squareplayed == 7:
            self.board[0] = XorO
        elif squareplayed == 8:
            self.board[0] = XorO
        elif squareplayed == 9:
            self.board[0] = XorO
        else:
            raise RuntimeError("")
        return self.board


pvp_pvc, XorO = start_game()
