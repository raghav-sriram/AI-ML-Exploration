import numpy as np
import sys
import math

def sigmoid(x):
    return 1 / (1 + np.power(math.e, -x))

def sigmoid_(x):
    return sigmoid(x) * (1 - sigmoid(x))

def forward_propagation(weightings, biases, a, inner_product, x):
    a[0] = x
    for l in range(1, len(weightings)):
        inner_product[l] = (a[l-1] @ weightings[l]) + biases[l]
        a[l] = np.vectorize(sigmoid)(inner_product[l])
    return a, inner_product

def backward_propagation(weightings, a, inner_product, deltar, y):
    N = len(weightings) - 1
    deltar[N] = np.multiply(np.vectorize(sigmoid_)(inner_product[N]),(y-a[N]))
    for lair in range(N-1,0,-1): deltar[lair] = np.multiply(sigmoid_(inner_product[lair]), deltar[lair+1] @ np.transpose(weightings[lair+1]))
    return deltar

def update_weights_biases(weightings, biases, a, deltar, lambdarate):
    for i in range(1, len(weightings)):
        weightings[i] = weightings[i] + np.matmul(lambdarate * np.transpose(a[i-1]) , deltar[i])
        biases[i] = biases[i] + lambdarate * deltar[i]
    return weightings, biases

def count_misclassified(weightings, biases, datar):
    misclassified = 0
    for x in datar:
        if not np.array_equal(np.round(p_net(sigmoid, weightings, biases, x[0])), x[1]):
            misclassified += 1
    return misclassified

def print_epoch_info(epoch, misclassified, datar):
    print(f"Epoch Number: {epoch}, Misclassified points: {misclassified}/{len(datar)}")


def p_net(A, weightings, biases, x):
    
    a = [None] * (len(weightings))
    a[0] = x
    N = len(weightings) - 1
    for i in range (1,N+1):
        a[i] = np.vectorize(A)((a[i-1] @ weightings[i])+ biases[i])
    return a[N]

def print_final_accuracy(misclassified, datar, epochs):
    accuracy = (len(datar)-misclassified)/len(datar)
    print(f"Epoch: {epochs-1}, Accuracy: {accuracy*100}%")
    print(f"Correctly Classified: {len(datar)-misclassified} out of {len(datar)}")
    print(f"Misclassified: {misclassified} out of {len(datar)}")

def trainee(datar,lambdarate,max,print_=False,architecture = [2,2,1]):   
    weightings, biases = [None], [None]
    for i in range(len(architecture) - 1):
        weightings.append(np.random.uniform(-1, 1, (architecture[i], architecture[i + 1])))
        biases.append(np.random.uniform(-1, 1, (1, architecture[i + 1])))
        
    
    N = len(weightings)-1
    a = (1+N) * [np.array([])]
    inner_product, deltar = (1+N) * [np.array([])], (1+N) * [np.array([])]
    for epoch in range(max):
        for x, y in datar:
            a, inner_product = forward_propagation(weightings, biases, a, inner_product, x)
            deltar = backward_propagation(weightings, a, inner_product, deltar, y)
            weightings, biases = update_weights_biases(weightings, biases, a, deltar, lambdarate)
        if print_ == True:
            counter = count_misclassified(weightings, biases, datar)
            print_epoch_info(epoch, counter, datar)
            if epoch == max-1:
                print_final_accuracy(counter, datar, max)
    return weightings,biases

if (sys.argv[1] == "S"):
    weightings,biases = trainee(dayta := [(np.array([[0,0]]), np.array([[0,0]])), (np.array([[0,1]]), np.array([[0,1]])), (np.array([[1,0]]), np.array([[0,1]])), (np.array([[1,1]]), np.array([[1,0]]))],0.7,10000, False,[2,2,2])

    for x in dayta: 
        print(f"Output ({x[1][0][0]},{x[1][0][1]}) {np.array([[(w:=p_net(sigmoid, weightings, biases,x[0]))[0][0]],[w[0][1]]])}")

if (sys.argv[1] == "C"): 
    weightings,biases = trainee([(np.array([[rand1 := np.random.uniform(-1, 1), rand2 := np.random.uniform(-1, 1)]]), np.array([[int((rand1**2 + rand2**2)**0.5 < 1)]]) ) for _ in range(10000)],0.1,200,True, [2,4,1])














