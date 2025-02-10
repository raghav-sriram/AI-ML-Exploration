# Raghav Sriram
# Tuesday 3/28/2023
# Unit 7 Unsupervised Machine Learning
# K-Means
# csv data from kaggle

import random
from math import log, sqrt

vector = list()
star_types = dict()

with open("star_data.csv") as stars:
    next(stars) #skipping the first line in stars
    # star_data = [line.strip() for line in stars]

    for s in stars:
        star = s.strip().split(",")
        vector.append(w:=(log(float(star[0])), log(float(star[1])), log(float(star[2])), float(star[3])))
        # star_types.append(float(star[4]))
        star_types[w] = float(star[4])

def K_Means(vect,k):
    K = k # step 1
    # random_numbers = [random.randint(0,len(vect)) for i in range(K)]
    # random_numbers = list()
    # i = 0
    # while i < K:
    #     randint = random.randint(0,len(vect))
    #     if not randint in random_numbers:
    #         random_numbers.append(randint)
    #         i+=1

    # means = [vect[x] for x in random_numbers]

    means = random.sample(vect,K) # step 2


    stable_means = None

    mapping = dict()
    

    # print(means)
    # input()
    ustable = True

    m = {x: [] for x in means}
    # means = stable_means
    for x in vect: # step 3
        min_dist = float("inf")
        stable_means = None
        for y in means:
            distance = dist(x,y)

            if distance < min_dist:
                min_dist = distance
                # x = y # try a dictionary and mapping x to y like {x: y}
                m[y].append(x)
                stable_means = []
    # print(mapping)
    # input()
    for y in m.values(): #find the average star data for each of the means star types
        # print(y)
        stable_means.append(average(y)) #average method doesn't work like this I think
    
    # print(means)
    # print(stable_means)
    # input()

    temp = stable_means
    stable_means = []
    means = temp
    # input()


    while ustable: # step 5
        mapping = {x: [] for x in means}
        # means = stable_means
        for x in vect: # step 3
            min_dist = float("inf")
            stable_means = None
            for y in means:
                distance = dist(x,y)

                if distance < min_dist:
                    min_dist = distance
                    closest_mean = y
                    # x = y # try a dictionary and mapping x to y like {x: y}
            mapping[closest_mean].append(x)
            stable_means = []
        # print(mapping)
        # input()
        for y in mapping.values(): #find the average star data for each of the means star types
            # print(y)
            stable_means.append(average(y)) # step 4
        
        # print(means)
        # print(stable_means)
        # input()

        if stable_means == means:
            ustable = False # step 6
            # input("means")

        temp = stable_means
        stable_means = None
        means = temp
        # input()
        return mapping
                                                


def dist(x,y):
    return sqrt( sum([(x[i]-y[i])**2 for i in range(len(x))]) )

def average(star_vectors):
    a1 = sum([x[0] for x in star_vectors])/len(star_vectors)
    a2 = sum([x[1] for x in star_vectors])/len(star_vectors)
    a3 = sum([x[2] for x in star_vectors])/len(star_vectors)
    a4 = sum([x[3] for x in star_vectors])/len(star_vectors)
    return (a1,a2,a3,a4)

spectral = K_Means(vector,6)
# print(spectral)
print()
i = 1
for x in spectral:
    print("Mean " + str(i) +": " + str(x))
    i+=1
    for y in spectral[x]:
        print(star_types[y],y)
    print()
    # input()
    # break