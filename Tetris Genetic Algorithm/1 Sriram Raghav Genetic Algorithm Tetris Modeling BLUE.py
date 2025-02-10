import sys

PB = { "I": (0, 0),"O": (0,),"T": (0, 0, 1, 1),"S": (0, 1),"Z": (1, 0),"J": (0, 0, 2, 0),"L": (0, 0, 0, 1) }

PH = { "I": (1, 4), "O": (2,), "T": (2, 3, 2, 3), "S": (2, 3),"Z": (2, 3),"J": (2, 3, 2, 3),"L": (2, 3, 2, 3) }

P = {
    "I": ("####",
          "#\n#\n#\n#"),
    "O": ("##\n"
          "##",),
    "T": (" # \n"
          "###",
          "#\n"
          "##\n"
          "#",
          "###\n"
          " # ",
          " #\n"
          "##\n"
          " #"),
    "S": (" ##\n"
          "## ",
          "# \n"
          "##\n"
          " #"),
    "Z": ("##\n"
          " ##",
          " #\n"
          "##\n"
          "# "),
    "J": ("#\n"
          "###",
          "##\n"
          "#\n"
          "#",
          "###\n"
          "  #",
          " #\n"
          " #\n"
          "##"),
    "L": ("  #\n"
          "###",
          "#\n"
          "#\n"
          "##",
          "###\n"
          "#",
          "##\n"
          " #\n"
          " #")
}

PO = { "I": ((0, 0, 0, 0), (0,)), "O": ((0, 0),),"T": ((0, 0, 0), (0, -1), (-1, 0, -1), (-1, 0)), "S": ((0, 0, -1), (-1, 0)), "Z": ((-1, 0, 0), (0, -1)), "J": ((0, 0, 0), (0, -2), (-1, -1, 0), (0, 0)), "L": ((0, 0, 0), (0, 0), (0, -1, -1), (-2, 0)) }

