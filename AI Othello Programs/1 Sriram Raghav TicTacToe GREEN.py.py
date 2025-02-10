from re import X
import sys
from tracemalloc import start
from turtle import pos

start_board = "........."
index_board = "012345678"

def display_board(board):
    print("Current board:")
    print(board[:3] + "    " + index_board[:3])
    print(board[3:6] + "    " + index_board[3:6])
    print(board[6:9] + "    " + index_board[6:9])
    
# display_board(start_board)

def game_over(board):
    for i in range(3):
        if board[i] != "." and (board[i] == board[i+3] == board[i+6]):
            return (True, winner(board[i]))
    val1 = board[0]
    val2 = board[2]

    if board[0] != "." and board[0] == board[4] == board[8]:
        return (True, winner(board[0]))
    if board[2] != "." and board[2] == board[4] == board[6]:
        return (True, winner(board[2]))  

    if (board[0:3] == "XXX" or board[0:3] == "OOO"):
        return (True, winner(board[0]))
    if (board[3:6] == "XXX" or board[3:6] == "OOO"):
        return (True, winner(board[3]))
    if (board[6:9] == "XXX" or board[6:9] == "OOO"):
        return (True, winner(board[6]))
    if not "." in board:
        return (True, 0)
    return (False, None)

def winner(p):
    if p == 'X':
        return 1
    elif (p == 'O'):
        return -1
    else:
        return 0

def who_winner(winner):
    if winner == 1: return "X"
    if winner == 0: return "tie"
    return "O"

def who_wins(win,player):
    if winner(player) == win:
        return "win."
    elif win == 0:
        return "tie."
    else:
        return "loss."

def is_draw(board):
    for i in range(3):
        if board[i] != "." and (board[i] == board[i+3] == board[i+6]):
            return False
    val1 = board[0]
    val2 = board[2]
    
    if board[0] != "." and board[0] == board[4] == board[8]:
        return False
    if board[2] != "." and board[2] == board[4] == board[6]:
        return False   

    if (board[0:3] == "XXX" or board[0:3] == "OOO"):
        return False
    if (board[3:6] == "XXX" or board[3:6] == "OOO"):
        return False
    if (board[6:9] == "XXX" or board[6:9] == "OOO"):
        return False
    return True

final_states = []
specific_states = [0,0,0,0,0,0] # [draws,x in 5, o in 6, x in 7, o in 8, x in 9]

def possible_moves(board):
    possibiles = []
    for i in range(len(board)):
        if board[i] == '.':
            possibiles.append(i)
    return possibiles
            

def possible_next_boards(board, player):
    possibles = []
    board = list(board)
    for i in range(len(board)):
        if (board[i] == "."):
            new_board = board.copy()
            new_board[i] = player
            stri = ""
            for x in new_board:
                stri += str(x)
            possibles.append(stri)
    return possibles

def diff_board(board,new_board):
    for i in range(len(board)): 
        if (board[i] != new_board[i]):
            return i
  

def max_step(board):
    if game_over(board)[0]:
        return game_over(board)[1]
    results = list()
    nodots = "".join(board[i] for i in range(len(board)) if board[i] != '.')
    current_player = ""
    if len(nodots) %2 == 0:
        current_player = "X"
    else: current_player = "O"

    for next_board in possible_next_boards(board, current_player):
        results.append(min_step(next_board))
    return max(results)

def min_step(board):
    if game_over(board)[0]:
        return game_over(board)[1]
    results = list()
    nodots = "".join(board[i] for i in range(len(board)) if board[i] != '.')
    current_player = ""
    if len(nodots) %2 == 0:
        current_player = "X"
    else: current_player = "O"
    for next_board in possible_next_boards(board, current_player):
        results.append(max_step(next_board))
    return min(results)

def x_move(board):
    # print(board)
    # input()
    if game_over(board)[0]:
        final_states.append(board)
        return
    board = list(board)
    for i in range(len(board)):
        if (board[i] == "."): 
            new_board = board.copy()
            new_board[i] = "X"
            #print(new_board)
            stri = ""
            for x in new_board:
                stri += str(x)
            # print(stri)
            # input()
            o_move(stri)
            
def o_move(board):
    if game_over(board)[0]:
        final_states.append(board)
        return
    board = list(board)
    
    for i in range(len(board)):
        if (board[i] == "."):
            new_board = board.copy()
            new_board[i] = "O"
            stri = ""
            for x in new_board:
                stri += str(x)
            x_move(stri)
         
