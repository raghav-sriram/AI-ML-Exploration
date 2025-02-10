# 1 Sriram Raghav Game of Choice Ultimate Tic Tac Toe Modeling Green.py
# Raghav Sriram
# Tuesday 1/3/2023

ultimate_board = "XOXOXOOXOXOXOXOOXOXOXOXOOXOXOXOXOOXOXOXOXOOXOXOXOXOOXOXOXOXOOXOXOXOXOOXOXOXOXOOXO"
# print(len(ultimate_board))

"""
Test cases
blank = "................................................................................."
X wins with top 3 "XXX............XXX....XX........................................................."
X wins top left to bot right diagonal "XXX............XXX....XX...............XXX....................................XXX"
X wins bot 3 "XXX............XXX...XOX...............XOX...............XXX......XXX.........XXX"
X wins top right to bot left diagonal "XOX............XXX...XXX...............XXX..................XXX...............XOX"
X wins far right column "XOX............XXX...XXX...............XXX.........XXXX.....XOO...............XXX"
- wins game not over "XOXOXOOXO......XOX...XXX...............XXX..................XOX...............XOX"
- draws "XOXOXOOXOXOXOXOOXOXOXOXOOXOXOXOXOOXOXOXOXOOXOXOXOXOOXOXOXOXOOXOXOXOXOOXOXOXOXOOXO"
"""
p1, p2 = 1, 2
# p1 = input("Who should be Player 1 (X) - Type Human to play manually   ")
# p2 = input("Who should be Player 2 (O) - Type Human to play manually   ")
players = [p1,p2]

def possible_moves(board,num): # num = -1 means the game has just started (can play anywhere)

    possibles = list()
    if num == -1:
        return [i for i in range(0,64)]
    # if num == -2:
    #     for i,v in enumerate(board):
    #         if v == ".":
    #             possibles.append(i)
    #     return possibles
    start_index = 9*num
    for i in range(start_index,start_index+9):
        if board[i] == ".": possibles.append(i)
    return possibles

def possible_next_boards(board,token,num):
    
    possibles = list()
    board = list(board)
    if num == -1:
        for i in range (len(board)):
            if (board[i] == "."):
                new_board = board.copy()
                new_board[i] = token
                stri = "".join(str(x) for x in new_board)
                possibles.append(stri)
        # return [i for i in range(0,64)]
        return possibles
    start_index = 9*num
    for i in range(start_index,start_index+9):
        if (board[i] == "."):
                new_board = board.copy()
                new_board[i] = token
                stri = "".join(str(x) for x in new_board)
                possibles.append(stri)
    # print("\n".join(x for x in possibles))
    return possibles

def make_move(board, token, index):
    board = list(board)
    board[index] = token
    return ("".join(str(x) for x in board),index%9)

def game_over(board):
    games_and_results = [game_over_small(board[9*i:9*i+9]) for i in range(9)]

    for i in range(3):
        if games_and_results[i][0] == True and games_and_results[i][1] != 0 and (games_and_results[i][1] == games_and_results[i+3][1] == games_and_results[i+6][1]):
            # print("here" + str(i))
            return (True, games_and_results[i][1])
    val1 = board[0]
    val2 = board[2]

    if games_and_results[0][0] == True and games_and_results[0][1] != 0 and games_and_results[0][1] == games_and_results[4][1] == games_and_results[8][1]:
        # print("nah here")
        return (True, games_and_results[0][1])
    if games_and_results[2][0] == True and games_and_results[2][1] != "." and games_and_results[2][1] == games_and_results[4][1] == games_and_results[6][1]:
        # print("nah nah here")
        return (True, games_and_results[2][1])  

    for i in range (3):
        if (games_and_results[3*i][0] == True and games_and_results[3*i][1] != 0 and games_and_results[3*i][1] == games_and_results[3*i+1][1] == games_and_results[3*i+2][1]):
            # print("nah nah nah here")
            return (True, games_and_results[3*i][1])

    # if (board[0:3] == "X XX" or board[0:3] == "OOO"):
    #     return (True, winner(board[0]))
    # if (board[3:6] == "X XX" or board[3:6] == "OOO"):
    #     return (True, winner(board[3]))
    # if (board[6:9] == "X XX" or board[6:9] == "OOO"):
    #     return (True, winner(board[6]))
    # if not (True, 0) in games_and_results:

    if not "." in board:
        # print("nah nah nah nah here")
        return (True, 0)

    return (False, None) # (False, None)

    # print(games_and_results)

def game_over_small(board): # ADD WALRUS
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
    if winner == 1: return "X wins"
    if winner == 0: return "DRAW"
    return "O wins"

