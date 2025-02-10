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












# # 1 Sriram Raghav Othello Modeling BLUE.py
# # Raghav Sriram
# # 11/28/2022

# import math
# from re import U

# # char_board = "x x o o . x o x . . . . . o o x . . . . . . o x o . . o o x o o o . . o o x . o x . x x x . . o x o o x . . . o . . . . . x o x"
# # no_space_board = "".join(char_board.split(" "))              here
# char_board = "xxoo.xox.....oox......oxo..ooxooo..oox.ox.xxx..oxoox...o.....xox"

# def add_question_mark_border_without_spaces(str): #new_str = '?' * int(math.sqrt(len(str)) + 2) + ''.join('?' + str[a:a+int(math.sqrt(len(str)))] + '?' for a in range(0, len(str), int(math.sqrt(len(str)))) + '?' * int(math.sqrt(len(str)) + 2))
#     new_str = '?' * int(math.sqrt(len(str)) + 2) + ''.join('?' + str[a:a+int(math.sqrt(len(str)))] + '?' for a in range(0, len(str), int(math.sqrt(len(str))))) + '?' * int(math.sqrt(len(str)) + 2)
#     return new_str

# oth_board = add_question_mark_border_without_spaces(char_board)
# print(oth_board) 
# # print('\n'.join(oth_board[a:a+10] for a in range(0, len(oth_board), 10)))
# print(char_board)

# def display(board):
#     print('\n'.join(board[a:a+10] for a in range(0, len(board), 10)))

# display(oth_board)   

# def question_mark_indices(board):
#     lis = []
#     for i in range(100):
#         if board[i] == '?' :
#             lis.append(i)
#     return lis
# question_mark_indexes = question_mark_indices(oth_board)
# print(question_mark_indexes)

# def convert_10_to_8(index):
#     u = index//10
#     v = index%10
#     retur = (u-1)*8 + (v-1)
#     return retur

# def convert_8_to_10(index):
#     # return (i for i in range(100) if (convert_10_to_8(i) == index))
#     for i in range(100):
#         if (convert_10_to_8(i) == index and i not in question_mark_indexes):
#             return i

# test = 34+7-5
# conv = convert_10_to_8(test)
# print(conv)
# print(convert_8_to_10(convert_10_to_8(test)))

# def possible_moves(board, token):

#     opp = 'xo'['ox'.index(token)]
#     possibles = []
#     directions = [-11, -10, -9, -1, 1, 9, 10, 11]
#     for i in range(len(board)):
#         if board[i] == ".":
#             for dir in directions:
#                 pos = i + dir
#                 if board[pos] == opp:
#                     while board[pos] == opp:
#                         pos+=dir
#                     if board[pos] == token:
#                         possibles.append(pos)
#     return possibles

# poss = possible_moves(oth_board,"x")
# print(poss)

# def make_move(board,token,index):
#     # board = list(board)
#     ind = convert_8_to_10(index)
#     question = add_question_mark_border_without_spaces(board)
#     question = list(question)
#     opp = 'xo'['ox'.index(token)]
#     # board = board[:index] + token  + board[index+1:]
#     question[ind] = token
#     # print ([ind])
#     right, left, up, down, top_right_diag, top_left_diag, bottom_right_diag, bottom_left_diag = [], [], [], [], [], [], [], []
#     right_bool, left_bool, up_bool, down_bool, top_right_diag_bool, top_left_diag_bool, bottom_right_diag_bool, bottom_left_diag_bool = True, True, True, True, True, True,True, True
    
#     # check right
#     while True:
#         for i in range(1,10-ind%10):
#             if (question[ind+i] == opp):
#                 right.append(ind+i)
#             elif (question[ind+i] == "?" or question[ind+i] == "."):
#                 right_bool = False
#                 break
#             else: # not an opp
#                 if len(right) == 0: right_bool = False
#                 break
#         break
    
#     # check left
#     while True:
#         for i in range(1,ind%10):
#             if (ind%10 <= 1):
#                 break
#             elif (question[ind-i] == opp):
#                 left.append(ind-i)
#             elif (question[ind-+i] == "?" or question[ind-i] == "."):
#                 left_bool = False
#                 break
#             else: # not an opp
#                 if len(left) == 0: left_bool = False
#                 break
#         break
    
