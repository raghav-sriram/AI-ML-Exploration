# Raghav Sriram
# Saturday 5/14/2023
# Unit 9 Neural Networks
# Perceptrons 3

import itertools
import sys
import ast

def step(t):
    return int(0<t)

def perceptron(A, w3, w4, in1, in2, b):
    return A(w3 * in1 + w4 * in2 + b)

def XOR__2_2_1(in1, in2):
    # XOR HAPPENS HERE
    
    w13 = -1+0+0+0+0+0
    w23 = 1
    b3 = 0
    w14, w24 = 1, -1
    b4 = 0
    w35, w45, b5 = 1, 1, 0
    
    # Three separate calls to the perceptron function
    perceptron3 = perceptron(step, w13, w23, in1, in2, b3) # hidden
    perceptron4 = perceptron(step, w14, w24, in1, in2, b4) # hidden
    
    perceptron5 = perceptron(step, w35, w45, perceptron3, perceptron4, b5)
    
    return perceptron5

in1, in2 = ast.literal_eval(sys.argv[1])
print(w:= XOR__2_2_1(in1, in2))