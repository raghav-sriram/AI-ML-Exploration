# Raghav Sriram
# Wednesday 5/3/2023
# Unit 9 Neural Networks
# Perceptrons 1


import itertools
import sys
import ast

def truth_table(bits, n):
    binary = str(bin(n))[2:]
    right_side = "0"*(bits-len(binary)) + binary
    right_side = list(right_side)

    truth = list(itertools.product([1,0],repeat=bits))
    return tuple(zip(truth,right_side))

def pretty_print_tt(table):
    print("Inputs", "Output")
    for x in table:
        prin = "".join(str(y) + " " for y in x[0])
        print(prin + "|", x[1])

def step(t):
    return int(0<t)

def perceptron(A, w, b, x):
    dp = sum([w[i]*x[i] for i in range(len(x))])
    return str(A(dp+b))

def check(n, w, b):
    truth = truth_table(len(w),n)
    count = 0
    denominator = 0
    # pretty_print_tt(truth)
    for tup in truth:
        # print(tup[0],tup[1])
        percep = perceptron(step, w, b, tup[0])
        if percep == tup[1]: count += 1
        denominator += 1
    return count/denominator

n = int(sys.argv[1])
w = ast.literal_eval(sys.argv[2])
b = float(sys.argv[3])

print(check(n, w, b))