#     # check up
#     while True:
#         for i in range(1,ind%10):
#             if (question[ind-i*10] == opp):
#                 up.append(ind-i*10)
#             elif (question[ind-i*10] == "?" or question[ind-i*10] == "."):
#                 up_bool = False
#                 break
#             else: # not an opp
#                 if len(up) == 0: up_bool = False
#                 break
#         break
    
#     # check down
#     while True:
#         for i in range(1,10-ind%10):
#             if (question[ind+i*10] == opp):
#                 down.append(ind+i*10)
#             elif (question[ind+i*10] == "?" or question[ind+i*10] == "."):
#                 down_bool = False
#                 break
#             else: # not an opp
#                 if len(down) == 0: down_bool = False
#                 break
#         break
    
#     # check top right diagonal
#     while True:
#         for i in range(1,ind%10):
#             if (question[ind-i*9] == opp):
#                 top_right_diag.append(ind-i*9)
#             elif (question[ind-i*9] == "?" or question[ind-i*9] == "."):
#                 top_right_diag_bool = False
#                 break
#             else: # not an opp
#                 if len(top_right_diag) == 0: top_right_diag_bool = False
#                 break
#         break
    
#     # check top left diagonal
#     while True:
#         for i in range(1,ind%10):
#             if (question[ind-i*11] == opp):
#                 top_left_diag.append(ind-i*11)
#             elif (question[ind-i*11] == "?" or question[ind-i*11] == "."):
#                 top_left_diag_bool = False
#                 break
#             else: # not an opp
#                 if len(top_left_diag) == 0: top_left_diag_bool = False
#                 break
#         break
    
#     # check bottom right diagonal
#     while True:
#         for i in range(1,10-ind%10):
#             if (question[ind+i*11] == opp):
#                 bottom_right_diag.append(ind+i*11)
#             elif (question[ind+i*11] == "?" or question[ind+i*11] == "."):
#                 bottom_right_diag_bool = False
#                 break
#             else: # not an opp
#                 if len(bottom_right_diag) == 0: bottom_right_diag_bool = False
#                 break
#         break
    
#     # check bottom left diagonal
#     while True:
#         for i in range(1,10-ind%10):
#             if (question[ind+i*9] == opp):
#                 bottom_left_diag.append(ind+i*9)
#             elif (question[ind+i*9] == "?" or question[ind+i*9] == "."):
#                 bottom_left_diag_bool = False
#                 break
#             else: # not an opp
#                 if len(bottom_left_diag) == 0: bottom_left_diag_bool = False
#                 break
#         break
    
#     # print(right)
#     for x in right:
#         if right_bool:
#             question[x] = token
            
#     # print(left)
#     for x in left:
#         if left_bool:
#             question[x] = token
            
#     # print(up)
#     for x in up:
#         if up_bool:
#             question[x] = token
    
#     # print(down)
#     for x in down:
#         if down_bool:
#             question[x] = token
            
#     # print(top_right_diag)
#     for x in top_right_diag:
#         if top_right_diag_bool:
#             question[x] = token
    
#     # print(top_left_diag)
#     for x in top_left_diag:
#         if top_left_diag_bool:
#             question[x] = token
    
#     # print(bottom_right_diag)
#     for x in bottom_right_diag:
#         if bottom_right_diag_bool:
#             question[x] = token
            
#     # print(bottom_left_diag)
#     for x in bottom_left_diag:
#         if bottom_left_diag_bool:
#             question[x] = token
    
#     return "".join(x for x in question)

# moves = make_move(char_board,"x",conv)
# print(moves)
# display(moves)

# # def add_question_mark_border(str): return ' '.join(a for a in '?' * int(math.sqrt(len(''.join(char_board.split(" ")))) + 2) + ''.join('?' + ''.join(char_board.split(" "))[a:a+int(math.sqrt(len(''.join(char_board.split(" ")))))] + '?' for a in range(0, len(''.join(char_board.split(" "))), int(math.sqrt(len(''.join(char_board.split(" "))))))) + '?' * int(math.sqrt(len(''.join(char_board.split(" ")))) + 2))
# # THIS IS FOR IF THERE ARE SPACES --> return '?' * int(math.sqrt(len(''.join(char_board.split(" ")))) + 2) + ''.join('?' + ''.join(char_board.split(" "))[a:a+int(math.sqrt(len(''.join(char_board.split(" ")))))] + '?' for a in range(0, len(''.join(char_board.split(" "))), int(math.sqrt(len(''.join(char_board.split(" "))))))) + '?' * int(math.sqrt(len(''.join(char_board.split(" ")))) + 2)