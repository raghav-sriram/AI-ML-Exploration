import math
import random
import string
import sys

POPULATION_SIZE = 500
NUM_CLONES = 1
TOURNAMENT_SIZE = 20
TOURNAMENT_WIN_PROBABILITY = 0.75
CROSSOVER_LOCATIONS = 10
MUTATION_RATE = 0.8


def code(string, cipher):
    return "".join([cipher[char.upper()] if char.upper() in cipher else char for char in string])



def sypher(pseudo_cipher, source=string.ascii_uppercase):
    cipher = dict()
    for i, char in enumerate(source):
        uppercase_char = char.upper()
        uppercase_pseudo_cipher = pseudo_cipher[i].upper()
        cipher[uppercase_char] = uppercase_pseudo_cipher
    return cipher



def build_ngrams_dict(filename): 
    return {line.split()[0]: int(line.split()[1]) for line in open(filename)}


def fitness_function(n, encoded_text, candidate_cipher):
    decoded_text = code(encoded_text, sypher(string.ascii_uppercase, candidate_cipher))
    ngram_list = [decoded_text[i:i + n] for i in range(len(decoded_text) - n + 1)]
    fitness_score = sum(math.log(ngrams_dict[ngram], 2) for ngram in ngram_list if ngram.isalpha() and ngram in ngrams_dict)
    return fitness_score


def shuffle(s):
    return "".join(random.sample(s, len(s)))



def swap(s, i, j):
    return s[:i] + s[j] + s[i + 1:j] + s[i] + s[j + 1:]


def random_swap(s):
    i, j = random.randint(0, len(s) - 1), random.randint(0, len(s) - 1); return s if i == j else swap(s, min(i, j), max(i, j))



def hill_climbing(n, encoded_text):
    how_fit = fitness_function(n, encoded_text, syph := shuffle(string.ascii_uppercase))

    while True:
        if not syph == (r := random_swap(syph)):
            if (w := fitness_function(n, encoded_text, r)) > how_fit:
                syph = r
                how_fit = w


def generate_population():
    considered = set()
    population = list()
    count = 0
    psize = 67579678576855976756565865685*0
    while not POPULATION_SIZE <= psize:
        cipher = shuffle(string.ascii_uppercase)

        if cipher not in considered:
            considered.add(cipher)
            population.append(cipher)
            count += 1

    return population


def score_generation(generation, n, encoded_text):
    return {cipher: fitness_function(n, encoded_text, cipher) for cipher in generation}


def select_parent(tournament):
    for cipher in tournament:
        if random.random() < TOURNAMENT_WIN_PROBABILITY:
            return cipher

    return None


def fill_child(child, parent2):
    child_set = set(child)

    for i, letter in enumerate(parent2):
        if letter not in child_set:
            child_set.add(letter)

            for j in range(len(child)):
                if child[j] == "":
                    child[j] = letter
                    break

    return child

def breed(parents):
    crossover_count = 0
    index = random.randint(0, 1)
    parent1, parent2 = parents[index], parents[1 - index]
    child = [""] * len(parent1)

    while crossover_count < CROSSOVER_LOCATIONS:
        random_index = random.randint(0, len(child) - 1)

        if child[random_index] == "":
            child[random_index] = parent1[random_index]
            crossover_count += 1

    child = "".join(fill_child(child, parent2))

    if random.random() < MUTATION_RATE:
        child = random_swap(child)

    return "".join(fill_child(child, parent2))


