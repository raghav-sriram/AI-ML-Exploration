# 1 Sriram Raghav Game of Choice Ultimate Tic Tac Toe Variety of AI BLUE.py
# Raghav Sriram
# Tuesday 1/3/2023
from random import choice
import sys



ultimate_board = "................................................................................."
ultimate_board = "OOO............OOO...XXX...X..X..XX....OOO......XXX.........XOX......OO.....OOXOX"
print(len(ultimate_board))

"""
Test cases 
# X wins with top 3 "XXX............XXX....XX........................................................."
X wins top left to bot right diagonal "XXX............XXX....XX...............XXX....................................XXX"
X wins bot 3 "XXX............XXX...XOX...............XOX...............XXX......XXX.........XXX"
X wins top right to bot left diagonal "XOX............XXX...XXX...............XXX..................XXX...............XOX"
X wins far right column "XOX............XXX...XXX...............XXX.........XXXX.....XOO...............XXX"
- wins game not over "XOXOXOOXO......XOX...XXX...............XXX..................XOX...............XOX"
- draws "XOXOXOOXOXOXOXOOXOXOXOXOOXOXOXOXOOXOXOXOXOOXOXOXOXOOXOXOXOXOOXOXOXOXOOXOXOXOXOOXO"
"""

p1, p2 = sys.argv[1], sys.argv[2]
# p1 = input("Who should be Player 1 (X)   ")
# p2 = input("Who should be Player 2 (O)   ")
players = [p1,p2]

def min_scoring(board, victory = 1000, count = 2, two = 8, one_space_one = 4, one_diagonal_space_one = 5, center = 3, corner = 2):
    if game_over(board)[0]:
        return 10000 * sum(game_over_small(board[9*i:9*i+9])[1] for i in range(9) if game_over_small(board[9*i:9*i+9])[0])
    
    # return sum(score_small(board[9*i:9*i+9],victory, count, two, one_space_one, one_diagonal_space_one, center, corner) for i in range (9))
    
    scores = list()
    for i in range(9):
        scores.append((i,score_small(board[9*i:9*i+9],victory, count, two, one_space_one, one_diagonal_space_one, center, corner)))
    sort_scores = sorted(scores)[::-1]
    # allocate numbers
    
    
    

def scoring(num, board, token, victory = 100, count = 2, two = 8, one_space_one = 4, one_diagonal_space_one = 5, center = 3, corner = 2):
    score = 0
    if game_over(board)[0]:
        return 10000000 * sum(game_over_small(board[9*i:9*i+9])[1] for i in range(9) if game_over_small(board[9*i:9*i+9])[0])
    
    # return sum(score_small(board[9*i:9*i+9],victory, count, two, one_space_one, one_diagonal_space_one, center, corner) for i in range (9))
    
    scores = list()
    for i in range(9):
        scores.append((i,score_small(token,board[9*i:9*i+9],victory, count, two, one_space_one, one_diagonal_space_one, 1, corner)))
    games_and_results = [game_over_small(board[9*i:9*i+9]) for i in range(9)]

    nah = [i for i in range(9) if games_and_results[i][0] == False]
    # print(nah)

    X_wins = 0
    O_wins = 0
    for x in games_and_results:
        if x==[True,"X"]: X_wins += 1
        if x==[True,"O"]: O_wins += 1
    score += 10*(X_wins-O_wins)
    # score += sum(0.1*score_small(board[9*i:9*i+9],victory, count, two, oneS_space_one, one_diagonal_space_one, center, corner) for i in range (9))
    # print(scores)
    score += sum(j for i,j in scores)
    
    # print(score)
    
    

    for i in range(3):
        if games_and_results[i][0] == True and games_and_results[i][1] != 0 and ((games_and_results[i][1] == games_and_results[i+3][1]) or (games_and_results[i][1] == games_and_results[i+6][1])):
            # print("here" + str(i))
            score += 200 * games_and_results[i][1]
        if games_and_results[i+3][0] == True and games_and_results[i+3][1] != 0 and games_and_results[i+3][1] == games_and_results[i+6][1]:
            # print("inga ")
            # return (True, games_and_results[i][1])
            score += 200 * games_and_results[i+3][1]
    if games_and_results[0][0] == True and games_and_results[0][1] != 0 and (games_and_results[0][1] == games_and_results[4][1] or games_and_results[0][1] == games_and_results[8][1]):
        # print("oi mate")
        score += 200 * games_and_results[0][1]
    if games_and_results[4][0] == True and games_and_results[4][1] != 0 and (games_and_results[8][1] == games_and_results[4][1] or games_and_results[6][1] == games_and_results[4][1]):
        # print("yo")
        score += 200 * games_and_results[4][1]
    
    if games_and_results[2][0] == True and games_and_results[2][1] != 0 and (games_and_results[2][1] == games_and_results[4][1] or games_and_results[2][1] == games_and_results[6][1]):
        # print("wsg mate")
        score += 200 * games_and_results[2][1]
    
    for i in range (3):
        if (games_and_results[3*i][0] == True and games_and_results[3*i][1] != 0 and (games_and_results[3*i][1] == games_and_results[3*i+1][1] or games_and_results[3*i][1] == games_and_results[3*i+2][1])):
            # print("nah nah nah here")
            score += 200 * games_and_results[3*i][1]
        if games_and_results[3*i+1][0] == True and games_and_results[3*i+1][1] != 0 and games_and_results[3*i+2][1] == games_and_results[3*i+1][1]:
            score += 200 * games_and_results[3*i+1][1]
            # return (True, games_and_results[3*i][1])
            
