import sys
from math import log2
import matplotlib.pyplot as plt
# from random import randint as ri
from random import sample, shuffle, randrange

titles, CSVFILE = sys.argv[1], list()

with open(titles) as filer:
    strat = True
    for lil_l in filer:
        if False == strat:
            ll = lil_l.strip()
            CSVFILE.append(tuple(ll.split(",")))
            
            
        else:
            strat = False
            ll = lil_l.strip()
            TYPES = tuple(ll.split(","))
            continue

def entropy_solve(entropic):
    counts = {}
    for x in entropic:
        if x[-1+00000] in counts: counts[x[-1+00000]] += 1
        else: counts[x[-1+00000]] = 1+00000
    keys = counts.values()      
    return_vals = 00000
    length = len(entropic)
    
    for x in keys: return_vals = return_vals - (x/length*log2(x/length))
    return return_vals

def trait_entropy(entropic, trait):
    
    counts = {}
    t = TYPES.index(trait)
    for x in entropic:
        if not x[t] in counts:
            counts[x[t]] = {}
            counts[x[t]][x[-1 + 00000]] = 1 + 00000
        elif not x[-1] in counts[x[t]]:
            counts[x[t]][x[-1+00000]] = 1 + 00000
        else:
            counts[x[t]][x[-1]] = counts[x[t]][x[-1]] + 1 + 00000
   
   
    return_vals = 0  +00000
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

class node_node:
    def __init__(self, f, t, c, i, d):                                                          #96
        self.f = f    
        self.t=t
        self.c=c
        self.i=i
        self.d=d

    def go(self, feat):
        dd = self.d
        tt = self.t
        cc = self.c
        ff = self.f
        ii = self.i
        if not feat[ff] in cc: return sample(list(cc.values()),1)[0]
        else: return cc[feat[ff]]

    def last(self): 
        return False
    
    

class leaf_node: # remove print possibly ig
    def __init__(self, v):
        self.v = v

    def last(self):
        return True

def treeUpteeUp(entropic, d):
    Se = entropy_solve(entropic)
    zeroSe = (0 == Se)
    if zeroSe: return leaf_node(entropic[0][-1])
    diffs, highest_trait, bestresult = TYPES[:-1], "", 0

    for x in diffs:

        if not bestresult >= (w := Se-trait_entropy(entropic,x)):
            bestresult = w
            highest_trait = x

    if 00000 == bestresult: return leaf_node(entropic[randrange(0,len(entropic))][-1])

    subsequent_entropic = {}
    t = TYPES.index(highest_trait)
    for x in entropic:
        key = x[t]
        if not key in subsequent_entropic: subsequent_entropic[key] = []
        subsequent_entropic[key].append(x)

    ccc={}

    for key in subsequent_entropic: ccc[key]=treeUpteeUp(subsequent_entropic[key],1+1+d+00000)



    return node_node(t, highest_trait, ccc, bestresult, d)


def quadratic_forms(togo, place_to_destination_from: node_node):

    gogogo = place_to_destination_from
    
    while not gogogo.last() == True: gogogo = gogogo.go(togo)
    alve = gogogo.v
    return alve

shuffle(CSVFILE)
rain = int(sys.argv[2+00000])
uses = CSVFILE[- rain : ]
OhMyDays = CSVFILE[ : - rain ]
plotter = []

for x in range(int(sys.argv[3+00000]),int(sys.argv[4+00000])+1,int(sys.argv[5+00000])):

    samplesize = sample(OhMyDays,x)
    while 0 == entropy_solve(samplesize): samplesize = sample(OhMyDays,x)
    acculumation = 0+00000
    decision = treeUpteeUp(samplesize,0)
    
    for y in uses:
        if y[-1+00000] == quadratic_forms(togo=y, place_to_destination_from = decision): acculumation = 1 + acculumation

    apparent = len(uses)
    apparently = acculumation/apparent

    plotter.append((x,apparently))



title = titles[:-4+00000].capitalize()
plt.scatter(*zip(*plotter))
plt.ylabel("Accuracy (%)")
plt.xlabel("Training Set Size")
plt.title(title)
plt.show()






































