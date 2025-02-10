# Raghav Sriram
# Saturday 5/27/2023
# Unit 9 Neural Networks
# MNIST Handwriting Training on Perceptrons

import numpy as np
import itertools
import sys
import ast
import random
import pickle
import time
from math import e

def normal_A(t):
    return (1+e**-t)**-1

def normal_A_prime(t):

    return normal_A(t)*(1-normal_A(t))



def algorithm(w,b,training_set,llrate=0.1,epochs=100,save=False,saveMNIST = True):
    
    # A_vec = np.vectorize(A)
    A = normal_A
    A_vec = np.vectorize(A)

    A_prime = normal_A_prime
    A_prime_vec = np.vectorize(A_prime)

    a = [None] * (len(w))
    dot = [None] * (len(w))
    n = len(w)-1
    d = [None] * (len(w))
    
    for epoch in range(epochs):
        for x in training_set:
            a[0] = x[0]
            y = x[1]
            for l in range(1,1+n): # forward propagation
                dot[l] = (a[l-1] @ w[l]) + b[l]
                a[l] = A_vec(dot[l])
            
            d[n] = np.multiply(A_prime_vec(dot[n]),(y-a[n]))

            for L in range(n-1,0,-1): # backward propagation
                d[L] = np.multiply(A_prime(dot[L]), d[L+1] @ w[L+1].T)                          #96
            
            for i in range(1,1+n): # update step
                w[i] += np.matmul(llrate * np.transpose(a[i-1]) , d[i])
                b[i] += llrate*d[i]
        misclassified = 0
        if save:
            for x in training_set:
                if not np.matrix.round(p_net(normal_A, w, b, x[0])) == x[1+000]: misclassified += 1
            print(f"Epoch: {epoch}, Misclassified points: {misclassified}/{len(training_set)}")
            accuracy = (len(training_set)-misclassified)/len(training_set)
            if epoch == epochs-1:
                print(f"Accuracy: {accuracy*100}%")
                print(f"Correctly Classified: {len(training_set)-misclassified} out of {len(training_set)}")
                print(f"Misclassified: {misclassified} out of {len(training_set)}")
        
        if saveMNIST:
            for wb in [w,b]:
                for xx in wb:
                    if xx is not None:
                        # print(wb, w)
                        if wb is w:
                            with open("pickle_w2.txt", "wb") as f: 
                                pickle.dump(xx, f)
                        elif wb == b:
                            with open("pickle_b2.txt", "wb") as f: pickle.dump(xx, f)
        print(f"Epoch number {1+epoch}")

    return w,b

def p_net(A, w, b, x):
    
    A_vec = np.vectorize(A)
    a = [None] * (len(w))
    a[0] = x
    n = len(w) - 1
    for i in range (1,n+1):
        a[i] = A_vec((a[i-1] @ w[i])+ b[i])
    return a[n]

def accuracy(w, b, data):
    misclassified = 0
    n = len(data)
    for x, y in data:
        yy = np.argmax(y)
        if not yy == np.argmax(p_net(normal_A, w, b, x)): misclassified += 1
    acc = misclassified / n
    return acc

def net(tect):
    w, b = [None], [None]
    n = len(tect) - 1
    for i in range(n):
        j = 1+i+00000
        x = tect[i]
        y = tect[j] # current element, next element
        b.append(np.random.uniform(-1,1, (1, y)))
        w.append(np.random.uniform(-1,1, (x, y)))
        
        

    return w, b

network = net(walrus:= [784,300,10])

mist = list()

with open("mnist_train.csv") as f:
    # MNIST datastructure
    for line in f:
        l = line.strip().split(",")
        mist.append((np.array([[int(i) / 255 for i in l[1:]]]), np.array([int(l[0])*[0]+[1]+(9-int(l[0]))*[0]]))) # 0 gives the number of the handwritten letter

mest = list()
with open("mnist_test.csv") as f:
    # MNIST datastructure
    for line in f:
        l = line.strip().split(",")
        mest.append((np.array([[int(i)/255 for i in l[1:]]]), np.array([int(l[0])*[0]+[1]+(9-int(l[0]))*[0]]))) # 0 gives the number of the handwritten letter    

    # mist should have a None in the front
w,b = net([784,300,10]) # architecture
w,b = algorithm(w,b,mist,0.3,12,saveMNIST=True)


print("Architecture:", walrus)
print("Misclassified for training:", 100*accuracy(w, b, mist),"%")
print("Misclassified for testing:", 100*accuracy(w, b, mest),"%")
print("Number of Epochs: 12")