# Raghav Sriram
# Monday 4/24/2023
# Unit 8 Supervised Machine Learning
# Decision Trees, Part 1.



from  collections import Counter
from math import log2
import sys

with open(sys.argv[1]) as file:
    f = file.read()
    headers = f.splitlines()[0].split(",")
    dataset = [dict(zip(headers, x.split(","))) for x in f.splitlines()[1:]]                    #96

def splitter(data,feat,val):
    retList = list()
    for x in data:
        if x[feat] == val:
            retList.append(x)
    return retList

def calc_entropy(data,feat):
    counts = Counter([x[feat] for x in data])
    lengths = len(data)
    return sum([log2(w:= x/lengths)*-1*w for x in counts.values()])
    
def info_gain(data,feat,target):
    terms = [x[feat] for x in data]
    tot, terms = len(data),set(terms) # holds every value of the attribute for example Outlook would have Sunny, Overcast, Rainy,,
    subsets = [splitter(data,feat,x) for x in terms]
    entropies = [(calc_entropy(s,target),s) for s in subsets]

    entropy = sum([len(e[1])/tot*e[0] for e in entropies])
    ent = calc_entropy(data,target)
    return ent - entropy

def recur(data,feats,depth,target):
    max = float("-inf")
    le = [x[target] for x in data]
    le = set(le)
    if len(le) == 1 or len(feats) == 0: 
        leaf = {"leaf?": "yes", "term": data[0][target]}
        return leaf
    feat = feats[0]
    for f in feats:
        info = info_gain(data,f,target)
        if max < info:
            feat  = f
            max = info
    sub = {"leaf?": "not", "feats": feat,"childs": dict()}
    feats = [f for f in feats if f != feat]  # remove a feature
    vals = [x[feat] for x in data]
    vals = set(vals) 
    tot = len(data)
    for x in vals:
        subsets = splitter(data,feat,x) # holds every value of the attribute for example Outlook would have Sunny, Overcast, Rainy,,
        if subsets:
            sub['childs'][x] = recur(subsets,feats,1+depth,target)
    return sub


def display(tree, mark="", file=None):

    if tree["leaf?"] == "yes":
        print("-->", tree["term"], file=file)
    else:
        print(mark + "*",tree["feats"] + "?", file=file)
        mark += "  "
        for key, child in tree["childs"].items():
            if child["leaf?"] == "not":
                print(mark + "*", key, file=file)
            else:
                print(mark + "*", key, end=" ", file=file)
            display(child, mark + "  ", f)

    return tree

# data = [{'Outlook': 'Sunny', 'Temp': 'Hot', 'Humidity': 'High', 'Wind': 'Weak', 'Play?': 'No'}, {'Outlook': 'Sunny', 'Temp': 'Hot', 'Humidity': 'High', 'Wind': 'Strong', 'Play?': 'No'}, {'Outlook': 'Overcast', 'Temp': 'Hot', 'Humidity': 'High', 'Wind': 'Weak', 'Play?': 'Yes'}, {'Outlook': 'Rain', 'Temp': 'Mild', 'Humidity': 'High', 'Wind': 'Weak', 'Play?': 'Yes'}, {'Outlook': 'Rain', 'Temp': 'Cool', 'Humidity': 'Normal', 'Wind': 'Weak', 'Play?': 'Yes'}, {'Outlook': 'Rain', 'Temp': 'Cool', 'Humidity': 'Normal', 'Wind': 'Strong', 'Play?': 'No'}, {'Outlook': 'Overcast', 'Temp': 'Cool', 'Humidity': 'Normal', 'Wind': 'Strong', 'Play?': 'Yes'}, {'Outlook': 'Sunny', 'Temp': 'Mild', 'Humidity': 'High', 'Wind': 'Weak', 'Play?': 'No'}, {'Outlook': 'Sunny', 'Temp': 'Cool', 'Humidity': 'Normal', 'Wind': 'Weak', 'Play?': 'Yes'}, {'Outlook': 'Rain', 'Temp': 'Mild', 'Humidity': 'Normal', 'Wind': 'Weak', 'Play?': 'Yes'}, {'Outlook': 'Sunny', 'Temp': 'Mild', 'Humidity': 'Normal', 'Wind': 'Strong', 'Play?': 'Yes'}, {'Outlook': 'Overcast', 'Temp': 'Mild', 'Humidity': 'High', 'Wind': 'Strong', 'Play?': 'Yes'}, {'Outlook': 'Overcast', 'Temp': 'Hot', 'Humidity': 'Normal', 'Wind': 'Weak', 'Play?': 'Yes'}, {'Outlook': 'Rain', 'Temp': 'Mild', 'Humidity': 'High', 'Wind': 'Strong', 'Play?': 'No'}]
target = headers.pop()
# print(info_gain(dataset,headers[0],target))
# print(calc_entropy(dataset,target))
# print(data)
# print(headers)

tree = recur(dataset,headers,0,target)
# display(data,headers,"Play?")
with open("treeout.txt", "w") as f:
    display(tree,"",f)

# {'leaf?': 'not', 'feats': 'Outlook', 'Depth': 0, 'childs': {'Overcast': {'leaf?': 'yes', 'val': 'Yes', 'Depth': 1}, 'Sunny': {'leaf?': 'not', 'feats': 'Humidity', 'Depth': 1, 'childs': {'Normal': {'leaf?': 'yes', 'val': 'Yes', 'Depth': 2}, 'High': {'leaf?': 'yes', 'val': 'No', 'Depth': 2}}}, 'Rain': {'leaf?': 'not', 'feats': 'Wind', 'Depth': 1, 'childs': {'Strong': {'leaf?': 'yes', 'val': 'No', 'Depth': 2}, 'Weak': {'leaf?': 'yes', 'val': 'Yes', 'Depth': 2}}}}}







