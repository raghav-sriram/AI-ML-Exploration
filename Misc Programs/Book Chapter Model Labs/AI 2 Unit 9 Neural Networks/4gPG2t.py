import sys
import itertools

def activation_function(x):
    return 1 if x >= 0 else 0

def dot_product(a, b):
    return sum(x * y for x, y in zip(a, b))

def perceptron_training_algorithm(truth_table, learning_rate, max_epochs):
    n = len(truth_table[0][0])
    weights = [0] * n
    bias = 0

    for _ in range(max_epochs):
        prev_weights = weights.copy()
        prev_bias = bias

        for input_vector, target_output in truth_table:
            current_output = activation_function(dot_product(weights, input_vector) + bias)
            error = target_output - current_output

            weights = [w + learning_rate * error * x for w, x in zip(weights, input_vector)]
            bias += learning_rate * error

        if weights == prev_weights and bias == prev_bias:
            break

    return weights, bias

def calculate_accuracy(truth_table, weights, bias):
    correct = 0
    total = len(truth_table)

    for input_vector, target_output in truth_table:
        current_output = activation_function(dot_product(weights, input_vector) + bias)
        if current_output == target_output:
            correct += 1

    return correct / total

def main():
    num_bits = int(sys.argv[1])
    canonical_int_representation = int(sys.argv[2])
    learning_rate = 0.1
    max_epochs = 100

    input_vectors = list(itertools.product([0, 1], repeat=num_bits))
    truth_table = [(list(input_vector), (canonical_int_representation >> i) & 1) for i, input_vector in enumerate(input_vectors)]

    weights, bias = perceptron_training_algorithm(truth_table, learning_rate, max_epochs)
    accuracy = calculate_accuracy(truth_table, weights, bias)

    print("Final weight vector:", weights)
    print("Final bias value:", bias)
    print("Accuracy:", accuracy * 100, "%")

if __name__ == "__main__":
    main()
