import sys

de = set()

bounds = int(sys.argv[2])

oro = "" if len(sys.argv)<  4 else str(sys.argv[3])

with open(sys.argv[1]) as f:
    lines = [line.strip() for line in f]

def run_game(l): return "Next player can guarantee victory by playing any of these letters:" + str(l) if len(l) != 0 else "Next player will lose!"

def f_m (startword): #find moves
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    if startword == "": return alphabet
    else: return mooves[startword]

for word in lines:
    if len(word) >= bounds and word.isalpha(): de.add(word.upper())

player = "ODD" if len(oro) % 2 != 0 else "EVEN"

def move (d):
    moves = dict()

    for DI in d:
        moves[DI] = ["XXXXXXXX"]
        for i in range(abs(1-len(DI))):
            if DI[0:i+1] in moves:
                if DI[0:i+2] not in moves[DI[0:i+1]]: moves[DI[0:i+1]].append(DI[0:i+2])
            else: moves[DI[0:i+1]] = [DI[0:i+2]]   

    for i in d:
        if i in moves:
            moves[i] = []   




    return moves

mooves = move(de)

def game_over(board):
    if board in de:
        i = len(board) % 2
        if i == 0: return -1 if player == "ODD" else 1
        if i != 0: return -1 if player == "EVEN" else 1
    return None

def max_step(thing):
    if not None == game_over(thing): return game_over(thing)
    lis = list()
    for x in f_m(thing): lis.append(min_step(x))
    m = max(lis)
    return m

def min_step(thing):
    if not None == game_over(thing): return game_over(thing)
    lis = list()
    for x in f_m(thing): lis.append(max_step(x))
    m = min(lis)
    return m
    
def lisst(vocab):
    moves = list()
    for x in f_m(vocab):
        l = len(x)
        moves.append([w := min_step(x), x]) if l<=1 else moves.append([w := min_step(x), x[-1]])
    lis = list()
    for x in moves:
        if not x[0] != 1: lis.append(x[1])
    return sorted(lis)

string = run_game(lisst(oro))
print(string)





