# ===================================================================================

    for i in range(3):
        if games_and_results[i][0] == True and games_and_results[i][1] != 0 and i+6 not in nah:
            if games_and_results[i][1] == games_and_results[i+3][1] == -1*games_and_results[i+6][1]:
            # print("here" + str(i))
                score += 150 * games_and_results[i+6][1]
        if games_and_results[i][0] == True and games_and_results[i][1] != 0 and i+3 not in nah:
            if games_and_results[i][1] == games_and_results[i+6][1] == -1*games_and_results[i+3][1]:
            # print("here" + str(i))
                score += 150 * games_and_results[i+3][1]
        if games_and_results[i+3][0] == True and games_and_results[i+3][1] != 0 and i+0 not in nah:
            if games_and_results[i+3][1] == games_and_results[i+6][1] == -1*games_and_results[i][1]:
            # print("inga ")
            # return (True, games_and_results[i][1])
                score += 150 * games_and_results[i][1]
    if games_and_results[0][0] == True and games_and_results[0][1] != 0 and 8 not in nah:
        if games_and_results[0][1] == games_and_results[4][1] == -1*games_and_results[8][1]:
            score += 150 * games_and_results[8][1]
    if games_and_results[0][0] == True and games_and_results[0][1] != 0 and 4 not in nah:
        if games_and_results[0][1] == games_and_results[8][1] == -1*games_and_results[4][1]:
        # print("oi mate")
            score += 150 * games_and_results[4][1]
    if games_and_results[4][0] == True and games_and_results[4][1] != 0 and 0 not in nah:
        if games_and_results[8][1] == games_and_results[4][1] == -1*games_and_results[0][1]:
            score += 150 * games_and_results[0][1]
    if games_and_results[4][0] == True and games_and_results[4][1] != 0 and 2 not in nah: 
        if games_and_results[6][1] == games_and_results[4][1] == -1*games_and_results[2][1]:
        # print("yo")
            score += 150 * games_and_results[2][1]
    
    if games_and_results[2][0] == True and games_and_results[2][1] != 0 and 6 not in nah:
        if games_and_results[2][1] == games_and_results[4][1] == -1*games_and_results[6][1]:    
            score += 150 * games_and_results[6][1]
    if games_and_results[2][0] == True and games_and_results[2][1] != 0 and 4 not in nah:
        if games_and_results[2][1] == games_and_results[6][1] == -1*games_and_results[4][1]:    
        # print("wsg mate")
            score += 150 * games_and_results[4][1]
    
    for i in range (3):
        if games_and_results[3*i][0] == True and games_and_results[3*i][1] != 0 and 3*i+2 not in nah:
            if games_and_results[3*i][1] == games_and_results[3*i+1][1] == -1*games_and_results[3*i+2][1]:
                score -= 150 * games_and_results[3*i][1]
        if games_and_results[3*i][0] == True and games_and_results[3*i][1] != 0 and 3*i+1 not in nah:
            if games_and_results[3*i][1] == games_and_results[3*i+2][1] == -1*games_and_results[3*i+1][1]:
            # print("nah nah nah here")
                score -= 150 * games_and_results[3*i][1]
        if games_and_results[3*i+1][0] == True and games_and_results[3*i+1][1] != 0 and 3*i not in nah:
            if -1*games_and_results[3*i][1] == games_and_results[3*i+1][1] == games_and_results[3*i+2][1]:

            # print("nah nah nah here")
                score -= 150 * games_and_results[3*i+1][1]
            # return (True, games_and_results[3*i][1])
            
