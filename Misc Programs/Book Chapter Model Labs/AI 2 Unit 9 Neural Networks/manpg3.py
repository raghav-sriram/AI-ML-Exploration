import sys
import math
import ast


def baseten_2_binary(n):
    # convert base 10 to binary
    # return list of bits
    bits = []
    while n > 0:
        bits.append(n % 2)
        n = n // 2
    bits.reverse()
    if len(bits) == 0:
        bits.append(0)
    return bits


def truth_table(bits, n):
    # dict: (input,...) -> output
    # truth_table(2, 5) --> (((1,1),0), ((1,0),1), ((0,1),0), ((0,0),1))

    # first, generate inputs
    inputs = []
    for i in range(2**bits):
        inputs.append(baseten_2_binary(i))
    # print(inputs)
    # pad inputs with 0s
    for i in range(len(inputs)):
        while len(inputs[i]) < bits:
            inputs[i].insert(0, 0)
    # print(inputs)
    inputs = list(reversed(inputs))
    # print(inputs)

    # generate outputs
    num = baseten_2_binary(n)
    for i in range(len(num)):
        while len(num) < 2**bits:
            num.insert(0, 0)
    outputs = {}
    for i in range(len(inputs)):
        outputs[tuple(inputs[i])] = num[i]
    return outputs


def pretty_print_tt(table):
    print()
    # print headers
    print("Inputs | Output")
    print("-------+-------")
    # print table
    for key in table:
        print(str(key) + " | " + str(table[key]))
    print()


def generate_all_truth_tables(n):
    # generate all ttables with n bits
    ttables = []
    for i in range(2 ** (2**n)):
        ttables.append(truth_table(n, i))
    return ttables


def step(num):
    if num > 0:
        return 1
    else:
        return 0


def dot_product(a, b):
    # a and b are lists of equal length
    # return dot product
    assert len(a) == len(b), "equal len"
    dot = 0
    for i in range(len(a)):
        dot += a[i] * b[i]
    return dot


def perceptron(A, w, b, x):
    # A = activation function
    # w = weights
    # b = bias
    # x = inputs
    output = A(dot_product(w, x) + b)
    assert type(output) in (int, float), "numrerical output"
    return output


def check(n, w, b, ttable=None):
    # Boolean integer n
    # Weight vector w
    # Bias b
    num_correct = 0
    if ttable == None:
        ttable = truth_table(len(w), n)
    else:
        ...  # ttable is given
    for key in ttable:
        output = perceptron(step, w, b, key)
        if output == ttable[key]:
            num_correct += 1
    return num_correct / len(ttable)


def train(A, w, table, b, lr, epochs):
    # (lr) lambda - learning rate
    outputs = []
    for i in range(epochs):
        for key in table:  # for each input
            output = perceptron(A, w, b, key)
            error = table[key] - output
            for j in range(len(w)):
                w[j] += lr * error * key[j]  # update weights
            b += lr * error
        outputs.append((tuple(w), b))
        if len(outputs) > 1:
            if outputs[-1] == outputs[-2]:  # 2 consecutive
                return outputs[-1]  # answer, last output
    return outputs[-1]


def eval_table(table, n):
    perceptron = train(step, [0] * n, table, 0, 1, 100)
    accuracy = check(n, perceptron[0], perceptron[1], table)
    # print("[DEBUG]", accuracy, perceptron)
    # pretty_print_tt(table)
    return accuracy, perceptron


def evaluate_perfect_model(n):
    perfect_count = 0
    tables = generate_all_truth_tables(n)
    print(len(tables))
    for table in tables:
        accuracy, _perceptron = eval_table(table, n)
        if accuracy == 1:
            perfect_count += 1
    return perfect_count, len(tables)


def two_two_one_network(A, w3, b3, w4, b4, w5, b5, in1, in2):
    # XOR happens here

    # perceptron 3
    output3 = perceptron(A, w3, b3, [in1, in2])
    # perceptron 4
    output4 = perceptron(A, w4, b4, [in1, in2])
    # perceptron 5
    output5 = perceptron(A, w5, b5, [output3, output4])
    return output5


def main_1():
    args = sys.argv[1:]

    n_bits = int(args[0])
    input = ast.literal_eval(args[1])
    bias = float(args[2])

    accuracy = check(n_bits, input, bias)
    print(accuracy)


def main_2():
    args = sys.argv[1:]

    n_bits = int(args[0])
    binary_num = int(args[1])

    table = truth_table(n_bits, binary_num)
    accuracy, perceptron = eval_table(table, n_bits)
    print(f"Perceptron {perceptron} has accuracy {accuracy} on table {binary_num}")


def main_3():
    w3 = [-1, 1]
    b3 = 0

    w4 = [1, -1]
    b4 = 0

    w5 = [1, 1]
    b5 = 0

    A = step

    entries = ((1, 1), (1, 0), (0, 1), (0, 0))

    # for entry in entries:
    #     output = two_two_one_network(A, w3, b3, w4, b4, w5, b5, entry[0], entry[1])
    #     print(entry, output)

    entry = ast.literal_eval("(1,0)")
    output = two_two_one_network(A, w3, b3, w4, b4, w5, b5, entry[0], entry[1])
    print(output)


def main_5():
    import matplotlib.pyplot as plt
    import numpy as np

    # subplot 4x4
    ax, axs = plt.subplots(4, 4)

    # title entire figure
    ax.suptitle("Perceptron Viz - Manav Gagvani")

    for i, entry in enumerate(generate_all_truth_tables(2)):
        # print(entry.keys())
        # print(i)
        accuracy, _perceptron = eval_table(entry, 2)

        x_t1, y_t1, x_t2, y_t2 = [], [], [], []
        for ii in np.linspace(-2, 2, 20):
            for jj in np.linspace(-2, 2, 20):
                output = perceptron(step, _perceptron[0], _perceptron[1], [ii, jj])
                if output > 0.5:
                    x_t1.append(ii)
                    y_t1.append(jj)
                else:
                    x_t2.append(ii)
                    y_t2.append(jj)

        x_big_true = [x[0] for x in entry.keys() if entry[x] == 1]
        y_big_true = [x[1] for x in entry.keys() if entry[x] == 1]

        x_big_false = [x[0] for x in entry.keys() if entry[x] == 0]
        y_big_false = [x[1] for x in entry.keys() if entry[x] == 0]

        # plot
        idx1 = int(i // 4)
        idx2 = int(i % 4)
        # print(i, idx1, idx2)
        axs[idx1, idx2].scatter(x_t1, y_t1, color="lightcoral", s=1, marker=",")
        axs[idx1, idx2].scatter(x_t2, y_t2, color="powderblue", s=1, marker=",")

        axs[idx1, idx2].scatter(x_big_true, y_big_true, color="red", s=35)
        axs[idx1, idx2].scatter(x_big_false, y_big_false, color="green", s=35)

        axs[idx1, idx2].set(adjustable="box", aspect="equal")

        # label
        # axs[idx1, idx2].set_xlabel(f'{entry}')

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main_5()