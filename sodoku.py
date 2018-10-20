import numpy as np
import math

def val_board(board):
    'return True if board is valid NxN board with sqroot(N) == int'
    return all([len(row) == len(board) for row in board]) and is_square(len(board))

def test_rows(board):
    'Returs True iff all columns in board are valid, else False'
    return all([checker(row) for row in board])

def test_columns(board):
    'Returs True iff all columns in board are valid, else False'
    board = transpose_lol(board)
    return all([checker(col) for col in board])

def test_lil_sqs(board):
    'Returs True iff all columns in board are valid, else False'
    npboard = np.array(board)
    root = int(math.sqrt(len(board)))
    lil_ls = []
    for i in range(root):
        for j in range(root):
            lil_sq = npboard[i*root:(i+1)*root,j*root:(j+1)*root].ravel()
            lil_ls.append(checker(lil_sq))
    return all(lil_ls)

def test_all(board):
    if val_board == False:
        return False
    return val_board(board) and test_rows(board) and test_columns(board) and test_lil_sqs(board)


def checker(unit):
    'Returns true iff a row, column or region is valid'
    return sorted(unit) == list(range(1, len(unit) + 1))

def transpose_lol(test_mat):
    'transpose list of lists'
    return [[row[i] for row in test_mat] for i in range(len(test_mat[0]))]

def is_square(integer):
    root = math.sqrt(integer)
    if int(root + 0.5) ** 2 == integer:
        return True
    else:
        return False




test_board1 = [
  [7,8,4,  1,5,9,  3,2,6],
  [5,3,9,  6,7,2,  8,4,1],
  [6,1,2,  4,3,8,  7,5,9],

  [9,2,8,  7,1,5,  4,6,3],
  [3,5,7,  8,4,6,  1,9,2],
  [4,6,1,  9,2,3,  5,8,7],

  [8,7,6,  3,9,4,  2,1,5],
  [2,4,3,  5,6,1,  9,7,8],
  [1,9,5,  2,8,7,  6,3,4]
]

test_board2 =   [[7, 8, 4, 1, 5, 9, 3, 2, 6],
                [5, 3, 9, 6, 7, 2, 8, 4, 1],
                [6, 1, 2, 4, 3, 8, 7, 5, 9],
                [9, 2, 8, 7, 1, 5, 4, 6, 3],
                [3, 5, 7, 8, 4, 6, 1, 9, 2],
                [4, 6, 1, 9, 2, 3, 5, 8, 7],
                [8, 7, 6, 3, 9, 4, 2, 1, 5],
                [2, 4, 3, 5, 6, 1, 9, 7, 8],
                [1, 9, 5, 2, 8, 7, 6, 3, 4]]

testboard3 = [[1, 4, 4, 3, 'a'], [3, 2, 4, 1], [4, 1, 3, 3], [2, 0, 1, 4], ['', False, None, '4']]

test_list = [1,2,3,4]

test_mat = [[1,2],[3,4],[5,6]]

print(test_all(testboard3))
