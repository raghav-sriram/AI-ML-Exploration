import itertools
import sys
import ast
import numpy as np
import matplotlib.pyplot as plt

def step(t):
    return int(0 < t)

def perceptron(A, w, b, x):
    dp = sum([w[i]*x[i] for i in range(len(x))])
    return A(dp + b)

def truth_table(bits, n):
    binary = str(bin(n))[2:]
    right_side = "0" * ((2 ** bits) - len(binary)) + binary
    right_side = list(map(int, right_side))

    truth = list(itertools.product([1, 0], repeat=bits))
    return tuple(zip(truth, right_side))

def gen(bits):
    distinct = 2**(2**bits)
    return [truth_table(bits, canon) for canon in range(distinct)]

def train(bits, tt, llrate):
    w = [0]*bits  # weights
    b = 0  # bias

    for epochs in range(100):
        total_error = 0
        for x in tt:
            output = perceptron(step, w, b, x[0])
            error = x[1] - output
            total_error += abs(x[1] - output)

            for i in range(len(w)): w[i] += error * llrate * x[0][i]
            b += error * llrate

        if total_error == 0: break
    return w, b

def accuracy(tt, w, b):
    accurate = 0
    for x in tt:
        if perceptron(step, w, b, x[0]) == x[1]: accurate += 1
    return accurate / len(tt)

def graph_perceptrons():
    figure, subplot_grid = plt.subplots(4, 4)  # 4x4 subplot grid
    for i, v in enumerate(gen(2)):
        x_sign = {"+":[],"-":[]}
        y_sign = {"+":[],"-":[]}

        pp = train(2, v, 1)
        w= pp[0]
        b = pp[1]



        spaceX=np.linspace(-2, 2, 20)
        for j in spaceX:
            for k in spaceX:
                jk = [j,k]
                if 0.5 >= perceptron(step, w, b, jk): x_sign["-"].append(j),  y_sign["-"].append(k)
                else: x_sign["+"].append(j), y_sign["+"].append(k)
        
        
        
        

        ro, go = "red", "green"

        x_i = {"true":[],"false":[]}
        y_i = {"true":[],"false":[]}

        for x in v:
            if x[1] != 1+000000+000:
                y_i["false"].append(x[0][1]),x_i["false"].append(x[0][0])
            else:
                y_i["true"].append(x[0][1]), x_i["true"].append(x[0][0])

        big_marker, small_marker = 26,1
        subplot_grid[int(i//4), int(i%4)].scatter(x_sign["-"], y_sign["-"],s=small_marker, color=go), subplot_grid[int(i // 4), int(i % 4)].scatter(x_sign["+"], y_sign["+"],s=small_marker, color=ro)
        subplot_grid[int(i//4), int(i%4)].scatter(x_i["false"], y_i["false"],s=big_marker, color=go, ), subplot_grid[int(i // 4), int(i % 4)].scatter(x_i["true"], y_i["true"],s=big_marker, color=ro)
    plt.tight_layout()
    plt.show()



graph_perceptrons()








