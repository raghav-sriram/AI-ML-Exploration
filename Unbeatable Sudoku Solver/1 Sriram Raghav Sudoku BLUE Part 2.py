from mimetypes import guess_all_extensions
from re import T
import sys

with open("puzzles_3_standard_medium.txt") as f:
    line_list = [line.strip() for line in f]





def list_to_string(list):
    string = ""
    for i in list:
        string = string + i
    return string

def display_board(state):
    toRet = ""
    for j in range(size):
        if j!= 0 and j%subblock_height == 0:
            toRet = toRet + ("----- " * int((size * 2 - subblock_width))) + "\n"
        for i in range (size):
            if i!= 0 and i%subblock_width == 0:
                toRet = toRet + " | "
            toRet = toRet + board_list[i+(j*size)] + "   "
        toRet = toRet + "\n"
    return toRet

#print(display_board(board_list))


def gut_check (state):
    for i in symbol_set:
        count = 0
        for j in state:
            if len(j) > 1:
                return False
            if j==i:
                count += 1
        if count != size:
            return False
    return True
    

def get_next_unassigned_var(board_list):
    min = 100
    ret = 0
    for i in range(len(board_list)):
        if len(board_list[i]) > 1 and len(board_list[i])<min:
            min = len(board_list[i])
            ret = i
    return ret

def get_sorted_values(state, var):
    possible_set = symbol_set.copy()
    iter_list = list(constraint_dict[var])
    for i in iter_list:
        if len(state[i]) == 1 and state[i] in possible_set:
            possible_set.remove(state[i])
    return list(possible_set)

def forward_looking(board_list):
    solved_list = []
    for i in range(len(board_list)):
        if len(board_list[i]) == 1:
            solved_list.append(i)
    # \while len(solved_list)!=0:
    for i in solved_list:
        const = board_list[i]
        t_set = constraint_dict[i]
        for j in t_set:
            item = board_list[j] 
            if const in item:
                x = item.index(const)
                board_list[j] = item[0:x] + item[x+1:]
                if len(board_list[j]) == 1:
                    solved_list.append(j)
                if len(board_list[j]) == 0:
                    return None
    return board_list

def copy(state):
    toRet = []
    for i in state:
        toRet.append(i)
    return toRet    

def csp_backtracting_with_fl(state):
    if gut_check(state):
        return state
    var = get_next_unassigned_var(state)
    for val in get_sorted_values(state, var):
        new_board = copy(state)
        new_board[var]=val
        checked_board = forward_looking(new_board)
        if checked_board != None:
            result = csp_backtracting_with_fl(checked_board)
            if result != None:
                return result
    return None



for x in line_list:
    state = x
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    size = int(len(state) ** 0.5)
    temp1 = int(size**0.5)
    while size%temp1 != 0:
        temp1 = temp1 - 1
    subblock_height = temp1
    subblock_width = size // temp1
    symbol_set = set()

    if size<=9:
        for i in range(size):
            symbol_set.add(str(i+1))
    else:
        symbol_set = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
        temp2 = size - 9
        for i in range (temp2):
            symbol_set.add(alphabet[i])

    symbol_string = ""
    for i in symbol_set:
        symbol_string = symbol_string+i

    board_list = []
    for i in state:
        if i == ".":
            board_list.append(symbol_string)
        else:
            board_list.append(i)

    constraint_list = []

    for i in range(0,  size*size-1,  size):
        row_set = set()
        for j in range(size):
            row_set.add(i+j)
        constraint_list.append(row_set)

    for j in range(size):
        col_set = set()
        for i in range(0,  size*size-1,  size):
            col_set.add(i+j)
        constraint_list.append(col_set)

    for i in range(subblock_width):
        for j in range(subblock_height):
            block_set = set()
            temp_left_index = (i * (size* subblock_height) + (j*subblock_width))
            for k in range(subblock_height):
                for m in range(subblock_width):
                    final_index = temp_left_index + (k*size) + m
                    block_set.add(final_index)
            constraint_list.append(block_set)

    constraint_dict = dict()
    for i in range(int(size**2)):
        temp_set = set()
        for j in constraint_list:
            if i in j:
                for k in j:
                    if k!=i:
                        temp_set.add(k)
        constraint_dict[i] = temp_set
    
    t = forward_looking(board_list)
    y = gut_check(t)
    if y == True:
        print(list_to_string(t))
        print(y)
    if y == False:
        x = csp_backtracting_with_fl(board_list)
        print(list_to_string(x))
        print(gut_check(x))
    #print(t)
    # if gut_check(t) == False:
    #     print(list_to_string(csp_backtracting_with_fl(board_list)))

    print("\n")

    #print(display_board(csp_backtracting_with_fl(board_list)))