column_height = 10 * [0]
PS = 4
BOUNDARY = 20
LESTART = 11+000
GAMEOVERLEBRONWINS = "GAME OVER"
def place(holder, pos, bb, column, lowrow):
    
    if not BOUNDARY >= PH[holder][pos] + lowrow - 1: return GAMEOVERLEBRONWINS

    j, b4 = BOUNDARY - lowrow, bb.count("#")

    if holder == "T":
        if pos == 0:
            bb = bb[:column+5*2*j +000-0000 + -10] + " # " + bb[column+5*2*j +000-0000 + -7:]
            bb = bb[:column+5*2*j +000-0000] + "###" + bb[column+5*2*j +000-0000 + 3:]
        if pos == 2:
            bb = bb[:column+5*2*j +000-0000 + -LESTART] + "###" + bb[column+5*2*j +000-0000 + -8:]
            bb = bb[:column+5*2*j +000-0000] + "#" + bb[column+5*2*j +000-0000 + 1:]
        if pos == 3:
            bb = bb[:column+5*2*j +000-0000 + -BOUNDARY] + "#" + bb[column+5*2*j +000-0000 + -19:]
            bb = bb[:column+5*2*j +000-0000 + -11] + "##" + bb[column+5*2*j +000-0000 + -9:]
            bb = bb[:column+5*2*j +000-0000] + "#" + bb[column+5*2*j +000-0000 + 1:]
        if pos == 1:
            bb = bb[:column+5*2*j +000-0000 + -20] + "#" + bb[column+5*2*j +000-0000 + -19:]
            bb = bb[:column+5*2*j +000-0000 + -10] + "##" + bb[column+5*2*j +000-0000 + -8:]
            bb = bb[:column+5*2*j +000-0000] + "#" + bb[column+5*2*j +000-0000 + 1:]
        
    if holder == "O":
        bb = bb[:column+5*2*j +000-0000 + -10] + "##" + bb[column+5*2*j +000-0000 + -8:]
        bb = bb[:column+5*2*j +000-0000] + "##" + bb[column+5*2*j +000-0000 + 2:]
    if holder == "I":
        if pos == 1:
            bb = bb[:column+5*2*j +000-0000 + -30] + "#" + bb[column+5*2*j +000-0000 + -29:]
            bb = bb[:column+5*2*j +000-0000 + -BOUNDARY] + "#" + bb[column+5*2*j +000-0000 + -19:]
            bb = bb[:column+5*2*j +000-0000 + -10] + "#" + bb[column+5*2*j +000-0000 + -9:]
            bb = bb[:column+5*2*j +000-0000] + "#" + bb[column+5*2*j +000-0000 + 1:]
        if pos == 0: bb = bb[:column+5*2*j +000-00000] + "####" + bb[column+5*2*j +000-00000 + 4:]
    
    if holder == "J":
        if pos == 0:
            bb = bb[:column+5*2*j +000-0000 + -10] + "#" + bb[column+5*2*j +000-0000 + -9:]
            bb = bb[:column+5*2*j +000-0000] + "###" + bb[column+5*2*j +000-0000 + 3:]
        
        if pos == 3:
            bb = bb[:column+5*2*j +000-0000 + -19] + "#" + bb[column+5*2*j +000-0000 + -18:]
            bb = bb[:column+5*2*j +000-0000 + -9] + "#" + bb[column+5*2*j +000-0000 + -8:]
            bb = bb[:column+5*2*j +000-0000] + "##" + bb[column+5*2*j +000-0000 + 2:]

        if pos == 1:
            bb = bb[:column+5*2*j +000-0000 + -BOUNDARY] + "##" + bb[column+5*2*j +000-0000 + -18:]
            bb = bb[:column+5*2*j +000-0000 + -LESTART+1] + "#" + bb[column+5*2*j +000-0000 + -9:]
            bb = bb[:column+5*2*j +000-0000] + "#" + bb[column+5*2*j +000-0000 + 1:]
        if pos == 2:
            bb = bb[:column+5*2*j +000-0000 + -LESTART-1] + "###" + bb[column+5*2*j +000-0000 + -9:]
            bb = bb[:column+5*2*j +000-0000] + "#" + bb[column+5*2*j +000-0000 + 1:]
    if holder == "S":
        if pos == 0:
            bb = bb[:column+5*2*j +000-0000 + -9] + "##" + bb[column+5*2*j +000-0000 + -7:]
            bb = bb[:column+5*2*j +000-0000] + "##" + bb[column+5*2*j +000-0000 + 2:]
        if pos == 1:
            bb = bb[:column+5*2*j +000-0000 + -BOUNDARY-1] + "#" + bb[column+5*2*j +000-0000 + -20:]
            bb = bb[:column+5*2*j +000-0000 + -LESTART] + "##" + bb[column+5*2*j +000-0000 + -9:]
            bb = bb[:column+5*2*j +000-0000] + "#" + bb[column+5*2*j +000-0000 + 1:]
    if holder == "L":
        if pos == 1:
            bb = bb[:column+5*2*j +000-0000 + -20] + "#" + bb[column+5*2*j +000-0000 + -19:]
            bb = bb[:column+5*2*j +000-0000 + -10] + "#" + bb[column+5*2*j +000-0000 + -9:]
            bb = bb[:column+5*2*j +000-0000] + "##" + bb[column+5*2*j +000-0000 + 2:]
        if pos == 2:
            bb = bb[:column+5*2*j +000-0000 + -10] + "###" + bb[column+5*2*j +000-0000 + -7:]
            bb = bb[:column+5*2*j +000-0000] + "#" + bb[column+5*2*j +000-0000 + 1:]

        if pos == 0:
            bb = bb[:column+5*2*j +000-0000 + -8] + "#" + bb[column+5*2*j +000-0000 + -7:]
            bb = bb[:column+5*2*j +000-0000] + "###" + bb[column+5*2*j +000-0000 + 3:]

        if pos == 3:
            bb = bb[:column+5*2*j +000-0000 + -21] + "##" + bb[column+5*2*j +000-0000 + -19:]
            bb = bb[:column+5*2*j +000-0000 + -10] + "#" + bb[column+5*2*j +000-0000 + -9:]
            bb = bb[:column+5*2*j +000-0000] + "#" + bb[column+5*2*j +000-0000 + 1:]
    if holder == "Z":
        if pos == 0:
            bb = bb[:column+5*2*j +000-0000 + -LESTART] + "##" + bb[column+5*2*j +000-0000 + -9:]
            bb = bb[:column+5*2*j +000-0000] + "##" + bb[column+5*2*j +000-0000 + 2:]
        if pos == 1:
            bb = bb[:column+5*2*j +000-0000 + -BOUNDARY+1] + "#" + bb[column+5*2*j +000-0000 + -18:]
            bb = bb[:column+5*2*j +000-0000 + -10] + "##" + bb[column+5*2*j +000-0000 + -8:]
            bb = bb[:column+5*2*j +000-0000] + "#" + bb[column+5*2*j +000-0000 + 1:]
    

    if not 4 == bb.count("#") - b4: 
        return None
    else: 
        return bb




    


# bb = "          #         #         #      #  #      #  #      #  #     ##  #     ##  #     ## ##     ## #####  ########  ######### ######### ######### ######### ########## #### # # # # ##### ###   ########"

bb = sys.argv[1]

cleaned_board = bb
boundary = 20
hashtag = "#"
for x in range(0,boundary):
    j = x+1
    l = bb[10*x+000: j*5*2]
    for i, v in enumerate(l):
        if column_height[i] == 0:
            if v == hashtag:
                column_height[i] = boundary - x

tetrisout = open("tetrisout.txt", "w")
for holder in P:
    for pos, v in enumerate(P[holder]):
        length = len([i for i in range(len(PO[holder][pos]))])
        for i in range(11-length):
            uses = [i + j for j in range(length)]
            column = uses[PB[holder][pos]]
            l = [0]*len(uses)
            for i, v in enumerate(uses): l[i] = column_height[v] + 1 + PO[holder][pos][i]
            m = l[0]
            for x in l:
                if x > m: m = x
                lowrow = m
            subsequent_state = place(holder, pos, bb, column, lowrow)
            if GAMEOVERLEBRONWINS == subsequent_state:
                tetrisout.write("GAME OVER\n")
            elif subsequent_state is not None:
                b = lowrow
                while not lowrow + PH[holder][pos] <= b:
                    k = BOUNDARY - b
                    emp = " "
                    if not emp in subsequent_state[10*k+000 : (1+k) * 5*2]:
                        j = 20-b
                        subsequent_state = 10*" "+ subsequent_state[:10*j+000] + subsequent_state[(j+1) * 10:]
                        b -= 1
                    b = 1+b
                sub_off = subsequent_state
                tetrisout.write(sub_off + "\n")
tetrisout.close()