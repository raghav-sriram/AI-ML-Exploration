# Raghav Sriram
# Monday 5/15/2023
# Unit 9 Neural Networks
# Gradient Descent

import sys
import numpy as np

def gradient_b(x,y):
    return np.array((2 * ( x - y ** 2), 2 * ( -2 * x * y + 2 * y ** 3 + y - 1)))


def gradient_A(x,y):
    return np.array((8 * x - 3 * y + 24, -3 * x + 4 * y - 20))

def gd(AB, l):
    if AB == "A": gradient = gradient_A
    else: gradient = gradient_b
    

    x, y = (0, 0)
    
    pd = gradient(x, y)
    partialx = pd[0]
    partialy = pd[1]
    stop_value = 10e-8
    while stop_value < np.sqrt(pd@pd):
        pd = gradient(x, y)
        partialx = pd[0]
        partialy = pd[1]
        x -= l * partialx
        y -= l * partialy
        pd = gradient(x, y)        
        print(f"({x},", f"{y}),", f"{pd}")















gd(sys.argv[1],0.10)