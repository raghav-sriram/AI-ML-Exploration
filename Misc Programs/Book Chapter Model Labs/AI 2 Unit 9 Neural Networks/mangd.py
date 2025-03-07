import sys  
import numpy as np


def gradA(x, y):
    """
    Gradient of function A
    """
    return np.array((8*x - 3*y + 24, -3*x + 4*y - 20))

def gradB(x, y):
    """
    Gradient of function B
    """
    return np.array((2*(x - y**2), 2*(-2*x*y + 2*y**3 + y - 1)))
    


def gradient_descent(learning_rate, func_string, start=(0, 0)):
    """
    Gradient descent algorithm
    - Learning rate: lambda 
    """
    if func_string == "A":
        grad = gradA

    else:
        grad = gradB

    # start at (0, 0)
    x, y = start
    curr_grad = grad(x, y) # gradient at (0, 0)
    while np.sqrt(curr_grad.dot(curr_grad)) > 10e-8: # stop when gradient is below threshold
        x = x - learning_rate * (curr_grad:=grad(x, y))[0] # update x and assign gradient to curr_grad
        y = y - learning_rate * curr_grad[1] # update y, curr_grad is stored from previous line
        print(f"({x}, {y}), {curr_grad}") # print current x, y and gradient


if __name__ == "__main__":
    gradient_descent(0.05, sys.argv[1])    