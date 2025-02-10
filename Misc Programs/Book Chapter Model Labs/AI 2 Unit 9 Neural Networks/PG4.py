# Raghav Sriram
# Monday 5/15/2023
# Unit 9 Neural Networks
# Perceptrons 4

import numpy as np
import itertools
import sys
import ast
import random
import pickle

def truth_table(bits, n):
    binary = str(bin(n))[2:]
    right_side = "0"*(bits-len(binary)) + binary
    right_side = list(right_side)

    truth = list(itertools.product([1,0],repeat=bits))
    return tuple(zip(truth,right_side))

def step(t):
    return int(0<t)

def perceptron(A, w3, w4, in1, in2, b):
    return A(b+w3 * in1 + w4 * in2)


def p_net(A, w, b, x):
    
    # w = np.array([[-1,1],[1,-1]])
    # w5 = np.array([[1,1]])
    
    # b = np.array([[0],[0]])
    # b5 = np.array([[0]])

    A = np.vectorize(A)
    a = [np.array([])*len(w)]
    n = len(w)
    a[0] = x
    for i in range (1,n):
        a[i] = A(w[i] @ a[i-1] + b[i])
    return a[n]

    # perceptron3 = perceptron(step, w[0,0], w[0,1], in1, in2, b[0,0]) # hidden
    # perceptron4 = perceptron(step, w[1,0], w[1,1], in1, in2, b[0,1]) # hidden

    # perceptron5 = perceptron(step, b[0,0], b[0,1], perceptron3, perceptron4, b5[0,0])
    
#     # return perceptron5

def re_XOR(i):
    
    # w = np.array([[-1,1],[1,-1]])
    # w5 = np.array([[1,1]])
    
    # b = np.array([[0],[0]])
    # b5 = np.array([[0]])
    w = [np.array([[-1, 1], [1, -1]]), np.array([[1, 1]])]
    b = [np.array([[0], [0]]), np.array([[0]])]
    return p_net(step, i, w, b)[0]
    # perceptron3 = p_net(step,(in1, in2), w,b)    

    # # perceptron3 = perceptron(step, w[0,0], w[0,1], in1, in2, b[0,0]) # hidden
    # # perceptron4 = perceptron(step, w[1,0], w[1,1], in1, in2, b[0,1]) # hidden

    # # perceptron5 = perceptron(step, b[0,0], b[0,1], perceptron3, perceptron4, b5[0,0])
    
    # return perceptron5

def diamond(w,b):
    for i in np.arange(0, 1, 0.1):
        for j in np.arange(0, 1, 0.1):
            net = p_net(step, (i, j), w, b)[0][0]
            actual = abs(i) + abs(j) < 1
            print(net == actual)

# output = p_net(A, w, b, x)

# def p_net(A, x, w_list, b_list):
#     A = np.vectorize(A)
#     a = [np.array([])] * len(w_list)
#     a[0] = x

#     for layer in range(1, len(w_list)):
#         a[layer] = A(np.add(np.matmul(a[layer - 1], w_list[layer]), b_list[layer]))

#     return a[len(w_list) - 1]


def test_diamond(w_list, b_list):
    for i in np.arange(0, 1, 0.1):
        for j in np.arange(0, 1, 0.1):
            net = p_net(step, (i, j), w_list, b_list)[0][0]
            actual = abs(i) + abs(j) < 1
            print(net == actual)


def test_circle(w_list, b_list):
    num_correct = 0
    c = 0

    while c < 500:
        i, j = random.uniform(0, 1), random.uniform(0, 1)
        net = p_net(step, (i, j), w_list, b_list)[0][0].round()
        actual = (i + j) ** .5 < 1

        if net == actual:
            num_correct += 1
        else:
            print(i, ",", j)

        c += 1

    print(f"Accuracy: {num_correct / 5}%")


test_diamond()

# print("XOR HAPPENS HERE")
# inputs = ast.literal_eval(sys.argv[1])
# print(f"Output: {re_XOR(inputs)}")







# in1, in2 = ast.literal_eval(sys.argv[1])
# print(w:= p_net(in1, in2))