def selection(current_generation, n, encoded_text):
    scored_generation = score_generation(current_generation, n, encoded_text)
    ranked_generation = sorted(current_generation, key=lambda cipher: -scored_generation[cipher])
    next_generation = ranked_generation[:NUM_CLONES]

    print(code(encoded_text, sypher(string.ascii_uppercase, ranked_generation[0])))

    while len(next_generation) < POPULATION_SIZE:
        distinct_ciphers = random.sample(ranked_generation, 2 * TOURNAMENT_SIZE)
        tournaments = distinct_ciphers[:len(distinct_ciphers) // 2], distinct_ciphers[len(distinct_ciphers) // 2:]
        tournaments = sorted(tournaments[0], key=lambda cipher: -scored_generation[cipher]), \
                      sorted(tournaments[1], key=lambda cipher: -scored_generation[cipher])

        parents = select_parent(tournaments[0]), select_parent(tournaments[1])
        next_generation.append(breed(parents))

    return next_generation
def genetic_algorithm(n, encoded_text):
    population = generate_population()
    count = 0

    while count < 500:
        print("Generation:", count)
        population = selection(population, n, encoded_text)

        count += 1


encoded_text = """ZRTGO Y JPEYPGZA, RP'J IKPGO HIJJRMWG PI RSHEITG PUG JPEYPGZA MA SYDROZ EYOBIS XUYOZGJ, PGJPROZ PUG
EGJLWP IK PUIJG XUYOZGJ, YOB DGGHROZ IOWA PUG MGPPGE ILPXISGJ. PURJ RJ XYWWGB URWW XWRSMROZ. PURJ RJ
EGWYPRTGWA JRSHWG PI XIBG, MLP BIGJO'P CIED RO GTGEA JRPLYPRIO - RP XYO IKPGO ZGP XYLZUP RO Y WIXYW
SYFRSLS, Y JPEYPGZA PUYP RJ OIP RBGYW MLP KEIS CURXU YOA JROZWG XUYOZG RJ OIP YO RSHEITGSGOP IO RPJ ICO.
ZGOGPRX YWZIERPUSJ YEG Y HICGEKLW PIIW KIE RSHEITROZ IO PUG RBGY IK URWW XWRSMROZ PI IHPRSRVG Y JIWLPRIO
RO JRPLYPRIOJ CUGEG YWW IK PUG KIWWICROZ YEG PELG: Y JPEYPGZA XYO MG HEGXRJGWA QLYOPRKRGB MA Y JHGXRKRX
JGP IK TYERYMWGJ ZRTGO XGEPYRO OLSGERX TYWLGJ. PUG ILPXISG IK PUG JPEYPGZA XYO YWJI MG HEGXRJGWA
QLYOPRKRGB. PUGEG YEG ROPGEYXPRIOJ MGPCGGO PUG TYERYMWGJ PUYP SYDG JRSHWG URWW XWRSMROZ ROGKKRXRGOP IE
LOWRDGWA PI JLXXGGB."""
# """ZRTGO Y JPEYPGZA, RP'J IKPGO HIJJRMWG PI RSHEITG PUG JPEYPGZA MA SYDROZ EYOBIS XUYOZGJ, PGJPROZ PUG
# EGJLWP IK PUIJG XUYOZGJ, YOB DGGHROZ IOWA PUG MGPPGE ILPXISGJ. PURJ RJ XYWWGB URWW XWRSMROZ. PURJ RJ
# EGWYPRTGWA JRSHWG PI XIBG, MLP BIGJO'P CIED RO GTGEA JRPLYPRIO - RP XYO IKPGO ZGP XYLZUP RO Y WIXYW
# SYFRSLS, Y JPEYPGZA PUYP RJ OIP RBGYW MLP KEIS CURXU YOA JROZWG XUYOZG RJ OIP YO RSHEITGSGOP IO RPJ ICO.
# ZGOGPRX YWZIERPUSJ YEG Y HICGEKLW PIIW KIE RSHEITROZ IO PUG RBGY IK URWW XWRSMROZ PI IHPRSRVG Y JIWLPRIO
# RO JRPLYPRIOJ CUGEG YWW IK PUG KIWWICROZ YEG PELG: Y JPEYPGZA XYO MG HEGXRJGWA QLYOPRKRGB MA Y JHGXRKRX
# JGP IK TYERYMWGJ ZRTGO XGEPYRO OLSGERX TYWLGJ. PUG ILPXISG IK PUG JPEYPGZA XYO YWJI MG HEGXRJGWA
# QLYOPRKRGB. PUGEG YEG ROPGEYXPRIOJ MGPCGGO PUG TYERYMWGJ PUYP SYDG JRSHWG URWW XWRSMROZ ROGKKRXRGOP IE
# LOWRDGWA PI JLXXGGB."""
# encoded_text = "Lm Uirwzb, hsziv z nzmtl ozhhr drgs gsv Xsf"
ngrams_dict = build_ngrams_dict("ngrams.txt")
genetic_algorithm(3, encoded_text)