# =================================================================================

    wins = {0:[(1,2),(3,6),(4,8)],2:[(0,1),(5,8),(4,6)],6:[(7,8),(0,3),(4,2)],8:[(6,7),(2,5),(4,0)]}
    edgew = {1:[(0,2),(4,7)],3:[(4,5),(0,6)],5:[(3,4),(2,8)],7:[(6,8),(1,4)]}
    
    for key in wins.keys():  
        row, col, dig = False, False, False
        if games_and_results[key][0] and games_and_results[key][1] != 0:
            if -1*games_and_results[key][1] == games_and_results[wins[key][0][0]][1] or -1*games_and_results[key][1] == games_and_results[wins[key][0][1]][1]: row = True
            if -1*games_and_results[key][1] == games_and_results[wins[key][1][0]][1] or -1*games_and_results[key][1] == games_and_results[wins[key][1][1]][1]: col = True
            if -1*games_and_results[key][1] == games_and_results[wins[key][2][0]][1] or -1*games_and_results[key][1] == games_and_results[wins[key][2][1]][1]: dig = True
        if row and col and dig:score -= 150*games_and_results[key][1]
    
    for key in edgew.keys():
        row, col = False, False
        if games_and_results[key][0] and games_and_results[key][1] != 0:
            if -1*games_and_results[key][1] == games_and_results[edgew[key][0][0]][1] or -1*games_and_results[key][1] == games_and_results[edgew[key][0][1]][1]: row = True
            if -1*games_and_results[key][1] == games_and_results[edgew[key][1][0]][1] or -1*games_and_results[key][1] == games_and_results[edgew[key][1][1]][1]: col = True
        if row and col:score -= 150*games_and_results[key][1]
    # if games_and_results[0][]

    # w = score_small(token,board[9*num:9*num+9]) # WHY AN IF STATEMENT??
    # # print(token,num,score)
    # # print(board[9*num:9*num+9])
    # # print(w*0.12)
    # # print("double u")
    # if game_over_small(board[9*num:9*num+9])[0]:
    #     # print("GAME OVER")
    #     score -= 0.25*w
    # if token == "O" and -12 > w > -69:
    #     # print("bruh O " + str(-0.14*w))
    #     # print("bro  ")
    #     score -= 0.14*w # dalmations
    # elif token == "X" and 12 < w < 69:
    #     # print("bruh X " + str(-0.14*w))
    #     # print("bro  nahhh")
    #     score -= 0.14*w # dalmations
    # score += 0.12*w
    # print("fin " + str(score))

    return score


def score_small(token, board, victory = 1000, count = 2, two = 8, one_space_one = 4, one_diagonal_space_one = 5, center = 3, corner = 2): # scoring for smaller boards

    victory = 100
    count = 0
    two = 5
    one_space_one = 5
    one_diagonal_space_one = 5
    center = 0.0 # 5
    corner = 0.0 # 25
    block = 20

    score = 0

    count_x = board.count("X")
    count_o = board.count("O")

    count_x_2 = board.count("XX.") + board.count(".XX")
    count_o_2 = board.count("OO.") + board.count(".OO")

    count_x_1_1 = board.count("X.X")
    count_o_1_1 = board.count("O.O")

    if game_over_small(board)[0]:
        return victory *game_over_small(board)[1] #+

    score += count * (count_x-count_o)
    score += two * (count_x_2)
    score -= two * (count_o_2)
    score += one_space_one * (count_x_1_1-count_o_1_1)

    if board[4] == "X":
        score += center
    elif board[4] == "O":
        score -= center

    for x in [0,2,6,8]:
        if board[x] == "X":
            score += corner
        elif board[x] == "O":
            score -= corner
    
    if board[0] == "X" and board[8] == "X" and board[4] != "X" and board[4] != "O":
        score += one_diagonal_space_one
    elif board[0] == "O" and board[8] == "O" and board[4] != "O" and board[4] != "X":
        score -= one_diagonal_space_one

    if board[2] == "X" and board[6] == "X" and board[4] != "X" and board[4] != "O":
        score += one_diagonal_space_one
    elif board[2] == "O" and board[6] == "O" and board[4] != "O" and board[4] != "X":
        score -= one_diagonal_space_one

    for i in range(3):
        if ("X" == board[i] == board[i+3] and board[i+6] == ".") or ("X" == board[i] == board[i+6] and board[i+3] == ".") or "X" == board[i+6] == board[i+3] and board[i+0] == ".":
            score += two
        elif ("O" == board[i] == board[i+3] and board[i+6] == ".") or ("O" == board[i] == board[i+6] and board[i+3] == ".") or "O" == board[i+6] == board[i+3] and board[i+0] == ".":
            score -= two
            
