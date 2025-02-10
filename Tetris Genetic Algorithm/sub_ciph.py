import math
import random


import sys


SIZE, POPULATION_SIZE, NUM_CLONES, TOURNAMENT_SIZE, TOURNAMENT_WIN_PROBABILITY, CROSSOVER_LOCATIONS, MUTATION_RATE = (
    4,
    500,
    1,
    20,
    0.75,
    5,
    0.8
)

dicty = dict()

ALPHABLUE = "ETAOINSHRDLCUMWFGYPBVKXJQZ"

REPLACE_COUNT = POPULATION_SIZE // 20
HILL_CLIMBING_INTERVAL = 5
HILL_CLIMBING_INTERVAL_ITERS = 750

def encode_message(message, encryption_key):
    encoded_message = ""
    for character in message:
        if character.isalpha():
            if character.isupper():
                encoded_message += encryption_key[character.lower()].upper()
            else:
                encoded_message += encryption_key[character]
        else:
            encoded_message += character
    return encoded_message


def decode(ciphertext, decryption_key):
    plaintext = ""
    for character in ciphertext:
        if character.isalpha():
            found = False
            for key, value in decryption_key.items():
                if value == character:
                    plaintext += key
                    found = True
                    break
            if not found:
                plaintext += character
        else:
            plaintext += character
    return plaintext


def generate_ngram_dict(file):
    global dicty
    with open(file, "r") as f:
        for line in f:
            ngram, count = line.split(" ")
            if len(ngram) == SIZE:
                dicty[ngram] = int(count)

def ngram_fitness(cipher_text):
    fitness = 0
    for i in range(len(cipher_text) - SIZE + 1):
        ngram = cipher_text[i:i+SIZE]
        if ngram in dicty.keys():
            fitness += math.log(dicty[ngram] + 1, 2)
    # log fitness to make it more linear
    return fitness  # add 1 to avoid log(0)

def hill_climbing(encoded_msg, max_iters=100000, print_results=False, key=None):
    if key is None:
        # generate random cipher alphabet
        letters = list(ALPHABLUE)
        random.shuffle(letters)
        key = dict(zip(ALPHABLUE, letters))

    # keep track of the best key and its fitness
    best_key = key
    best_fitness = ngram_fitness(encoded_msg)

    if print_results:
        print("Initial fitness:", best_fitness)
        print("Initial Decoded message:", decoded:=decode(encoded_msg, best_key))

    # loop forever
    iter = 0
    while True:
        # generate a new key by swapping two letters
        new_key = best_key.copy()
        a, b = random.sample(ALPHABLUE, 2)
        new_key[a], new_key[b] = new_key[b], new_key[a] # random swap

        # calculate the fitness of the new key
        new_fitness = ngram_fitness(decoded:=decode(encoded_msg, new_key))

        # if the new key is better, keep it
        if new_fitness > best_fitness:
            best_key = new_key
            best_fitness = new_fitness
            if print_results:
                print("New best fitness:", best_fitness)
                print("Decoded message:", decoded:=decode(encoded_msg, best_key))
        else:
            # otherwise, swap the letters back
            new_key[a], new_key[b] = new_key[b], new_key[a]
        iter += 1
        if print_results:
            print(f"Iteration: {iter}, curr fitness {new_fitness}, best fitness {best_fitness}", end="\r") # \r is realy cool - same line
        if iter >= max_iters:
            return (best_key, best_fitness)

def gen_initial_population(encoded_text):
    # each item in population is (key, fitness)
    population = []
    for i in range(POPULATION_SIZE - REPLACE_COUNT):
        letters = list(ALPHABLUE)
        random.shuffle(letters)
        key = dict(zip(ALPHABLUE, letters))
        fitness = ngram_fitness(decode(encoded_text, key))
        population.append((key, fitness))
    # generate some using hill climbing
    for i in range(REPLACE_COUNT):
        print("Generating initial population:", i + 1, "/", REPLACE_COUNT, end="\r")
        best = hill_climbing(encoded_text, 25, False)
        population.append(best)
    return population

def tournament_selection(population):
    # select TOURNAMENT_SIZE random members of the population
    # and return the one with the highest fitness
    parent1 = parent2 = None
    competitors = random.sample(population, TOURNAMENT_SIZE * 2)
    competitors = sorted(competitors, key=lambda x: x[1]) # sort by fitness from highest to lowest
    for i in range(TOURNAMENT_SIZE):
        if random.random() < TOURNAMENT_WIN_PROBABILITY:
            parent1 = competitors[i]
    for i in range(TOURNAMENT_SIZE, TOURNAMENT_SIZE * 2):
        if random.random() < TOURNAMENT_WIN_PROBABILITY:
            parent2 = competitors[i]
    return parent1, parent2

def breed(p1, p2, encoded_text):
    # generate 1 child from 2 parents
    child = [None] * len(ALPHABLUE)
    # put in the letters from parent1 at random locations
    # sample random indices 
    parent1, parent2 = list(p1.values()), list(p2.values())
    indices = random.sample(range(len(ALPHABLUE)), CROSSOVER_LOCATIONS)
    for i in indices:
        child[i] = parent1[i]
    # fill in the rest of the child with the letters from parent2
    # in the order they appear in parent2
    j = 0
    for i in range(len(ALPHABLUE)):
        if child[i] is None:
            while parent2[j] in child:
                j += 1
            child[i] = parent2[j]
    # convert the child to a dictionary
    child = dict(zip(ALPHABLUE, child))
    # evaluate the child's fitness
    fitness = ngram_fitness(decode(encoded_text, child))
    return (child, fitness)

