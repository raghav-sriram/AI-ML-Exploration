# Raghav Sriram
# Period 6 ML Gabor
# Chapter 15

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

def algorithm(w,b,training_set,llrate=0.1,epochs=100,save=False):
    
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

    return w,b

def p_net(A, w, b, x):
    
    A_vec = np.vectorize(A)
    a = [None] * (len(w))
    a[0] = x
    n = len(w) - 1
    for i in range (1,n+1):
        a[i] = A_vec((a[i-1] @ w[i])+ b[i])
    return a[n]

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

def random_generate(n):
    app = list()

    for kfahusej in range(n): 
        i, j = np.random.uniform(-1, 1), np.random.uniform(-1, 1)        
        y = np.array([[int((i**2+j **2)**0.5<1)]]) # dist formula
        x = np.array([[i, j]])
        app.append((x, y))
    return app

w,b = net([2,4,1])
w,b = algorithm(w,b,random_generate(10000),0.1,200,True)







