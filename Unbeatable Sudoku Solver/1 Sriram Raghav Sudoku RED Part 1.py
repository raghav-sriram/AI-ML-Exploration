
# GLOBAL VARIABLES

# from tkinter import N
from turtle import pu
from time import perf_counter
import sys


global N_size
global subblock_height
global subblock_width
global symbol_set
global constraints
global neighbors

N_size, subblock_height, subblock_width, symbol_set = 1,0,0,set()

constraints = []
neighbors = dict()

puzzle = [] # holds tuples with (N,height,width,symbols)

def display_puzzle(sudoku):
    
    #sudoku = state[0]
    # sudoku, nnn, high, wid, cym = state[0],state[1],state[2],state[3],state[4]

    # i = 0
    # while i < len(sudoku):
    #     print(" | ".join(sudoku[i:i+N_size]))
    #     i+=N_size

    for i in range(N_size):
        if i % subblock_height == 0: print()
        for j in range(0,subblock_height):
            u = i*N_size + j * subblock_width
            v = i*N_size + (1+j) * subblock_width
            print(" ".join(sudoku[u:v]),end="  |  ")
        print()
        

#++++++++++++++++++ Constriant Set ++++++++++++++++++#

def make_constraints():
    
    constr = []
    # neighbors = dict()

    for i in range (N_size): #constraining rows & columns
        temp_rows = set()
        temp_cols = set()
        # for j in range(N_size):
        temp_rows = {(i*N_size+j) for j in range(N_size)}
        temp_cols = {(i+k*N_size) for k in range(N_size) }
        constr.append(temp_rows)
        constr.append(temp_cols)

        
    less = 0

    while less < N_size**2:
        constrain = set()
        Nh = N_size*subblock_height
        for h in range(less,N_size*subblock_height+less,N_size):
            for w in range(h,subblock_width+h): constrain.add(w)
        if (less+subblock_width) % N_size != 0:
            less += subblock_width
        else:
            while less % N_size != 0: less = less- subblock_width
            less += Nh
        constr.append(constrain)

    return constr


def make_neighbors():
    neighborers = dict()
    #creating neighbors
    for i in range(N_size**2):
        neighs = set()
        for constraint_set in constraints:
            if i in constraint_set:
                for x in constraint_set:
                    if x != i:
                        neighs.add(x)
        neighborers.update({i:neighs})
    return neighborers

#++++++++++++++++++ Constriant Set ++++++++++++++++++#

def check_symbols(sudoku):
    
    counter = []
    for i in sudoku[4]:
        counter.append("Symbol: " + str(i) + " Count: " + str(sudoku[0].count(i)))
    return counter
    
# print(check_symbols(puzzle[0]))

def get_next_unassigned_var(board):
    for i in range (N_size**2):
        if board[i] == ".":
            return i
    return None

# print(get_next_unassigned_var(puzzle[0][0]))

def get_sorted_values(board,key):
    neighbor_set = neighbors.get(key)
    possibiles = sorted(symbol_set)

    for x in neighbor_set:
        if board[x] in possibiles: possibiles.remove(board[x])
    return possibiles

# print("get_sorted_values()")
# print(get_sorted_values(puzzle[0][0],0))

def csp_backtracking(board):
    # board = list(board)
    # print(board)
    var = get_next_unassigned_var(board)
    if var is None:
        return board
    for val in get_sorted_values(board, var):
        new_board = board.copy()
        new_board[var] = val
        returned_board = csp_backtracking(new_board)
        if returned_board is not None:
            return returned_board
    return None

def num(board):
    total = []
    for x in symbol_set: total.append(board.count(x))
    return total

# puzzles_1_standard_easy
# puzzles_2_variety_easy
# Documents\AI 1 Unit 2 Constraint Satisfaction\puzzles_2_variety_easy.txt
chars = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
with open ("puzzles_2_variety_easy.txt") as infile:
    sud_puz = [line.strip() for line in infile]
    for puz in sud_puz: #in infile
        # N_size, subblock_height, subblock_width, symbol_set = 0,0,0,set()
        N_size = int(len(puz)**0.5)
        # N_size = 18
        # print(N_size)
        fact = [i for i in range(1,1+int(N_size)) if (N_size%i == 0)]
        if (int(N_size**0.5)**2 == N_size):
            subblock_height = N_size**0.5
            subblock_width = N_size**0.5
        else:
            for x in fact:
                if int(N_size**0.5) < x:
                    subblock_width = x
                    break
            subblock_height = N_size/int(subblock_width)

        subblock_height = int(subblock_height)
        subblock_width = int(subblock_width)
        
        symbol_set = {chars[j] for j in range(N_size)}
        constraints = make_constraints()
        neighbors = make_neighbors()
        finale_board = csp_backtracking(list(puz))
        puzzle_string = ""
        # print(finale_board)
        for final_print in finale_board:
            puzzle_string += str(final_print)
        print(puzzle_string)
        li = num(puzzle_string)
        # print(num)
        # display_puzzle(finale_board)
        puzzle.append((puz, N_size, subblock_height, subblock_width, symbol_set))