def genetic_algorithm(encoded_text):
    population = gen_initial_population(encoded_text)
    # keep track of the best key and its fitness
    best_key = None
    best_fitness = 0
    # loop forever
    iter = 0
    while True:
        new_population = []
        # if iter is large enough, use hill climbing to find a better key
        if (iter+1) % HILL_CLIMBING_INTERVAL == 0:
            best = hill_climbing(encoded_text, HILL_CLIMBING_INTERVAL_ITERS, True, best_key)
            if best[1] > best_fitness:
                best_key = best[0]
                best_fitness = best[1]
                new_population.append(best)
        # copy some clones
        clones = random.sample(population, NUM_CLONES)
        new_population.extend(clones)
        # for the rest of the population, breed
        while len(new_population) < POPULATION_SIZE:
            parent1, parent2 = tournament_selection(population)
            child = breed(parent1[0], parent2[0], encoded_text)
            if child in population:
                continue
            new_population.append(child)
        # sort the population by fitness
        population = sorted(new_population, key=lambda x: x[1], reverse=True)
        # keep track of the best key and its fitness
        if population[0][1] > best_fitness:
            best_key = population[0][0]
            best_fitness = population[0][1]
            print("New best fitness:", best_fitness)
            print("Decoded message:", decode(encoded_text, best_key))
        iter += 1
        print(f"Iteration: {iter}, curr fitness {population[0][1]}, best fitness {best_fitness}", end="\r") 
        if iter == 500:
            print("Iteration 500. Exiting")
            sys.exit(1)



if __name__ == "__main__":
    generate_ngram_dict("ngrams.txt")

    test_string = """
    PF HACYHTTRQ VF N PBYYRPGVBA BS SERR YRNEAVAT NPGVIVGVRF GUNG
GRNPU PBZCHGRE FPVRAPR GUEBHTU RATNTVAT TNZRF NAQ CHMMYRF GUNG
HFR PNEQF, FGEVAT, PENLBAF NAQ YBGF BS EHAAVAT NEBHAQ. JR

BEVTVANYYL QRIRYBCRQ GUVF FB GUNG LBHAT FGHQRAGF PBHYQ QVIR URNQ-
SVEFG VAGB PBZCHGRE FPVRAPR, RKCREVRAPVAT GUR XVAQF BS DHRFGVBAF

NAQ PUNYYRATRF GUNG PBZCHGRE FPVRAGVFGF RKCREVRAPR, OHG JVGUBHG
UNIVAT GB YRNEA CEBTENZZVAT SVEFG. GUR PBYYRPGVBA JNF BEVTVANYYL
VAGRAQRQ NF N ERFBHEPRz SBE BHGERNPU NAQ RKGRAFVBA, OHG JVGU GUR
NQBCGVBA BS PBZCHGVAT NAQ PBZCHGNGVBANY GUVAXVAT VAGB ZNAL
PYNFFEBBZF NEBHAQ GUR JBEYQ, VG VF ABJ JVQRYL HFRQ SBE GRNPUVAT.
GUR ZNGREVNY UNF ORRA HFRQ VA ZNAL PBAGRKGF BHGFVQR GUR PYNFFEBBZ
NF JRYY, VAPYHQVAT FPVRAPR FUBJF, GNYXF SBE FRAVBE PVGVMRAF, NAQ
FCRPVNY RIRAGF. GUNAXF GB TRAREBHF FCBAFBEFUVCF JR UNIR ORRA
NOYR GB PERNGR NFFBPVNGRQ ERFBHEPRF FHPU NF GUR IVQRBF, JUVPU NER
VAGRAQRQ GB URYC GRNPUREF FRR UBJ GUR NPGVIVGVRF JBEX (CYRNFR
QBA’G FUBJ GURZ GB LBHE PYNFFRF – YRG GURZ RKCREVRAPR GUR
NPGVIVGVRF GURZFRYIRF!). NYY BS GUR NPGVIVGVRF GUNG JR CEBIVQR
NER BCRA FBHEPR – GURL NER ERYRNFRQ HAQRE N PERNGVIR PBZZBAF
NGGEVOHGVBA-FUNERNYVXR YVPRAPR, FB LBH PNA PBCL, FUNER NAQ ZBQVSL
GUR ZNGREVNY. SBE NA RKCYNANGVBA BA GUR PBAARPGVBAF ORGJRRA PF
HACYHTTRQ NAQ PBZCHGNGVBANY GUVAXVAT FXVYYF, FRR BHE
PBZCHGNGVBANY GUVAXVAT NAQ PF HACYHTTRQ CNTR. GB IVRJ GUR GRNZ
BS PBAGEVOHGBEF JUB JBEX BA GUVF CEBWRPG, FRR BHE CRBCYR CNTR.
SBE QRGNVYF BA UBJ GB PBAGNPG HF, FRR BHE PBAGNPG HF CNTR. SBE
ZBER VASBEZNGVBA NOBHG GUR CEVAPVCYRF ORUVAQ PF HACYHTTRQ, FRR
BHE CEVAPVCYRF CNTR."""
    genetic_algorithm(test_string)