def AI_move(board):
    print()
    # display_board(board)
    nodots = "".join(board[i] for i in range(len(board)) if board[i] != '.')
    current_player = ""
    if len(nodots) %2 == 0:
        current_player = "X"
    else: current_player = "O"
    
    if game_over(board)[0]:
        if game_over(board)[1] == 0:
            print("We tied!")
            return #A
        elif who_winner(game_over(board)[1]) == current_player:
            print("I win!")
            return
        else:
            print("You win!")
            return
    
    possible_boards = possible_next_boards(board, current_player)
    all_boards = []
    best_move_X = [board,-1,-1] #board,index, winner
    best_move_O = [board,1,1] #board,index, winner
    # print(current_player)
    for x in possible_boards:
        if current_player == 'X':
            move = min_step(x)

            stri = ""
            for y in x:
                stri += str(y)
            if move > best_move_X[2]:
                best_move_X[0] = stri
                # best_move[2] = move
                best_move_X[1] = diff_board(board,stri)
                best_move_X[2] = move
            all_boards.append((diff_board(board,stri),move))
        else:
            move = max_step(x)
            stri = ""
            for y in x:
                stri += str(y)
            if move < best_move_O[2]:
                best_move_O[0] = stri
                best_move_O[1] = diff_board(board,stri)
                best_move_O[2] = move
            all_boards.append((diff_board(board,stri),move))
    if board != ".........":
        for x in all_boards:
            print("Moving at " + str(x[0]) + " results in a " +who_wins(x[1],current_player))
    else:
        for x in all_boards:
            print("Moving at " + str(x[0]) + " results in a tie.")
    if best_move_X[0] == board:
        best_move = best_move_O
        print("yes")
    else: 
        best_move = best_move_X
        print("no")
    print()
    print("I choose space " + str(best_move[1]) +".")
    print()
    if (best_move[0] == board):
        bo = list(board)
        bo[best_move[1]] = current_player
        bo_string = ""
        for x in bo:
            bo_string += x
        best_move[0] = bo_string
    # print("Current board:")
    display_board(best_move[0])
    # display_board(index_board)
    print() 
    human_move(best_move[0])

def human_move(board):
    nodots = "".join(board[i] for i in range(len(board)) if board[i] != '.')
    current_player = ""
    if len(nodots) %2 == 0 or nodots == "":
        current_player = "X" #
        # print('X')
    else: current_player = "O"
    
    if game_over(board)[0]:
        if game_over(board)[1] == 0:
            print("We tied!")
            return #A
        elif who_winner(game_over(board)[1]) == current_player:
            print("You win!")
            return
        else:
            print("I win!")
            return
    possible_boards = possible_next_boards(board, current_player)
    indices = []
    for new_boards in possible_boards:
        indices.append(diff_board(board,new_boards))
    print_string = "You can move to any of these spaces:" 
    for x in indices:
        print_string += " "+str(x)+","
    print_string = print_string.strip(",")
    print_string += "."
    choice = input(print_string +"\n" + "Your choice? ")
    # if choice in indices:
    # print("Your choice? " + choice)
    
    print()
    board = list(board)
    new_board = board.copy()
    new_board[int(choice)] = current_player
    #print(new_board)
    stri = ""
    # print(new_board)
    for x in new_board:
        stri += str(x)
    display_board(stri)
    # display_board(index_board)
    return AI_move(stri)
    
    
        
         
x_move(start_board)     

final_set = set()
for x in final_states:
    final_set.add(x)

for x in final_set:
    nodots = "".join(x[i] for i in range(len(x)) if x[i] != '.')
    if len(nodots) == 9 and is_draw(x):

        specific_states[0] += 1
    else:
        specific_states[len(nodots)-4] += 1

playing_board = input("Starting Board: ") # sys.argv[1]
print(playing_board)
if (start_board == playing_board):
    choice = input("Should I be X or O? ")  
    print()
    display_board(playing_board)
    if choice == "X":
        AI_move(playing_board)
    else: human_move(playing_board)
else:
    print()
    display_board(playing_board)
    AI_move(playing_board)
# print(possible_next_boards('.....XX..','O'))
# print(possible_moves('.....XX..'))

# print(diff_board(".........","..X......"))

# print(len(final_set))
# print(specific_states)