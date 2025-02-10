import sys
import numpy as np
import math
import ast

np.set_printoptions(threshold=np.inf)
np.set_printoptions(linewidth=np.inf)

def iprint(iterable):
    for idx, item in enumerate(iterable):
        print(idx, "\t", item)


def dprint(dictionary):
    for key, value in dictionary.items():
        print(key, "\t", value)


def step(x):
    return 1 if x > 0 else 0

def sigmoid(x):
    # works with numpy arrays
    return 1 / (1 + np.e ** (-x))

def sigmoid_prime(x):
    return sigmoid(x) * (1 - sigmoid(x))


def p_net(A_vec, weights, biases, input):
    outputs = [input.reshape(-1, 1)]  # turn into column vector
    # outputs = [input]
    n = len(weights)
    for i in range(1, n):  # @ is dot product
        output = A_vec(
            weights[i] @ outputs[i - 1] + biases[i]
        )  # previous layer's output is outputs[i-1]
        outputs.append(output)

        # debug
        # print(f'[DEBUG] {input} weights[{i}] =\n {weights[i]}')
        # print(f'[DEBUG] {input} outputs[{i-1}] =\n {outputs[i-1]}')
        # print(f'[DEBUG] {input} biases[{i}] =\n {biases[i]}')

    return outputs[-1]

def lr_scaler(lr, epoch, epochs):
    if epoch < epochs / 2:
        return lr
    return lr * (1 - epoch / epochs)


def train_network(A_vec, A_prime_vec, inputs, outputs, w, b, epochs, lr, lr_scaler=None, test_accuracy=False):
    # (x,y) --> input, output
    # w     --> weights
    # b     --> biases
    # lr    --> learning rate
    n = len(w)
    dataset = list(zip(inputs, outputs))
    dataset_size = len(dataset)

    # # print(f"[DEBUG] w[L] shape: {w[1].shape}, w, b len: {len(w)}, {len(b)}")
    # print(f"[DEBUG] epochs: {epochs}, lr: {lr}")

    for epoch in range(epochs):
        # print(f"[DEBUG] Starting Epoch {epoch}:")
        if lr_scaler:
            lr_scaled = lr_scaler(lr, epoch, epochs)
        else:
            lr_scaled = lr
        for x, y in dataset:
            a = [x.reshape(-1, 1)]; # print(f"[DEBUG] a[0]: {a[0]}, a[0] shape: {a[0].shape}")
            dotN = {}
            for layer in range(1, n):
                dotL = w[layer] @ a[layer - 1] + b[layer]
                # print(f"[DEBUG] dotL shape: {dotL.shape}, w[layer] shape: {w[layer].shape}, a[layer-1] shape: {a[layer-1].shape}, b[layer] shape: {b[layer].shape}")
                a.append(A_vec(dotL))
                dotN[layer] = dotL

            # dprint(dotN)
            y = y.reshape(-1, 1); # print(f"[DEBUG] y shape: {y.shape}")
            deltaN = A_prime_vec(dotN[n - 1]) * (y - a[n - 1]); # print(f"[DEBUG] deltaN shape: {deltaN.shape}, A_prime_vec shape: {A_prime_vec(dotN[n-1]).shape}, y shape: {y.shape}, a[n-1] shape: {a[n-1].shape}, y-a[n-1] shape: {(y-a[n-1]).shape}")
            delta = {n-1: deltaN}
            for back_layer in range(n - 2, 0, -1):  # update deltas going backwards
                # # print(f"[DEBUG] back_layer: {back_layer}, prev delta: {delta[back_layer+1]}")
                # # print(f"[DEBUG] w[back_layer+1] shape: {w[back_layer+1].shape}")
                c1 = A_prime_vec(dotN[back_layer])
                c2 = delta[back_layer + 1]
                c3 = w[back_layer + 1].transpose()
                # print(f"[DEBUG] c1 shape: {c1.shape}, c2 shape: {c2.shape}, c3 shape: {c3.shape}")
                delta[back_layer] = c1 * (c3 @ c2)
                
            
            for layer1 in range(1, n):  # update weights & biases
                b[layer1] = b[layer1] + lr_scaled * delta[layer1]; # print(f"[DEBUG] b[{layer1}] shape: {b[layer1].shape}, delta[{layer1}] shape: {delta[layer1].shape}")
                w[layer1] = w[layer1] + lr_scaled * delta[layer1] * a[layer1 - 1].transpose()
        if not test_accuracy:
            print(f"[DEBUG] Epoch {epoch}: a[last]: {a[-1].tolist()}", end="\r")
        else:
            print(f"[DEBUG] Epoch {epoch}: {dataset_size - accuracy(w, b, inputs, outputs, sigmoid, False) * dataset_size}", end="\r")
        # print(f"[DEBUG] End Epoch {epoch}")
    return w, b  # return new weights and biases    