# ============================================
    # if board[0] == "X" and board[8] == "X" and board[4] != "X" and board[4] == "O":
    #     score += block
    # elif board[0] == "O" and board[8] == "O" and board[4] != "O" and board[4] == "X":
    #     score -= block

    # if board[2] == "X" and board[6] == "X" and board[4] != "X" and board[4] == "O":
    #     score += block
    # elif board[2] == "O" and board[6] == "O" and board[4] != "O" and board[4] == "X":
    #     score -= block

    # for i in range(3):
    #     if ("X" == board[i] == board[i+3] and board[i+6] == "O") or ("X" == board[i] == board[i+6] and board[i+3] == "O") or "X" == board[i+6] == board[i+3] and board[i+0] == "O":
    #         score += block
    #     elif ("O" == board[i] == board[i+3] and board[i+6] == "X") or ("O" == board[i] == board[i+6] and board[i+3] == "X") or "O" == board[i+6] == board[i+3] and board[i+0] == "X":
    #         score -= block
            
        

# ==================================================================================

    wins = {0:[(1,2),(3,6),(4,8)],2:[(0,1),(5,8),(4,6)],6:[(7,8),(0,3),(4,2)],8:[(6,7),(2,5),(4,0)]}
    edgew = {1:[(0,2),(4,7)],3:[(4,5),(0,6)],5:[(3,4),(2,8)],7:[(6,8),(1,4)]}
    
    for key in wins.keys():  
        row, col, dig = False, False, False
        # input(wins[key][0][1])
        if board[key] != ".":
            if opponent(board[key]) == board[wins[key][0][0]] == board[wins[key][0][1]]: row = True
            if opponent(board[key]) == board[wins[key][1][0]] == board[wins[key][1][1]]: col = True
            if opponent(board[key]) == board[wins[key][2][0]] == board[wins[key][2][1]]: dig = True
        if row and col and dig: 
            score += block*winner(board[key])
    
    for key in edgew.keys():  
        row, col = False, False
        if board[key] != ".":
            if opponent(board[key]) == board[edgew[key][0][0]] == board[edgew[key][0][1]]: row = True
            if opponent(board[key]) == board[edgew[key][1][0]] == board[edgew[key][1][1]]: col = True
        if row and col: 
            score += block*winner(board[key])

    wins = {0:[(1,2),(3,6),(4,8)],2:[(0,1),(5,8),(4,6)],6:[(7,8),(0,3),(4,2)],8:[(6,7),(2,5),(4,0)]}
    edgew = {1:[(0,2),(4,7)],3:[(4,5),(0,6)],5:[(3,4),(2,8)],7:[(6,8),(1,4)]}
    
    for key in wins.keys():
        row, col, dig = False, False, False
        # input()
        if board[key] and board[key] != 0:
            if opponent(board[key]) == board[wins[key][0][0]] or opponent(board[key]) == board[wins[key][0][1]]: row = True
            if opponent(board[key]) == board[wins[key][1][0]] or opponent(board[key]) == board[wins[key][1][1]]: col = True
            if opponent(board[key]) == board[wins[key][2][0]] or opponent(board[key]) == board[wins[key][2][1]]: dig = True
        if row and col and dig:score -= block*winner(board[key])
    
    for key in edgew.keys():
        row, col = False, False
        if board[key] and board[key] != 0:
            if opponent(board[key]) == board[edgew[key][0][0]] or opponent(board[key]) == board[edgew[key][0][1]]: row = True
            if opponent(board[key]) == board[edgew[key][1][0]] or opponent(board[key]) == board[edgew[key][1][1]]: col = True
        if row and col:score -= block*winner(board[key])

    # score += winner(token)

    return score

def possible_moves(board,num): # num = -1 means the game has just started (can play anywhere)

    possibles = list()
    if num == -1:
        return [i for i in range(81)]
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
                possibles.append((i,stri))
        # return [i for i in range(0,64)]
        return possibles
    start_index = 9*num
    for i in range(start_index,start_index+9):
        if (board[i] == "."):
                new_board = board.copy()
                new_board[i] = token
                stri = "".join(str(x) for x in new_board)
                possibles.append((i,stri))
    # print("\n".join(x for x in possibles))
    return possibles

def make_move(board, token, index):
    if index == -1: return (board,-1)
    board = list(board)
    board[index] = token
    return ("".join(str(x) for x in board),index%9)

