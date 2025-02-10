import itertools
import sys

def step(t):
    return int(0 < t)

def perceptron(w, b, x):
    dp = sum([w[i] * x[i] for i in range(len(x))])
    return step(dp + b)

def truth_table(bits, n):
    binary = str(bin(n))[2:]
    right_side = "0" * ((2 ** bits) - len(binary)) + binary
    right_side = list(map(int, right_side))

    truth = list(itertools.product([1, 0], repeat=bits))
    return tuple(zip(truth, right_side))

def train(bits, tt, llrate, max_epochs):
    w = [0] * bits
    b = 0

    prev_outcome = None
    for epoch in range(max_epochs):
        outcome = []
        for x in tt:
            target = x[1]
            output = perceptron(w, b, x[0])
            error = target - output

            for i in range(len(w)):
                w[i] += error * llrate * x[0][i]
            b += error * llrate
            
            outcome.append((w.copy(), b))
        
        if outcome == prev_outcome:
            break
        prev_outcome = outcome.copy()

    return w, b

def accuracy(tt, w, b):
    accurate = 0
    for x in tt:
        output = perceptron(w, b, x[0])
        if output == x[1]:
            accurate += 1
    return accurate / len(tt)

bits = int(sys.argv[1])
canon = int(sys.argv[2])

tt = truth_table(bits, canon)
llrate = 1
max_epochs = 100

w, b = train(bits, tt, llrate, max_epochs)
accr = accuracy(tt, w, b)

print(f"Final weight vector: {w}")
print(f"Final bias value: {b}")
print(f"Accuracy: {accr * 100:.2f}%")
