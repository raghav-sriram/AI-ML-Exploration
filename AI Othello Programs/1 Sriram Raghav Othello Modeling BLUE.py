# 1 Sriram Raghav Othello Modeling BLUE.py
# Raghav Sriram
# 11/28/2022

import math
from re import U

char_board = "xxoo.xox.....oox......oxo..ooxooo..oox.ox.xxx..oxoox...o.....xox"

def add_question_mark_border_without_spaces(str): #new_str = '?' * int(math.sqrt(len(str)) + 2) + ''.join('?' + str[a:a+int(math.sqrt(len(str)))] + '?' for a in range(0, len(str), int(math.sqrt(len(str)))) + '?' * int(math.sqrt(len(str)) + 2))
    new_str = '?' * int(math.sqrt(len(str)) + 2) + ''.join('?' + str[a:a+int(math.sqrt(len(str)))] + '?' for a in range(0, len(str), int(math.sqrt(len(str))))) + '?' * int(math.sqrt(len(str)) + 2)
    return new_str

def remove_question_mark_border(str):
    new_str = ''.join([str[i:i+10][1:-1] for i in range(0, len(str), 10)][1:-1])
    return new_str


oth_board = add_question_mark_border_without_spaces(char_board)

test = remove_question_mark_border(oth_board)


def display_10(board):
    print('\n'.join(board[a:a+10] for a in range(0, len(board), 10)))

# display_10(oth_board)   

def display_8(board):
    print('\n'.join(board[a:a+8] for a in range(0, len(board), 8)))

# display_8(test)

def question_mark_indices(board):
    lis = []
    for i in range(100):
        if board[i] == '?' :
            lis.append(i)
    return lis
question_mark_indexes = question_mark_indices(oth_board)

def convert_10_to_8(index):
    u = index // 10
    v = index % 10
    return (u-1) * 8 + (v-1)

def convert_8_to_10(index):
    for i in range(100):
        if (convert_10_to_8(i) == index and i not in question_mark_indexes):
            return i

test = 34+7-5
conv = convert_10_to_8(test)

def possible_moves(board, token):
    directions = [-11, -10, -9, -1, 1, 9, 10, 11]
    oth_board = add_question_mark_border_without_spaces(board)

    opp = 'xo'['ox'.index(token)]

    moves = list()

    for i in range(0,len(oth_board)):
        if oth_board[i] == '.':
            for x in directions:
                fin = x+i
                if oth_board[fin] == opp:
                    while oth_board[fin] == opp: fin += x
                    if oth_board[fin] == token: moves.append(i)
    return sorted(list(set([(convert_10_to_8(x)) for x in moves])))

# print(possible_moves("xxoo.xox.....oox......oxo..ooxooo..oox.ox.xxx..oxoox...o.....xox", 'x'))
# [4, 12, 16, 19, 20, 21, 26, 34, 56, 57, 58]



def make_move(board, token, index):
    directions = [-11, -10, -9, -1, 1, 9, 10, 11]
    
    
    oth_board = add_question_mark_border_without_spaces(board[:index] + '-' + board[1+index:])
    
    ind = oth_board.index("-")

    oth_board = add_question_mark_border_without_spaces(board[:index] + token + board[1+index:])
    opp = 'xo'['ox'.index(token)]
    moves = list()
    for x in directions:
        la = x+ind
        if opp == oth_board[la]:
            var = list()
            while opp == oth_board[la]:
                var.append(la)
                la += x
            if oth_board[la] == token:
                moves += var
    for x in moves:
        oth_board = oth_board[:x]+token+oth_board[1+x:]

    return remove_question_mark_border(oth_board)