def aggressive(board, possibles, token, num):
    
    if num == -1: return choice(possibles)

    if game_over_small(board[9*num:9*num+9])[0]:
        for i in range (9):
            if not game_over_small(board[9*i:9*i+9])[0]: num = i
    pos_next_boards = possible_next_boards(board,token,num)
    results = list()
    moves = dict()
    for x in pos_next_boards:
        # results.append((score_small(x[1][9*num:9*num+9]),x[0]))
        moves[x] = score_small(".",x[1][9*num:9*num+9]),x[0]
        # if game_over_small(x[1][9*num:9*num+9])[0]:
        #     return x[0]
    if len(results) != 0:
        if token == "O": return min(results, key=moves.get)
        return max(results, key=moves.get)
    # if token == "X": return max(results)
    # else: return min(results)
    return choice(possibles)

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
    if games_and_results[2][0] == True and games_and_results[2][1] != 0 and games_and_results[2][1] == games_and_results[4][1] == games_and_results[6][1]:
        # print("nah nah here")
        return (True, games_and_results[2][1])  

    for i in range (3):
        if (games_and_results[3*i][0] == True and games_and_results[3*i][1] != 0 and games_and_results[3*i][1] == games_and_results[3*i+1][1] == games_and_results[3*i+2][1]):
            # print("nah nah nah here")
            return (True, games_and_results[3*i][1])

    if not "." in board:
        # print("nah nah nah nah here")
        return (True, 0)

    return (False, None) # (False, None)
    return (False,None)

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

def game_over_board_indexes(board):
    blank = "................................................................................."
    cant_move_to = list()
    for i in range (9):
        if game_over_small(board[9*i:9*i+9])[0]:
            for x in possible_moves(blank,i):
                cant_move_to.append(x)
    return cant_move_to


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

def opponent(token):
    if token == "O": return "X"
    return "O"

def min_step(board,token,depth, alpha, beta, num, possibles):
    
    if depth == 0 or game_over(board)[0]:
        return scoring(num, board, "X", victory = 100, count = 2, two = 8, one_space_one = 4, one_diagonal_space_one = 5, center = 3, corner = 2)

    if num != -1:
        if game_over_small(board[9*num:9*num+9])[0]:
            p = list()
            cant = game_over_board_indexes(board)
            # input(str(cant))
            for i,v in enumerate(board):
                if v == "." and i not in cant: p.append(i)
            possibles = p
        else: possibles = possible_moves(board,num)
    if possible_moves(board, num) == 0:
        return max_step(board,opponent(token),depth-1,alpha,beta,num,possibles)

    results = list()
    for x in possibles:
        results.append(max_step(make_move(board,token,x)[0],opponent(token),depth-1,alpha,beta,num,possibles))
        pru = min(results) # ALPHA/BETA PRUNING HERE
        beta = min(pru,beta) # ALPHA/BETA PRUNING HERE
        if alpha >= pru: break # ALPHA/BETA PRUNING HERE
        # if next < beta:
        #     beta = next
        # if alpha >= beta: break
    # return beta
    #     results.append(max_step(make_move(board,token,x)[0],opponent(token),depth-1,alpha,beta,num,possibles))
    #     pru = min(results) # ALPHA/BETA PRUNING HERE
    #     beta = min(pru,beta) # ALPHA/BETA PRUNING HERE
    #     if alpha >= pru: break # ALPHA/BETA PRUNING HERE
    

    return min(results)

def max_step(board,token,depth, alpha, beta, num, possibles):
    
    if depth == 0 or game_over(board)[0]:
        return scoring(num, board, "O", victory = 100, count = 1, two = 5, one_space_one = 4, one_diagonal_space_one = 5, center = 3, corner = 1)

    if num != -1:
        if game_over_small(board[9*num:9*num+9])[0]:
            p = list()
            cant = game_over_board_indexes(board)
            # input(str(cant))
            for i,v in enumerate(board):
                if v == "." and i not in cant: p.append(i)
            possibles = p
        else: possibles = possible_moves(board,num)
    if possible_moves(board, num) == 0:
        return min_step(board,opponent(token),depth-1,alpha,beta,num,possibles)

    results = list()
    for x in possibles:
        results.append(min_step(make_move(board,token,x)[0],opponent(token),depth-1,alpha,beta,num,possibles))
        # if alpha < next:
        #     alpha = next
        # if alpha >= beta: break
        pru = max(results) # ALPHA/BETA PRUNING HERE
        alpha = max(pru,alpha) # ALPHA/BETA PRUNING HERE
        if beta <= pru: break # ALPHA/BETA PRUNING HERE
    # return alpha
    #     results.append(min_step(make_move(board,token,x)[0],opponent(token),depth-1,alpha,beta,num,possibles))
    #     pru = max(results) # ALPHA/BETA PRUNING HERE
    #     alpha = max(pru,alpha) # ALPHA/BETA PRUNING HERE
    #     if beta <= pru: break # ALPHA/BETA PRUNING HERE
    return max(results)