def main_1(input):
    A_vec = np.vectorize(step)
    weights = [None]
    biases = [None]

    # everything has to be 2d arrays
    weights.append(
        np.array(
            [
                [
                    -1,
                    1,
                ],
                [
                    1,
                    -1,
                ],
            ]
        )
    )
    # print(weights[-1].shape) # 1st layer
    weights.append(
        np.array(
            [
                [
                    1,
                    1,
                ]
            ]
        )
    )
    # print(weights[-1].shape) # 2nd layer

    biases.append(
        np.array(
            [
                [
                    0,
                ],
                [
                    0,
                ],
            ]
        )
    )
    # print(biases[-1].shape) # 1st layer
    biases.append(
        np.array(
            [
                [0],
            ]
        )
    )
    # print(biases[-1].shape)    # 2nd layer

    inputs = (
        np.array([0, 0]),
        np.array([0, 1]),
        np.array([1, 0]),
        np.array([1, 1]),
    )
    inputs = tuple(reversed(inputs))

    # XOR HAPPENS HERE
    output = p_net(A_vec, weights, biases, input)
    print(input, output[0, 0])


def main_2(point):
    A_vec = np.vectorize(step)
    weights = [None]
    biases = [None]

    # 2-4-1 network
    weights.append(np.array([[1, 1], [-1, -1], [1, -1], [-1, 1]]))
    weights.append(np.array([[1, 1, 1, 1]]))

    biases.append(np.array([[1, 1, 1, 1]]))
    biases.append(np.array([[-3]]))

    output = p_net(A_vec, weights, biases, point)[0, 0]
    if output > 0.5:
        print("inside")
    else:
        print("outside")

    # accuracy = 0
    # for i in range(250):
    #     input = np.random.random((2,)) * 2 - 1
    #     if abs(input[0]) + abs(input[1]) < 1:
    #         output = p_net(A_vec, weights, biases, input)
    #         # print("inside", output, output[0,0] == 1)
    #         if output[0,0] == 1:
    #             accuracy += 1
    #     else:
    #         output = p_net(A_vec, weights, biases, input)
    #         # print("outside", output, output[0,0] == 0)
    #         if output[0,0] == 0:
    #             accuracy += 1
    # print(accuracy / 250)


def test_network(A_vec, weights, biases, N, print_misses=False):
    accuracy = 0
    for i in range(N):
        input = np.random.random((2,)) * 2 - 1
        condition = math.sqrt(input[0] ** 2 + input[1] ** 2) < 1
        if condition:
            output = p_net(A_vec, weights, biases, input)
            # print("inside", output[0,0], output[0,0] == 1)
            if output[0, 0] > 0.5:
                accuracy += 1
            else:
                if print_misses:
                    print(input, output[0, 0])
        else:
            output = p_net(A_vec, weights, biases, input)
            # print("outside", output[0,0], output[0,0] == 0)
            if output[0, 0] <= 0.5:
                accuracy += 1
            else:
                if print_misses:
                    print(input, output[0, 0])
    return accuracy / N


def main_3():
    # results = {}

    # for i in np.linspace(0.75, 2.5, 51):
    #     for j in np.linspace(-2.5, -3.2, 41):
    #         weights = [None]
    #         biases = [None]

    #         weights.append(np.array([[1, 1], [-1, -1], [1, -1], [-1, 1]]))
    #         weights.append(np.array([[1, 1, 1, 1]]))

    #         biases.append(np.array([[i, i, i, i]]))
    #         biases.append(np.array([[j]]))

    #         accuracy = test_network(sigmoid, weights, biases, 1000)
    #         print(f'({i}, {j})', accuracy)
    #         results[(i, j)] = accuracy

    # # print top 5
    # print()
    # print(sorted(results.items(), key=lambda x: x[1], reverse=True)[:5])

    i, j = 1.59, -3.1475  # 98.3% accuracy

    weights = [None]
    biases = [None]

    weights.append(np.array([[1, 1], [-1, -1], [1, -1], [-1, 1]]))
    weights.append(np.array([[1, 1, 1, 1]]))

    biases.append(np.array([[i, i, i, i]]))
    biases.append(np.array([[j]]))

    # print(weights[1].shape, biases[1].shape)

    accuracy = test_network(sigmoid, weights, biases, 500, True)
    print(f"Network i={i}, j={j} accuracy: {accuracy}")


def runner_main():
    args = sys.argv[1:]
    if len(args) == 0:
        main_3()
    elif len(args) == 1:
        main_1(np.array(ast.literal_eval(args[0])))
    elif len(args) == 2:
        x, y = float(args[0]), float(args[1])
        main_2(np.array([x, y]))
    else:
        import antigravity

