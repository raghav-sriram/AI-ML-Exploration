# Raghav Sriram
# Monday 5/15/2023
# Unit 9 Neural Networks
# Perceptrons 4

import numpy as np
import itertools
import sys
import ast
from math import e

def truth_table(bits, n):
    binary = str(bin(n))[2:]
    right_side = "0"*(bits-len(binary)) + binary
    right_side = list(right_side)

    truth = list(itertools.product([1,0],repeat=bits))
    return tuple(zip(truth,right_side))

def step(t):
    return np.heaviside(t,0) # int(0<t)

def normal_A(t):
    return (1+e**-t)**-1

def perceptron(A, w3, w4, in1, in2, b):
    return A(b+w3 * in1 + w4 * in2)

def p_net(A, w, b, x):
    a=[x]
    length_ = len(w)-1
    for i in range(1,length_+1,1): a.append(A(np.add(np.matmul(w[i],a[i-1]),b[i])))
    return a[length_]

def re_XOR(i): 
    b = [None, np.array([[0],[3]]),np.array([[-2]])]
    w = [None, np.array([[1,1],[-1,-2]]),np.array([[1,2]])]
    print(int(p_net(step,w, b, np.array([[int(i[0])],[int(i[1])]])))) # XOR HAPPENS HERE

def diamond(i):
    bondage = 1
    bia = -3.5
    b = [None, np.array([[bondage],[bondage],[bondage],[bondage]]), np.array([[bia]])]
    w = [None, np.array([[-bondage,-bondage],[-bondage,bondage],[bondage,-bondage],[bondage,bondage]]), np.array([[1,1,1,1]])]
    if not 1 == int(p_net(step, w, b, np.array([[i[0]],[i[1]]]))): # inside or outside
        print("outside")
    else: 
        print("inside")

def circle(i):
    bondage = 1
    number_of_points = 500
    b = [None, np.array( [ [i[0]] , [i[0]] , [i[0]] , [i[0]]] ), np.array([ [i[1]]] )]
    references = 2*np.random.rand(500, 2) - 1
    w = [None, np.array( [ [-bondage,-bondage] , [-bondage,bondage] , [bondage,-bondage] , [bondage,bondage]] ), np.array([ [1,1,1,1]] )]    
    not_missclassified = 0
    for x in references:
        if not int(p_net(normal_A, w, b, np.array([x]).transpose())<0.5) == int(np.linalg.norm(x)<1): print(x) # print the misclassified
        else: not_missclassified = 1+not_missclassified
    print(f"Final Accuracy (%): {not_missclassified/number_of_points*100}")                     #96

command_line_arguments = sys.argv[1:]
# print(len(sys.argv))
# print(len(command_line_arguments))

if len(command_line_arguments)==1: re_XOR(ast.literal_eval(sys.argv[1])) # challenge 1

if len(command_line_arguments)==2: diamond((float(sys.argv[1]),float(sys.argv[2]))) # challenge 2

if len(command_line_arguments)==0: circle((-0.9035 , -1.3)) # challenge 3





