def find_next_move(board,token,depth,num,possibles):
    alpha = float("-inf")
    beta = float("inf")
    if num != -1:
        if game_over_small(board[9*num:9*num+9])[0]:
            p = list()
            cant = game_over_board_indexes(board)
            # input(str(cant))
            for i,v in enumerate(board):
                if v == "." and i not in cant: p.append(i)
            possibles = p
        else: possibles = possible_moves(board,num)
    moves = dict()
    results = list()
    for x in possibles:
        if token == "X":
            moves[x] = min_step(make_move(board,token,x)[0],opponent(token),depth-1,alpha,beta,make_move(board,token,x)[1],possibles)
            # moves.update({x: min_step(make_move(board,token,x),'xo'['ox'.index(token)],depth-1,alpha,beta)})
        else:
            moves[x] = max_step(make_move(board,token,x)[0],opponent(token),depth-1,alpha,beta,make_move(board,token,x)[1],possibles)
            # moves.update(x,max_step(make_move(board,token,x),'xo'['ox'.index(token)],depth-1,alpha,beta))
    if token == "X":
        # input("X"+str(moves[max(moves, key = moves.get)]))
        return max(moves, key = moves.get)
    else: 
        # input("O"+str(moves[min(moves, key = moves.get)]))
        return min(moves, key = moves.get) # WHAT IF ITS A DOT

# display("XXX............XXX....XX...............XXX....................................XXX")

# print(score("XXX............XXX....XX...............XXX....................................XXX"))

def run_game(players):
    print(players)
    board = "................................................................................."
    # display(board)
    input("\nRules for Ultimate Tic Tac Toe:")
    # input("Chose a number from the possible moves to make your move.")
    input("Use the board of indexes/possible moves to decided where you want to move to")
    input("Where you move on the small board directly corresponds to where your opponent plays next")
    input("If your opponent sends you to a board that is already over, you can play anywhere except those boards")
    input("The goal is to win three different games in a row, column, or diagonal")
    # display(board)
    # display_index_board()


    # first_move = input("Enter the first move for X (Type in any index from the board)  ")
    tac = make_move(board,"X",-1)
    print(tac)

    X_turn(tac, players)
    # run_game(players)



def O_turn(tictactoe, players):
    if players[1] == "USER":
        O_turn_human(tictactoe, players)
    elif players[1] == "RANDOM":
        O_turn_random(tictactoe, players)
    elif players[1] == "AGGRESSIVE":
        O_turn_aggressive(tictactoe,players)
    elif players[1] == "BEST":
        O_turn_best(tictactoe,players)
    else:
        print("NOT A VALID PLAYER: ENDING GAME")

def X_turn(tictactoe, players):
    if players[0] == "USER":
        X_turn_human(tictactoe, players)
    elif players[0] == "RANDOM":
        X_turn_random(tictactoe, players)
    elif players[0] == "AGGRESSIVE":
        X_turn_aggressive(tictactoe,players)
    elif players[0] == "BEST":
        X_turn_best(tictactoe,players)
    else:
        print("NOT A VALID PLAYER: ENDING GAME")

def O_turn_human(toe, players):
    display(toe[0])
    display_index_board()

    if toe[1] != -1:
        if game_over_small(toe[0][9*toe[1]:9*toe[1]+9])[0]:
            p = list()
            cant = game_over_board_indexes(toe[0])
            for i,v in enumerate(toe[0]):
                if v == "." and i not in cant: p.append(i) # in [ind for ind in range(9*toe[1],9*toe[1]+9)]
            print("Possible moves for O: " + str(p))
        else: print("Possible moves for O: " + str(p:= possible_moves(toe[0],toe[1])))
    else: print("Possible moves for O: " + str(p:= possible_moves(toe[0],toe[1])))
    # toe[0][9*toe[1]:9*toe[1]+9]
    if len(p) == 0: move = -1
    else: move = input("Enter the move for O from the possible moves:  ")
    while move == "" or int(move) not in p:
        move = input("Enter the move for O from the possible moves:  ")
    moved = make_move(toe[0],"O",int(move))
    if not game_over(moved[0])[0]:
        # input("SCORES o   " + str(scoring(moved[1],moved[0])))
        X_turn(moved, players)
    else:
        display(moved[0])
        print("Game Over")
        w = game_over(moved[0])[1]
        print(who_winner(w))

