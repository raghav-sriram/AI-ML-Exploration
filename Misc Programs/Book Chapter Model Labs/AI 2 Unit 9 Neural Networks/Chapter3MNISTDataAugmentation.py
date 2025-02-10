# Raghav Sriram
# Period 6 ML Gabor
# Chapter 3 MNIST Data Augmentation

import numpy as np
import itertools
import sys
import ast
import random
import pickle
import time
from math import e
import matplotlib.pyplot as plt
from scipy.ndimage import shift, rotate

def normal_A(t):
    return (1+e**-t)**-1

def normal_A_prime(t):

    return normal_A(t)*(1-normal_A(t))



def algorithm(w,b,training_set,llrate=0.1,epochs=100,save=False,saveMNIST = True,distort = False):
    
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
            if distort:
                x = which_jitter(x)
            a[0] = x[0]
            y = x[1]
            for l in range(1,1+n):
                dot[l] = (a[l-1] @ w[l]) + b[l]
                a[l] = A_vec(dot[l])
            
            d[n] = np.multiply(A_prime_vec(dot[n]),(y-a[n]))

            for L in range(n-1,0,-1):
                d[L] = np.multiply(A_prime(dot[L]), d[L+1] @ w[L+1].T)                          #96
            
            for i in range(1,1+n):
                w[i] += np.matmul(llrate * np.transpose(a[i-1]) , d[i])
                b[i] += llrate*d[i]
        misclassified = 0        
        print(f"Epoch number {epoch+1}")

    return w,b

def p_net(A, w, b, x):
    
    A_vec = np.vectorize(A)
    a = [None] * (len(w))
    a[0] = x
    n = len(w) - 1
    for i in range (1,n+1):
        a[i] = A_vec((a[i-1] @ w[i])+ b[i])
    return a[n]

def display(classification,image):
    re_img = image.reshape(28,28)

    # Display each transformation
    plt.figure()
    plt.title(f"Correct Classification: {classification}")
    plt.imshow(re_img,cmap="gray")
    plt.show()
    plt.pause(1)  # Adjust the duration in seconds
    plt.close()

# def accuracy(w, b, data):
#     misclassified = 0
#     n = len(data)
#     for x, y in data:
#         yy = np.argmax(y)
#         if not yy == np.argmax(p_net(normal_A, w, b, x)): 
#             misclassified += 1
#             print(f"Correct Classification is {np.argmax(y)}")
#             display(classification=np.argmax(y),image=x)
#     acc = misclassified / n
#     return acc

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


def which_jitter(img):
    ops = ["normal", "up", "left", "down", "right", "rotate_right", "rotate_left"]
    opps = np.random.choice(ops)
    re_img = img[0].reshape(28,28)

    matrix_transformations = {
        "up": np.roll(re_img, -1, axis=0),
        "left": np.roll(re_img, -1, axis=1),
        "down": np.roll(re_img, 1, axis=0),
        "right": np.roll(re_img, 1, axis=1),
        "rotate_right": crop_size(rotate(re_img, -15)),
        "rotate_left": crop_size(rotate(re_img, 15)),
        "normal": re_img
    }

    # plt.figure()
    # plt.title("normal")
    # plt.imshow(re_img,cmap="gray")

    re_img = matrix_transformations[opps]

    # Display each transformation
    # plt.figure()
    # plt.title(opps)
    # plt.imshow(matrix_transformations[opps], cmap="gray")
    
    # plt.figure()
    # plt.title(f"{opps}")
    # plt.imshow(re_img,cmap="gray")

    # plt.show()

    return (re_img.reshape(1,784), img[1])

def crop_size(img):
    y,x = img.shape
    cropx = x//2-(28//2)
    cropy = y//2-(28//2)    
    return img[cropy:cropy+28,cropx:cropx+28]

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
w,b = algorithm(w,b,mist,0.3,12,saveMNIST=True,distort = True)


print("Architecture:", walrus)
print("Misclassified for training:", 100*accuracy(w, b, mist),"%")
print("Misclassified for testing:", 100*accuracy(w, b, mest),"%")
print("Number of Epochs: 12")