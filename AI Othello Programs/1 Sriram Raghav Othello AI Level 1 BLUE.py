# 1 Sriram Raghav Othello AI Level 1 BLUE.py
# Raghav Sriram
# 12/28/2022

# from othello_imports import make_move, possible_moves
import ast
import time
import sys
import math

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

# =============================================================================================================================================

def scoring(board):

    score = 0  
    c_ind = [0,7,56,63]
    c_a_ind = {1: 0, 6: 7, 8: 0, 9: 0, 14: 7, 15: 7, 48: 56, 49: 56, 54: 63, 55: 63, 57: 56, 62: 63}
    edges = [16,24,32,40,58,59,60,61,2,3,4,5,23,31,39,47]
    victory = 500000
    corner = 50000
    edge = 50
    corner_adjacents = 5000
    corner_edge = 50
    mobility = 5

    pos_moves_black = possible_moves(board,"x")
    pos_moves_white = possible_moves(board,"o")

    if game_over(board): #victory
        return victory * (board.count("x") - board.count("o")) # * 

    for x in c_ind: #corners
        if i := board[x] != ".":
            if i == "x":
                score += corner
            else:
                score =- corner

    for x in edges: #corners
        if i := board[x] != ".":
            if i == "x":
                score += edge
            else:
                score =- edge
    
    for x in c_a_ind.keys(): #corner adjacents
        if i := board[x] != ".":
            if i == "x": 
                if board[c_a_ind[x]] != "x":
                    score -= corner_adjacents
                else: score += corner_edge
            else:
                if board[c_a_ind[x]] != "o":
                    score += corner_adjacents
                else: score -= corner_edge

    mob = len(pos_moves_black) - len(pos_moves_white) #mobility
    score += mob*mobility
    return score

def game_over(board):
    return len(possible_moves(board,"x")) == 0 and len(possible_moves(board,"o")) == 0
    # return len(board) == 64 or len(possible_moves(board,"x")) == 0 and len(possible_moves(board,"o")) == 0
    
def min_step(board,token,depth, alpha, beta): # ALPHA/BETA PRUNING HERE
    if depth == 0 or game_over(board):
        return scoring(board)
    
    if len(possible_moves(board,token)) == 0: #if i have no moves
        return max_step(board,'xo'['ox'.index(token)],depth-1,alpha,beta)

    pos_mov = possible_moves(board,token)
    results = list()
    for x in pos_mov:
        results.append(max_step(make_move(board,token,x),'xo'['ox'.index(token)],depth-1,alpha,beta)) # ALPHA/BETA PRUNING HERE
        pru = min(results) # ALPHA/BETA PRUNING HERE
        beta = min(pru,beta) # ALPHA/BETA PRUNING HERE
        if alpha >= pru: break # ALPHA/BETA PRUNING HERE


    return min(results)

def max_step(board,token,depth, alpha, beta): # ALPHA/BETA PRUNING HERE
    if depth == 0 or game_over(board):
        return scoring(board)
    
    if len(possible_moves(board,token)) == 0: #if i have no moves
        return min_step(board,'xo'['ox'.index(token)],depth-1,alpha,beta)

    pos_mov = possible_moves(board,token)
    results = list()
    for x in pos_mov:
        results.append(min_step(make_move(board,token,x),'xo'['ox'.index(token)],depth-1,alpha,beta)) # ALPHA/BETA PRUNING HERE
        pru = max(results) # ALPHA/BETA PRUNING HERE
        alpha = max(pru,alpha) # ALPHA/BETA PRUNING HERE
        if beta <= pru: break # ALPHA/BETA PRUNING HERE
    return max(results)

def find_next_move(board,token,depth):
    alpha = float("-inf")
    beta = float("inf")
    pos_mov = possible_moves(board,token)
    moves = dict()
    results = list()
    for x in pos_mov:
        if token == "x":
            moves[x] = min_step(make_move(board,token,x),'xo'['ox'.index(token)],depth-1,alpha,beta)
            # moves.update({x: min_step(make_move(board,token,x),'xo'['ox'.index(token)],depth-1,alpha,beta)})
        else:
            moves[x] = max_step(make_move(board,token,x),'xo'['ox'.index(token)],depth-1,alpha,beta)
            # moves.update(x,max_step(make_move(board,token,x),'xo'['ox'.index(token)],depth-1,alpha,beta))
    if token == "x":
        return max(moves, key = moves.get)
    else: return min(moves, key = moves.get)


# class Strategy():

#    logging = True  # Optional

#    def best_strategy(self, board, player, best_move, still_running):

#        depth = 1

#        for count in range(board.count(".")):  # No need to look more spaces into the future than exist at all

#            best_move.value = find_next_move(board, player, depth)

#            depth += 1

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

   # Based on whether player is x or o, start an appropriate version of minimax

   # that is depth-limited to "depth".  Return the best available move.



# All your other functions


# results = []
# with open("boards_timing.txt") as f:
#     for line in f:
#         board, token = line.strip().split()
#         temp_list = [board, token]
#         print(temp_list)
#         for count in range(1, 7):
#             print("depth", count)
#             start = time.perf_counter()
#             find_next_move(board, token, count)
#             end = time.perf_counter()
#             temp_list.append(str(end - start))
#         print(temp_list)
#         print()
#         results.append(temp_list)
# with open("boards_timing_my_results.csv", "w") as g:
#     for l in results:
#         g.write(", ".join(l) + "\n")


board = sys.argv[1]

player = sys.argv[2]

depth = 1

for count in range(board.count(".")):  # No need to look more spaces into the future than exist at all

   print(find_next_move(board, player, depth))

   depth += 1