def X_turn_human(tic, players):
    display(tic[0])
    display_index_board()
    
    if tic[1] != -1:
        if game_over_small(tic[0][9*tic[1]:9*tic[1]+9])[0]:
            p = list()
            cant = game_over_board_indexes(tic[0])
            for i,v in enumerate(tic[0]):
                if v == "." and i not in cant: p.append(i) # in [ind for ind in range(9*tic[1],9*tic[1]+9)]
            print("Possible moves for X: " + str(p))
        else: print("Possible moves for X: " + str(p:= possible_moves(tic[0],tic[1])))
    else: print("Possible moves for X: " + str(p:= possible_moves(tic[0],tic[1])))
    # toe[0][9*toe[1]:9*toe[1]+9]
    if len(p) == 0: move = -1
    else: move = input("Enter the move for X from the possible moves:  ")
    while move == "" or int(move) not in p or move == "":
        move = input("Enter the move for X from the possible moves:  ")
    moved = make_move(tic[0],"X",int(move))
    if not game_over(moved[0])[0]:
        # input("SCORE x   " + str(scoring(moved[1],moved[0])))
        O_turn(moved, players)
    else:
        display(moved[0])
        print("Game Over")
        w = game_over(moved[0])[1]
        print(who_winner(w))

def O_turn_random(tac, players):
    display(tac[0])
    display_index_board()

    if tac[1] != -1:
        if game_over_small(tac[0][9*tac[1]:9*tac[1]+9])[0]:
            p = list()
            cant = game_over_board_indexes(tac[0])
            # input(str(cant))
            for i,v in enumerate(tac[0]):
                if v == "." and i not in cant: p.append(i)
            print("Possible moves for O: " + str(p))
        else: print("Possible moves for O: " + str(p:= possible_moves(tac[0],tac[1])))
    else: print("Possible moves for O: " + str(p:= possible_moves(tac[0],tac[1])))
    # toe[0][9*toe[1]:9*toe[1]+9]
    if len(p) == 0: move = -1
    else: move = choice(p)
    print("RANDOM chooses to play O at: " + str(move))
    # while int(move) not in p:
    #     move = input("Enter the move for O from the possible moves:  ")
    moved = make_move(tac[0],"O",int(move))
    if not game_over(moved[0])[0]:
        X_turn(moved, players)
    else:
        display(moved[0])
        print("Game Over")
        w = game_over(moved[0])[1]
        print(who_winner(w))

def X_turn_random(tac, players):
    display(tac[0])
    display_index_board()

    if tac[1] != -1:
        if game_over_small(tac[0][9*tac[1]:9*tac[1]+9])[0]:
            p = list()
            cant = game_over_board_indexes(tac[0])
            for i,v in enumerate(tac[0]):
                if v == "." and i not in cant: p.append(i) # in [ind for ind in range(9*tac[1],9*tac[1]+9)]
            print("Possible moves for X: " + str(p))
        else: print("Possible moves for X: " + str(p:= possible_moves(tac[0],tac[1])))
    else: print("Possible moves for X: " + str(p:= possible_moves(tac[0],tac[1])))
    # toe[0][9*toe[1]:9*toe[1]+9]
    if len(p) == 0: move = -1
    else: move = choice(p)
    print("RANDOM chooses to play X at: " + str(move))
    # while int(move) not in p:
    #     move = input("Enter the move for O from the possible moves:  ")
    moved = make_move(tac[0],"X",int(move))
    if not game_over(moved[0])[0]:
        # input(scoring(moved[1],moved[0]))
        O_turn(moved, players)
    else:
        display(moved[0])
        print("Game Over")
        w = game_over(moved[0])[1]
        print(who_winner(w))

def O_turn_aggressive(tac, players):
    display(tac[0])
    display_index_board()

    if tac[1] != -1:
        if game_over_small(tac[0][9*tac[1]:9*tac[1]+9])[0]:
            p = list()
            cant = game_over_board_indexes(tac[0])
            for i,v in enumerate(tac[0]):
                if v == "." and i not in cant: p.append(i)
            print("Possible moves for O: " + str(p))
        else: print("Possible moves for O: " + str(p:= possible_moves(tac[0],tac[1])))
    else: print("Possible moves for O: " + str(p:= possible_moves(tac[0],tac[1])))
    # toe[0][9*toe[1]:9*toe[1]+9]
    if len(p) == 0: move = -1
    else: move = aggressive(tac[0],p,"O",tac[1])
    print("AGGRESIVE chooses to play O at: " + str(move))
    # while int(move) not in p:
    #     move = input("Enter the move for O from the possible moves:  ")
    moved = make_move(tac[0],"O",int(move))
    if not game_over(moved[0])[0]:
        X_turn(moved, players)
    else:
        display(moved[0])
        print("Game Over")
        w = game_over(moved[0])[1]
        print(who_winner(w))

