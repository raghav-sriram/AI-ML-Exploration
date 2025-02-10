# Raghav Sriram
# Saturday 5/13/2023
# Unit 9 Neural Networks
# Perceptrons 2

import itertools
import sys
import ast
import numpy as np
import matplotlib.pyplot as plt

def step(t):
    return int(0<t)

def perceptron(A, w, b, x):
    dp = sum([w[i]*x[i] for i in range(len(x))])
    return A(dp+b)

def truth_table(bits, n):
    binary = str(bin(n))[2:]
    right_side = "0" * ((2 ** bits) - len(binary)) + binary
    right_side = list(map(int, right_side))

    truth = list(itertools.product([1, 0], repeat=bits))
    return tuple(zip(truth, right_side))

def generate_truth_tables(bits):
    distinct = 2**(2**bits)
    llrate = 1
    # print (distinct)
    accurate_count = 0
    # return [truth_table(bits,canon) for canon in range(distinct)]
    truth_tables = list() 
    for canon in range(distinct):
        tt = truth_table(bits,canon)
        w,b = train(bits,tt,llrate)
        # print(tt,w,b)
        # input()
        accr = accuracy(tt,w,b)
        if accr == 1.0:
            accurate_count = accurate_count + 1
        
            
        # truth_tables.append(truth_table(bits,canon))
    # return truth_tables
    print(f"{distinct} possible functions; {accurate_count} can be correctly modeled")
    
    
def train(bits, tt, llrate):
    
    w = [0]*bits #weights
    b = 0 #bias

    for epochs in range(100):
        total_error = 0
        for x in tt:
            output = perceptron(step,w, b, x[0])
            error = x[1] - output
            total_error += abs(x[1] - output)

            for i in range(len(w)): w[i] += error * llrate * x[0][i]
            b += error * llrate

        if total_error == 0: break
    return w,b

def accuracy(tt, w, b):
    accurate = 0
    for x in tt:
        if perceptron(step, w, b, x[0]) == x[1]: accurate += 1
    return accurate / len(tt)

bits = int(sys.argv[1])
canonint = int(sys.argv[2])
llrate = 1
# gen = generate_truth_tables(bits)
tt = truth_table(bits,canonint)
w,b = train(bits,tt,llrate)
accurate = accuracy(tt,w,b)*100
print("Weight vector:",w)
print("Bias:",b)
print("Accuracy (%):",accurate)