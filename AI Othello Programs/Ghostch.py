import sys


bounds = int(sys.argv[2])

sett = set()
with open(sys.argv[1]) as f: l = [line.strip() for line in f]


for w in l:
    if len(w) >= bounds and w.isalpha():
        sett.add(w.upper())

wordthing = "" if len(sys.argv)<4 else str(sys.argv[3])
player = "EVEN" if len(wordthing) % 2 == 0 else "ODD"


def mover (webster):
    ok = {}
    for x in webster:
        ok[x] = ["XXXXXXXX"]
        bou = len(x) -1
        for i in range(0,bou):
            if x[0:i+1] in ok:
                if not x[0:2+i] in ok[x[0:1+i]]: 
                    ok[x[0:1+i]].append(x[0:2+i])
            else: 
                
                ok[x[0:i+1]] = [x[0:i+2]]   

    for i in webster:
        if i in ok == True: ok[i] = list()   



    return ok

mo = mover(sett)

def game_over(board):
    if board in sett:
        if 0 == len(board) % 2 == 0: 
            return 1 if player == "EVEN" else -1*1
        if not 0 == len(board) % 2: 
            return -1 if player == "EVEN" else 1*1
    else:
    
        return None

def movess (word):
    return list("ABCDEFGHIJKLMNOPQRSTUVWXYZ") if word == "" else mo[word]

def min_step(token):
    if None != game_over(token): return game_over(token)
    r = list()
    for rr in movess(token): r.append(max_step(rr))
    minimum = min(r)
    return minimum
    
def max_step(token):
    if None != game_over(token): return game_over(token)
    r = []
    for rr in movess(token):
        r.append(min_step(rr))
    return max(r)

def sortedl(word):
    moves = list()
    for x in movess(word):
        min__step = min_step(x)
        moves.append([min__step, x[-1]]) if len(x)>1 else moves.append([min__step, x])
    r = []
    for mmm in moves:
        if mmm[0] == 1: r.append(mmm[1])
    return r


def run(l): 
    if len(l) != 0:
        return "Next player can guarantee victory by playing any of these letters:" + str(l)
    else: return "Next player will lose!"


print(run(sortedl(wordthing)))