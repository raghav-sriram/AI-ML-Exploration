import sys
import csv
from math import log2
import matplotlib.pyplot as plt
from random import sample, shuffle, randrange

def load_dataset(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        dataset = list(reader)
    return dataset

titles = sys.argv[1]
dataset = load_dataset(titles)
CSVFILE = dataset[1:]

TYPES = tuple(dataset[0])

def entropy_solve(entropic):
    counts = {}
    for x in entropic:
        if x[-1] in counts:
            counts[x[-1]] += 1
        else:
            counts[x[-1]] = 1
    keys = counts.values()
    return_vals = 0
    length = len(entropic)

    for x in keys:
        return_vals = return_vals - (x/length*log2(x/length))
    return return_vals

def trait_entropy(entropic, trait):
    counts = {}
    t = TYPES.index(trait)
    for x in entropic:
        if not x[t] in counts:
            counts[x[t]] = {}
            counts[x[t]][x[-1]] = 1
        elif not x[-1] in counts[x[t]]:
            counts[x[t]][x[-1]] = 1
        else:
            counts[x[t]][x[-1]] = counts[x[t]][x[-1]] + 1
    
    return_vals = 0
    for y in counts:
        vays = counts[y].values()
        traiters = 0
        vvayss = counts[y].values()
        for z in vvayss:
            traiters = traiters - (z/sum(vays)*log2(z/sum(vays)))
        
        length = len(entropic)
        summon = sum(vays)
        return_vals = return_vals + summon/length * traiters

    return return_vals

class Node:
    def __init__(self, feature=None, children=None, label=None):
        self.feature = feature
        self.children = children
        self.label = label

class DecisionTree:
    def __init__(self):
        self.tree = None

    def train(self, dataset, depth):
        self.tree = self.generate_tree(dataset, depth)

    def generate_tree(self, dataset, depth):
        if depth == 0 or len(dataset) == 0:
            return None
        
        labels = [row[-1] for row in dataset]
        if len(set(labels)) == 1:
            return Node(label=labels[0])
        
        best_feature, best_gain = self.get_best_feature(dataset)
        if best_gain == 0:
            return Node(label=self.get_majority_label(dataset))

        node = Node(feature=best_feature)
        values = set([row[best_feature] for row in dataset])
        node.children = {}
        for value in values:
            sub_dataset = self.split_dataset(dataset, best_feature, value)
            sub_tree = self.generate_tree(sub_dataset, depth - 1)
            node.children[value] = sub_tree

        return node

    def get_best_feature(self, dataset):
        features = len(dataset[0]) - 1
        entropy = entropy_solve(dataset)
        best_feature = -1
        best_gain = 0

        for i in range(features):
            gain = entropy - self.get_information_gain(dataset, i)
            if gain > best_gain:
                best_gain = gain
                best_feature = i
        
        return best_feature, best_gain

    def get_information_gain(self, dataset, feature):
        values = set([row[feature] for row in dataset])
        entropy = entropy_solve(dataset)
        gain = 0

        for value in values:
            sub_dataset = self.split_dataset(dataset, feature, value)
            weight = len(sub_dataset) / len(dataset)
            entropy_sub = entropy_solve(sub_dataset)
            gain += weight * entropy_sub

        return gain

    def split_dataset(self, dataset, feature, value):
        return [row for row in dataset if row[feature] == value]

    def get_majority_label(self, dataset):
        labels = [row[-1] for row in dataset]
        counts = {}
        for label in labels:
            if label in counts:
                counts[label] += 1
            else:
                counts[label] = 1
        return max(counts, key=counts.get)

    def classify(self, sample):
        return self.classify_sample(sample, self.tree)

    def classify_sample(self, sample, node):
        if node.label is not None:
            return node.label
        
        feature = node.feature
        value = sample[feature]
        if value not in node.children:
            return self.get_majority_label(self.split_dataset(dataset, feature, value))
        
        child = node.children[value]
        return self.classify_sample(sample, child)

class RandomForest:
    def __init__(self, num_trees=10, sample_proportion=0.1):
        self.num_trees = num_trees
        self.sample_proportion = sample_proportion
        self.trees = []

    def train(self, dataset, depth):
        self.trees = []
        for _ in range(self.num_trees):
            sample_size = int(len(dataset) * self.sample_proportion)
            sample_data = sample(dataset, sample_size)
            tree = DecisionTree()
            tree.train(sample_data, depth)
            self.trees.append(tree)

    def classify(self, sample):
        labels = [tree.classify(sample) for tree in self.trees]
        return max(set(labels), key=labels.count)

shuffle(CSVFILE)
rain = int(sys.argv[2])
uses = CSVFILE[-rain:]
OhMyDays = CSVFILE[:-rain]
plotter = []

for x in range(int(sys.argv[3]), int(sys.argv[4]) + 1, int(sys.argv[5])):
    samplesize = sample(OhMyDays, x)
    while entropy_solve(samplesize) == 0:
        samplesize = sample(OhMyDays, x)
    acculumation = 0
    forest = RandomForest(num_trees=10, sample_proportion=0.1)
    forest.train(samplesize, depth=5)

    for y in uses:
        if y[-1] == forest.classify(y):
            acculumation += 1

    apparent = len(uses)
    apparently = acculumation / apparent

    plotter.append((x, apparently))

title = titles[:-4].capitalize()
plt.scatter(*zip(*plotter))
plt.ylabel("Accuracy (%)")
plt.xlabel("Training Set Size")
plt.title(title)
plt.show()


