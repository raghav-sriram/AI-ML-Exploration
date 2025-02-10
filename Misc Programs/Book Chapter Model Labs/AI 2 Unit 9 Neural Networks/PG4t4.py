import sys
import numpy as np
import random
from math import exp

def step_function(x):
    return 1 if x >= 0 else 0

def sigmoid_function(x):
    return 1 / (1 + exp(-x))

def p_net(A, x, weights, biases):
    for W, b in zip(weights, biases):
        x = [A(xi) for xi in np.dot(W, x) + b]
    return x

def xor(inputs):
    weights = [np.array([[20, 20], [20, 20]]), np.array([[20, -20]])]
    biases = [np.array([[-10], [-30]]), np.array([[10]])]
    return p_net(step_function, inputs, weights, biases)[0]

def diamond(inputs):
    weights = [np.array([[-1, -1], [-1, 1], [1, -1], [1, 1]]), np.array([[1, 1, 1, 1]])]
    biases = [np.array([[0.5], [0.5], [0.5], [0.5]]), np.array([[-1.5]])]
    return p_net(step_function, inputs, weights, biases)[0]

def circle(inputs, i, j):
    weights = [np.array([[-1, -1], [-1, 1], [1, -1], [1, 1]]), np.array([[1, 1, 1, 1]])]
    biases = [np.array([[i], [i], [i], [i]]), np.array([[j]])]
    return p_net(sigmoid_function, inputs, weights, biases)[0]

if __name__ == "__main__":
    if len(sys.argv) == 1:
        total = 500
        correct = 0
        i = -0.15  # Best bias for hidden layer found through trial and error
        j = -0.2   # Best bias for output layer found through trial and error
        for _ in range(total):
            x, y = random.uniform(-1, 1), random.uniform(-1, 1)
            output = round(circle([x, y], i, j))
            if (output == 0 and x**2 + y**2 >= 1) or (output == 1 and x**2 + y**2 < 1):
                correct += 1
            else:
                print(f"Misclassified point: ({x}, {y})")
        print(f"Accuracy: {correct / total * 100}%")
    elif len(sys.argv) == 2:
        print("XOR HAPPENS HERE")
        inputs = [int(x) for x in sys.argv[1].strip("()").split(",")]
        print(f"Output: {xor(inputs)}")
    elif len(sys.argv) == 3:
        inputs = [float(x) for x in sys.argv[1:]]
        print("Inside" if diamond(inputs) else "Outside")
