import sys
import csv
import math
from collections import Counter

# Read CSV file
def read_csv(filename):
    with open(filename, 'r') as file:
        lines = file.read().splitlines()
        print(lines)
        headers = lines[0].split(',')
        print(headers)
        data = [dict(zip(headers, row.split(','))) for row in lines[1:]]
        print("yorepi!")
        print(data)
    return data


# Calculate entropy
def entropy(data, target_attribute):
    target_values = [row[target_attribute] for row in data]
    print(target_values)
    counter = Counter(target_values)
    total = len(data)
    entropy = sum([(-count / total) * math.log2(count / total) for count in counter.values()])
    return entropy

# Split data by attribute value
def split_data(data, attribute, value):
    return [row for row in data if row[attribute] == value]

# Calculate information gain
def information_gain(data, attribute, target_attribute):
    total_entropy = entropy(data, target_attribute)
    total_count = len(data)
    
    values = set(row[attribute] for row in data)
    weighted_entropy = sum([(len(subset) / total_count) * entropy(subset, target_attribute) for value in values for subset in [split_data(data, attribute, value)]])
    
    return total_entropy - weighted_entropy

# Build decision tree
def build_decision_tree(data, attributes, target_attribute, depth=0):
    if len(set(row[target_attribute] for row in data)) == 1:
        return {
            'type': 'leaf',
            'value': data[0][target_attribute],
            'depth': depth
        }
    
    best_attribute = max(attributes, key=lambda attribute: information_gain(data, attribute, target_attribute))
    attributes.remove(best_attribute)
    subtree = {
        'type': 'node',
        'attribute': best_attribute,
        'depth': depth,
        'children': {}
    }

    for value in set(row[best_attribute] for row in data):
        child_data = split_data(data, best_attribute, value)
        if child_data:
            subtree['children'][value] = build_decision_tree(child_data, attributes[:], target_attribute, depth + 1)
    
    return subtree

# Print decision tree
def print_tree(tree, file):
    if tree['type'] == 'leaf':
        print(' ' * tree['depth'] * 2, '-->', tree['value'], file=file)
    else:
        print(' ' * tree['depth'] * 2, tree['attribute'] + '?', file=file)
        for value, child in tree['children'].items():
            print(' ' * (tree['depth'] * 2 + 1), value, file=file)
            print_tree(child, file)

# Main function
def main(input_file):
    data = read_csv(input_file)
    attributes = list(data[0].keys())
    target_attribute = attributes.pop()
    # print(attributes)
    # print(target_attribute)
    # print(entropy(data,"Play?"))
    # input()
    tree = build_decision_tree(data, attributes, target_attribute)
    
    with open('treeout.txt', 'w') as output_file:
        print_tree(tree, output_file)

if __name__ == '__main__':
    main(sys.argv[1])
