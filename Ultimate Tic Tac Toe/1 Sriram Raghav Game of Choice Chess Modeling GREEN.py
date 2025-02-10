# 1 Sriram Raghav Game of Choice Chess Modeling Green.py
# Raghav Sriram
# Tuesday 1/3/2023

import math
from re import U

chess_board = "RNBQKBNRPPPPPPPP................................pppppppprnbqkbnr"
print (len(chess_board))

print(76//9)
print(4%9)

def add_question_mark_border_without_spaces(str): #new_str = '?' * int(math.sqrt(len(str)) + 2) + ''.join('?' + str[a:a+int(math.sqrt(len(str)))] + '?' for a in range(0, len(str), int(math.sqrt(len(str)))) + '?' * int(math.sqrt(len(str)) + 2))
    new_str = '?' * int(math.sqrt(len(str)) + 2) + ''.join('?' + str[a:a+int(math.sqrt(len(str)))] + '?' for a in range(0, len(str), int(math.sqrt(len(str))))) + '?' * int(math.sqrt(len(str)) + 2)
    return new_str

def remove_question_mark_border(str):
    new_str = ''.join([str[i:i+10][1:-1] for i in range(0, len(str), 10)][1:-1])
    return new_str


game = add_question_mark_border_without_spaces(chess_board)

test = remove_question_mark_border(game)


def display_10(board):
    str = '\n'.join(board[a:a+10] for a in range(0, len(board), 10))
    print(str[::-1])

display_10(game)   
print()
def display_8(board):
    str = '\n'.join(board[a:a+8] for a in range(0, len(board), 8))
    print(str[::-1])

display_8(test)

def question_mark_indices(board):
    lis = []
    for i in range(100):
        if board[i] == '?' :
            lis.append(i)
    return lis
question_mark_indexes = question_mark_indices(game)

def convert_10_to_8(index):
    u = index // 10
    v = index % 10
    return (u-1) * 8 + (v-1)

def convert_8_to_10(index):
    for i in range(100):
        if (convert_10_to_8(i) == index and i not in question_mark_indexes):
            return i

def possible_moves(board, token):
    P_dir = []
    R_dir = []
    N_dir = []
    B_dir = []
    Q_dir = []
    K_dir = []
    p_dir = []
    r_dir = []
    n_dir = []
    b_dir = []
    q_dir = []
    k_dir = []

def possibles_moves_KNIGHT(board):
    return