def accuracy(weights, biases, input, output, A_vec, sum=False):
    num_correct = 0

    assert len(input) == len(output)
    num_samples = len(input)

    for x, y in zip(input, output):
        out = p_net(A_vec, weights, biases, x)
        if sum:
            if round(out[0, 0]) == y[0] and round(out[1, 0]) == y[1]:
                num_correct += 1
            print(x, y, "yo", out)
        else: # circle
            if round(out[0, 0]) == y[0]:
                num_correct += 1


    return num_correct / num_samples

def train_sum():
    x = [(0, 0), (0, 1), (1, 0), (1, 1)]
    y = [(0, 0), (0, 1), (0, 1), (1, 0)]

    for i in range(len(x)):
        x[i] = np.array(x[i])
        y[i] = np.array(y[i])

    weights = [None]        
    biases = [None]

    weights.append(np.random.random((2, 2)) * 2 - 1)
    weights.append(np.random.random((2, 2)) * 2 - 1)

    biases.append(np.random.random((2, 1)) * 2 - 1)
    biases.append(np.random.random((2, 1)) * 2 - 1)

    weights, biases = train_network(
        sigmoid, sigmoid_prime, x, y, weights, biases, 2500, 5, None, False
    )

    # print(); iprint(weights); print(); iprint(biases); print()

    print(accuracy(weights, biases, x, y, sigmoid, True))

def train_circle():
    # 2 - 12 - 4 - 1 network

    x, y = [], []
    for i in range(10000):
        x.append(np.random.random((2,)) * 2 - 1)
        if (x[-1][0] ** 2 + x[-1][1] ** 2)**0.5 < 1:
            y.append(np.array([1]))
        else:
            y.append(np.array([0]))

    weights = [None]
    biases = [None]

    weights.append(np.random.random((12, 2)) * 2 - 1)
    weights.append(np.random.random((4, 12)) * 2 - 1)
    weights.append(np.random.random((1, 4)) * 2 - 1)

    biases.append(np.random.random((12, 1)) * 2 - 1)
    biases.append(np.random.random((4, 1)) * 2 - 1)
    biases.append(np.random.random((1, 1)) * 2 - 1)

    weights, biases = train_network(
        sigmoid, sigmoid_prime, x, y, weights, biases, 30, 0.18, lr_scaler, True
    )

    print("\n\r")
    num_wrong = 10000 - accuracy(weights, biases, x, y, sigmoid, False) * 10000
    print(f"# Incorrectly Classified Points: {num_wrong}")

def runner_2():
    args = sys.argv[1:]
    assert len(args) == 1
    if args[0] == "S":
        train_sum()
    elif args[0] == "C":
        train_circle()
    else:
        import antigravity

def generate_initial_weights_biases(layers):
    weights = [None]
    biases = [None]

    # first layer
    weights.append(np.random.random((layers[1], layers[0])) * 2 - 1)
    biases.append(np.random.random((layers[1], 1)) * 2 - 1)

    # rest of the layers
    for i in range(2, len(layers)):
        weights.append(np.random.random((layers[i], layers[i-1])) * 2 - 1)
        biases.append(np.random.random((layers[i], 1)) * 2 - 1)

    return weights, biases

def accuracy_list(weights, biases, input, output, A_vec):
    num_correct = 0

    assert len(input) == len(output)
    num_samples = len(input)

    for x, y in zip(input, output):
        out = p_net(A_vec, weights, biases, x)
        if np.argmax(out) == np.argmax(y): # if the index of the max value is the same
            num_correct += 1

    return num_correct / num_samples

def train_mnist():
    # load data from csv
    train = np.loadtxt("MNIST/mnist_train.csv", delimiter=",")
    test = np.loadtxt("MNIST/mnist_test.csv", delimiter=",")

    # split into inputs and outputs
    train_x = train[:, 1:]
    train_y = train[:, 0]

    test_x = test[:, 1:]
    test_y = test[:, 0]

    # normalize inputs
    train_x = train_x / 255
    test_x = test_x / 255

    # convert outputs to a 10x1 array instad of number from 0-9
    train_y = np.array([np.array([1 if i == j else 0 for i in range(10)]) for j in train_y])
    test_y = np.array([np.array([1 if i == j else 0 for i in range(10)]) for j in test_y])

    print(train_x.shape, train_y.shape, test_x.shape, test_y.shape)

    weights, biases = generate_initial_weights_biases([784, 392, 10])

    print(accuracy_list(weights, biases, test_x, test_y, sigmoid))
    weights, biases = train_network(
        sigmoid, sigmoid_prime, train_x, train_y, weights, biases, 10, 0.1, lr_scaler, False)
    
    # test accuracy
    print(accuracy_list(weights, biases, test_x, test_y, sigmoid))


if __name__ == "__main__":
    # train_mnist()
    runner_2()