def display(board):
    print("---------------")
    for i in range (3):
        print(board[3*i:3*i+3] + " | " + board[9+ 3*i:9+ 3*i+3] + " | " + board[18+ 3*i:18+ 3*i+3])
    print("---------------")
    for i in range (3):
        print(board[3*i + 27:3*i+3 + 27] + " | " + board[9+ 3*i + 27:9+ 3*i+3 + 27] + " | " + board[18+ 3*i + 27:18+ 3*i+3 + 27])
    print("---------------")
    for i in range (3):
        print(board[3*i + 54:3*i+3 + 54] + " | " + board[9+ 3*i + 54:9+ 3*i+3 + 54] + " | " + board[18+ 3*i + 54:18+ 3*i+3 + 54])
    print("---------------")

# def display_index_board():
#     print("\n------------------------------")
#     print("0 1 2     |  3 4 5     |  6 7 8")
#     print("9 10 11   |  12 13 14  |  15 16 17")
#     print("18 19 20  |  21 22 23  |  24 25 26")
#     print("----------------------------------")
#     print("27 28 29  |  30 31 32  |  33 34 35")
#     print("36 37 38  |  39 40 41  |  42 43 44")
#     print("45 46 47  |  48 49 50  |  51 52 53")
#     print("----------------------------------")
#     print("54 55 56  |  57 58 59  |  60 61 62")
#     print("63 64 65  |  66 67 68  |  69 70 71")
#     print("72 73 74  |  75 76 77  |  78 79 80")
#     print("------------------------------\n")

def display_index_board():
    print("\n0  1  2  |  9 10 11 | 18 19 20")
    print("3  4  5  | 12 13 14 | 21 22 23")
    print("6  7  8  | 15 16 17 | 24 25 26")
    print("------------------------------")
    print("27 28 29 | 36 37 38 | 45 46 47")
    print("30 31 32 | 39 40 41 | 48 49 50")
    print("33 34 35 | 42 43 44 | 51 52 53")
    print("------------------------------")
    print("54 55 56 | 63 64 65 | 72 73 74")
    print("57 58 59 | 66 67 68 | 75 76 77")
    print("60 61 62 | 69 70 71 | 78 79 80")
    print("------------------------------\n")

# print(possible_next_boards(ultimate_board,"x",-1))
# (possible_next_boards(ultimate_board,"x",8))
# print(make_move(ultimate_board,"X",10)[0:2])
# print(ultimate_board)
# # print([game_over_small(ultimate_board[9*i:9*i+9]) for i in range(9)][7])
# game_over(ultimate_board)
# print(game_over(ultimate_board))
# print()
# display(ultimate_board)
# print()

def run_game(players):
    # print(players)
    board = "................................................................................."
    # display(board)
    input("\nRules for Ultimate Tic Tac Toe:")
    # input("Chose a number from the possible moves to make your move.")
    input("Use the board of indexes/possible moves to decided where you want to move to")
    input("Where you move on the small board directly corresponds to where your opponent plays next")
    input("If your opponent sends you to a board that is already over, you can play anywhere except those boards")
    input("The goal is to win three different games in a row, column, or diagonal")
    display(board)
    display_index_board()


    first_move = input("Enter the first move for X (Type in any index from the board)  ")
    tac = make_move(board,"X",int(first_move))
    # while not game_over(tac[0])[0]:
    # while True:   
    O_turn_human(tac)

def O_turn_human(toe):
    display(toe[0])
    display_index_board()
    # print(toe[1])
    # print(toe[0][9*toe[1]:9*toe[1]+9])
    if game_over_small(toe[0][9*toe[1]:9*toe[1]+9])[0]:
        p = list()
        for i,v in enumerate(toe[0]):
            if v == "." and i not in [ind for ind in range(9*toe[1],9*toe[1]+9)]: p.append(i)
        print("Possible moves for O: " + str(p))
    else: print("Possible moves for O: " + str(p:= possible_moves(toe[0],toe[1])))
    # toe[0][9*toe[1]:9*toe[1]+9]
    move = input("Enter the move for O from the possible moves:  ")
    while int(move) not in p:
        move = input("Enter the move for O from the possible moves:  ")
    moved = make_move(toe[0],"O",int(move))
    if not game_over(moved[0])[0]:
        X_turn_human(moved)
    else:
        display(moved[0])
        print("Game Over")
        w = game_over(moved[0])[1]
        print(who_winner(w))

def X_turn_human(tic):
    display(tic[0])
    display_index_board()
    if game_over_small(tic[0][9*tic[1]:9*tic[1]+9])[0]:
        p = list()
        for i,v in enumerate(tic[0]):
            if v == "." and i not in [ind for ind in range(9*tic[1],9*tic[1]+9)]: p.append(i)
        print("Possible moves for X: " + str(p))
    else: print("Possible moves for X: " + str(p:= possible_moves(tic[0],tic[1])))
    # toe[0][9*toe[1]:9*toe[1]+9]
    move = input("Enter the move for X from the possible moves:  ")
    while int(move) not in p:
        move = input("Enter the move for X from the possible moves:  ")
    moved = make_move(tic[0],"X",int(move))
    if not game_over(moved[0])[0]:
        O_turn_human(moved)
    else:
        display(moved[0])
        print("Game Over")
        w = game_over(moved[0])[1]
        print(who_winner(w))


# display_index_board()
run_game(players)