def X_turn_aggressive(tac, players):
    display(tac[0])
    display_index_board()

    if tac[1] != -1:
        if game_over_small(tac[0][9*tac[1]:9*tac[1]+9])[0]:
            p = list()
            cant = game_over_board_indexes(tac[0])
            for i,v in enumerate(tac[0]):
                if v == "." and i not in cant: p.append(i)
            print("Possible moves for X: " + str(p))
        else: print("Possible moves for X: " + str(p:= possible_moves(tac[0],tac[1])))
    else: print("Possible moves for X: " + str(p:= possible_moves(tac[0],tac[1])))
    # toe[0][9*toe[1]:9*toe[1]+9]
    if len(p) == 0: move = -1
    else: move = aggressive(tac[0],p,"X",tac[1])
    print("AGGRESIVE chooses to play X at: " + str(move))
    # while int(move) not in p:
    #     move = input("Enter the move for O from the possible moves:  ")
    moved = make_move(tac[0],"X",int(move))
    if not game_over(moved[0])[0]:
        O_turn(moved, players)
    else:
        display(moved[0])
        print("Game Over")
        w = game_over(moved[0])[1]
        print(who_winner(w))

def O_turn_best(tac, players):
    display(tac[0])
    display_index_board()

    if tac[1] != -1:
        if game_over_small(tac[0][9*tac[1]:9*tac[1]+9])[0]:
            p = list()
            cant = game_over_board_indexes(tac[0])
            for i,v in enumerate(tac[0]):
                if v == "." and i not in cant: p.append(i)
            print("Possible moves for O: " + str(p))
        else: print("Possible moves for O: " + str(p:= possible_moves(tac[0],tac[1])))
    else: print("Possible moves for O: " + str(p:= possible_moves(tac[0],tac[1])))
    # toe[0][9*toe[1]:9*toe[1]+9]
    if len(p) == 0: move = -1
    else: move = find_next_move(tac[0],"O",5,tac[1],p)
    print("BEST chooses to play O at: " + str(move))
    # while int(move) not in p:
    #     move = input("Enter the move for O from the possible moves:  ")
    moved = make_move(tac[0],"O",int(move))
    if not game_over(moved[0])[0]:
        X_turn(moved, players)
    else:
        display(moved[0])
        print("Game Over")
        w = game_over(moved[0])[1]
        print(who_winner(w))

def X_turn_best(tac, players):
    display(tac[0])
    print("here")
    display_index_board()

    if tac[1] != -1:
        if game_over_small(tac[0][9*tac[1]:9*tac[1]+9])[0]:
            p = list()
            cant = game_over_board_indexes(tac[0])
            # input(str(cant))
            for i,v in enumerate(tac[0]):
                if v == "." and i not in cant: p.append(i)
            print("Possible moves for X: " + str(p))
        else: print("Possible moves for X: " + str(p:= possible_moves(tac[0],tac[1])))
    else: print("Possible moves for X: " + str(p:= possible_moves(tac[0],tac[1])))
    # toe[0][9*toe[1]:9*toe[1]+9]
    if len(p) == 0: move = -1
    else: move = find_next_move(tac[0],"X",5,tac[1],p)
    print("BEST chooses to play X at: " + str(move))
    # while int(move) not in p:
    #     move = input("Enter the move for O from the possible moves:  ")
    moved = make_move(tac[0],"X",int(move))
    if not game_over(moved[0])[0]:
        O_turn(moved, players)
    else:
        display(moved[0])
        print("Game Over")
        w = game_over(moved[0])[1]
        print(who_winner(w))

def make_test_cases(board, token):
    move = input("whats the move")
    input("token +" + token)
    if str(move) != "STOP":
        display_index_board()
        display(w := make_move(board,token,int(move))[0])
        make_test_cases(w,opponent(token))
        print(board)
    return board
# display_index_board()
# # 

# x = make_test_cases(ultimate_board,"X")
# print(x)
# display("O.X.X......O......O.OX..X..........OO...X.O............XX...O...........X........")
# for i in range(9):
#     print("  " +  str(scoring(i,"O.X.X......O......O.OX..X..........OO...X.O............XX...O...........X........","O")))
# print(game_over_board_indexes(ultimate_board))




run_game(players)