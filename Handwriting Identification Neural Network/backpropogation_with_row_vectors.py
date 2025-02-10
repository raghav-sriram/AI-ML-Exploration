# Raghav Sriram
# Saturday 5/13/2023
# Unit 9 Neural Networks
# Back Propogation

import sys
import numpy as np
from math import e
import pickle

def step(t):
    return int(0<t)

def perceptron(A, w3, w4, in1, in2, b):
    return A(b+w3 * in1 + w4 * in2)

def normal_A(t):
    return (1+e**-t)**-1

def normal_A_prime(t):

    return normal_A(t)*(1-normal_A(t))

def net(tect):
    w, b = [None], [None]

    for i in range(len(tect) - 1):
        x = tect[i]
        y = tect[i + 1] # current element, next element
        w.append(np.random.uniform(-1,1, (x, y))) #appended to the weight matrix
        b.append(np.random.uniform(-1,1, (1, y))) #appended to the bias matrix

    return w, b

def algorithm(w,b,training_set,llrate=0.1,epochs=100,save=False):
    
    # A_vec = np.vectorize(A)
    A = normal_A
    A_vec = np.vectorize(A)

    A_prime = normal_A_prime
    A_prime_vec = np.vectorize(A_prime)

    a = [np.array([])] * (len(w))
    dot = [np.array([])] * (len(w))
    n = len(w)-1
    d = [np.array([])] * (len(w))
    
    for epoch in range(epochs):
        for x in training_set:
            a[0] = x[0]
            y = x[1]
            for l in range(1,1+n): # forward propagation
                # dot[l] = w[l] @ a[l-1] + b[l]
                # print("w",w[l])
                # print("a",a[l-1])
                # print("b",b[l])
                dot[l] = np.dot(a[l-1],w[l]) + b[l]
                # a[l] = A(dot[l])
                a[l] = A_vec(dot[l])
            
            d[n] = np.multiply(A_prime_vec(dot[n]),(y-a[n]))

            for L in range(n-1,0,-1): # backward propagation
                # d[L] = np.multiply(A_prime_vec(dot[L]), np.transpose(w[L+1]) @ d[L+1])
                d[L] = np.multiply(A_prime_vec(dot[L]), np.matmul(d[L+1],np.transpose(w[L+1]))) #96
            
            for i in range(1,1+n): # update step
                b[i] = b[i] + llrate*d[i]
                # w[i] = w[i] + llrate * np.transpose(a[i-1]) @ d[i]
                w[i] = w[i] + np.matmul(llrate * np.transpose(a[i-1]) , d[i])
            # forward_prop_error(w, b, x[0], x[1])
    # error = 0.5*((y[0]-a[2][0])**2 + (y[1]-a[2][1])**2)
    # print("dr blythe", error)
        misclassified = 0
        if save:
            for x in training_set:
                # print("x[0]",x[0])
                # print("x[1]",x[1])
                point = np.matrix.round(p_net(normal_A, w, b, x[0]))
                if x[1] != point: misclassified += 1
            print(f"Epoch: {epoch}, Misclassified points: {misclassified}/{len(training_set)}")
            accuracy = (len(training_set)-misclassified)/len(training_set)
            if epoch == epochs-1:
                print(f"Accuracy: {accuracy*100}%")
                print(f"Correctly Classified: {len(training_set)-misclassified} out of {len(training_set)}")
                print(f"Misclassified: {misclassified} out of {len(training_set)}")

        for wb in [w,b]:
            for xx in wb:
                if xx is not None:
                    # print(wb, w)
                    if wb is w:
                        with open("picklerz.txt", "wb") as f: 
                            pickle.dump(xx, f)
                    elif wb == b:
                        with open("picklerzs.txt", "wb") as f: pickle.dump(xx, f)
    return w,b

def errand(w, b, x, y):
    a = p_net(normal_A, w, b,x)
    # [[0.01613435 0.53100825]]
    a_right = np.array([[a[0][0]],[a[0][1]]])
    print(x,y,a_right)
    # print(a)

    calculated = (y - np.matrix.round(a))[0]

    return np.dot(calculated, calculated) / 2

def p_net(A, w, b, x):
    
    A_vec = np.vectorize(A)
    a = [None] * (len(w))
    a[0] = x
    n = len(w) - 1
    for i in range (1,n+1):
        a[i] = A_vec(np.dot(a[i-1],w[i]) + b[i])
    return a[n]

def random_generate(n):
    ts = []

    for kuagsh in range(n):
        i, j = np.random.uniform(-1, 1), np.random.uniform(-1, 1)
        x = np.array([[i, j]])
        y = np.array([[int((i**2+j **2)**0.5<1)]]) # dist formula
        ts.append((x, y))
    return ts


# w = [None, np.array([[1, -0.5], [1, 0.5]]), np.array([[1, 2],[-1,-2]])]
# # b = [None, np.array([[1,-1]]), np.array([[-0.5,0.5]])]
# b = [None, np.array([[1,-1]]), np.array([[-0.5,0.5]])]

# x = [None, np.array([[2],[3]])]
# y = [None, np.array([[0.8],[1]])]

# training_set = [([[2] , [3]], 
#                  [[.8] ,[1]])]

# for x in (training_set):
    # print(x)
    # print(x[0])
    # print(x[0][0])


# up_w, up_b = algorithm(w,b,training_set,0.1,1)
# errand(up_w,up_b,training_set[0][0],training_set[0][1])
# print(up_w)
# print(up_b)






if (sys.argv[1] == "S"):
    w,b = net([2,2,2])
    # print("network",w)
    # print("network",b)

    for i in range(5):
        with open("picklerz.txt", "rb") as f:
            picked = pickle.load(f)
        print("yoyoyo",picked)

    for i in range(5):
        with open("picklerzs.txt", "rb") as f:
            picked = pickle.load(f)
        print("yoyoyo",picked)

    sum = [
            (np.array([[0,0]]), np.array([[0,0]])),
            (np.array([[0,1]]), np.array([[0,1]])),
            (np.array([[1,0]]), np.array([[0,1]])),
            (np.array([[1,1]]), np.array([[1,0]]))
            # (np.array([[0], [0]]), np.array([[0], [0]])),
        # (np.array([[0], [1]]), np.array([[0], [1]])),
        # (np.array([[1], [0]]), np.array([[0], [1]])),
        # (np.array([[1], [1]]), np.array([[1], [0]]))
        ]



    w,b = algorithm(w,b,sum,0.9,2500)
    # print(w)
    # print(b)

    for x in sum:
            errand(w, b, x[0], x[1])

if (sys.argv[1] == "C"):
    w,b = net([2,4,1])
    w,b = algorithm(w,b,random_generate(10000),0.1,200,True)

# i = np.array([[i[0]],[i[1]]])

# print(training_set[0][0])
# ouput = p_net(step,w,b,training_set[0][0])
# print(ouput)
# error = 0.5*((training_set[0][0][0][0]-ouput[0][0])**2 + (training_set[0][0][1][0]-ouput[1][0])**2)
# print(error)
# # calc error here
# output = p_net(step,up_w, up_b,training_set[0][0])
# print(output)
# error = 0.5*((training_set[0][0][0][0]-ouput[0][0])**2 + (training_set[0][0][1][0]-ouput[1][0])**2)
# print(error)
# # calc error here






