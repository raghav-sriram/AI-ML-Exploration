import pickle

for i in range (5):
    with open("pickle_w.txt", "rb") as f:
        pickled = pickle.load(f)
    print("Weights",pickled)

for i in range (5):
    with open("pickle_b.txt", "rb") as f:
        pickled = pickle.load(f)
    print("Biass", pickled)