import sys
import csv
import math
import operator
from collections import Counter

def entropy(data):
    outcomes = [row[-1] for row in data]
    counts = Counter(outcomes)
    total = len(outcomes)
    ent = 0
    for count in counts.values():
        p = count / total
        ent -= p * math.log2(p)
    return ent

def split_data(data, feature_index, value):
    split = [row for row in data if row[feature_index] == value]
    return split

def information_gain(data, feature_index):
    starting_entropy = entropy(data)
    feature_values = set(row[feature_index] for row in data)
    expected_entropy = 0
    for value in feature_values:
        split = split_data(data, feature_index, value)
        weight = len(split) / len(data)
        expected_entropy += weight * entropy(split)
    return starting_entropy - expected_entropy

def best_feature(data):
    num_features = len(data[0]) - 1
    gains = [information_gain(data, i) for i in range(num_features)]
    best_index, best_gain = max(enumerate(gains), key=operator.itemgetter(1))
    return best_index, best_gain

def build_tree(data, depth=0):
    if entropy(data) == 0:
        return [(depth, data[0][-1])]
    best_index, best_gain = best_feature(data)
    feature_values = sorted(set(row[best_index] for row in data))
    tree = []
    for value in feature_values:
        split = split_data(data, best_index, value)
        subtree = build_tree(split, depth + 1)
        tree.append((depth, f"{value}? (information gain: {best_gain})"))
        tree.extend(subtree)
    return tree

def read_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        return [row for row in reader]

def write_tree(tree):
    with open("treeout.txt", "w") as file:
        for depth, text in tree:
            file.write("  " * depth + text + "\n")

def main():
    if len(sys.argv) != 2:
        print("Usage: python decisiontreesBLUEg4.py play_tennis.csv")
        sys.exit(1)
    csv_file = "play_tennis.csv" # sys.argv[1]
    data = read_csv(csv_file)
    tree = build_tree(data)
    write_tree(tree)

if __name__ == "__main__":
    main()
