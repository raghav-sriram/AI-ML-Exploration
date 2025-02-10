import itertools
import numpy as np
import matplotlib.pyplot as plt

def step(t):
    return int(0<t)

def perceptron(A, w, b, x):
    dp = sum([w[i]*x[i] for i in range(len(x))])
    return A(dp+b)

def truth_table(bits, n):
    binary = str(bin(n))[2:]
    right_side = "0" * ((2 ** bits) - len(binary)) + binary
    right_side = list(map(int, right_side))

    truth = list(itertools.product([1, 0], repeat=bits))
    return tuple(zip(truth, right_side))

def train(bits, tt, llrate):
    
    w = [0]*bits #weights
    b = 0 #bias

    for epochs in range(100):
        total_error = 0
        for x in tt:
            output = perceptron(step,w, b, x[0])
            error = x[1] - output
            total_error += abs(x[1] - output)

            for i in range(len(w)): w[i] += error * llrate * x[0][i]
            b += error * llrate

        if total_error == 0: break
    return w,b

def accuracy(tt, w, b):
    accurate = 0
    for x in tt:
        if perceptron(step, w, b, x[0]) == x[1]: accurate += 1
    return accurate / len(tt)

def graph_perceptrons(bits):
    llrate, distinct = 1, 2** (2**bits)
    ax1, axs = plt.subplots(4,4)

    ax1.suptitle("Graph Perceptrons")


    for canon in range(distinct):
        tt = truth_table(bits, canon)
        w,b = train(bits, tt, llrate)

        x, y = np.arange(-2,2,0.1), np.arange(-2,2,0.1)


        mesh1,mesh2 = np.meshgrid(x, y)

        applied = np.zeros_like(mesh1) #same size array with zeros
        for i in range(len(mesh1)):
            for j in range(len(mesh1[i])):
                applied[i,j] = perceptron(step, w, b, [mesh1[i,j], mesh2[i,j]])


        canon2 = canon // 4
        canon1 = canon % 4

        ax = axs[canon2, canon1]

        sizeof_marker = 5
        ax.contourf(mesh1,mesh2 , applied, cmap="RdYlGn")
        red,green = "ro","go"
        for i, j in tt:
            triue = j == 1
            if not triue:
                ax.plot(*i, red, markersize = sizeof_marker)
            else:
                ax.plot(*i, green, markersize=sizeof_marker)

    plt.tight_layout() #spacing
    plt.show()


graph_perceptrons(2)














