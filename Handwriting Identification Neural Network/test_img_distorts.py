import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import shift, rotate

def net(tect):
    w, b = [None], [None]

    for i in range(len(tect) - 1):
        x = tect[i]
        y = tect[i + 1] # current element, next element
        w.append(np.random.uniform(-1,1, (x, y))) #appended to the weight matrix
        b.append(np.random.uniform(-1,1, (1, y))) #appended to the bias matrix

    return w, b

def algorithm(training_set,epochs=100,distort = False):
      
    for epoch in range(epochs):
        for x in training_set:
            
            if distort:
                x = which_jitter(x)

mist = list()

def which_jitter(img):
    ops = ["normal", "up", "left", "down", "right", "rotate_right", "rotate_left"]
    opps = np.random.choice(ops)

    re_img = img[0].reshape(28,28)

    matrix_transformations = {
        "up": np.roll(re_img, -1, axis=0),
        "left": np.roll(re_img, -1, axis=1),
        "down": np.roll(re_img, 1, axis=0),
        "right": np.roll(re_img, 1, axis=1),
        "rotate_right": rotate(re_img, -15),
        "rotate_left": rotate(re_img, 15),
        "normal": re_img
    }

    plt.figure()
    plt.title("normal")
    plt.imshow(re_img,cmap="gray")

    re_img = matrix_transformations[opps]

    # Display each transformation
    # plt.figure()
    # plt.title(opps)
    # plt.imshow(matrix_transformations[opps], cmap="gray")
    
    plt.figure()
    plt.title(f"{opps}")
    plt.imshow(re_img,cmap="gray")

    plt.show()

    return (re_img.reshape(1,-1),img[1])

with open("mnist_train.csv") as f:
    # MNIST datastructure
    for line in f:
        l = line.strip().split(",")
        mist.append((np.array([[int(i) / 255 for i in l[1:]]]),
                              np.array([[0]*int(l[0]) + [1] + [0] * (10 - int(l[0]) - 1)]))) # 0 gives the number of the handwritten letter

mest = list()
with open("mnist_test.csv") as f:
    # MNIST datastructure
    for line in f:
        l = line.strip().split(",")
        mest.append((np.array([[int(i) / 255 for i in l[1:]]]),
                              np.array([[0]*int(l[0]) + [1] + [0] * (10 - int(l[0]) - 1)]))) # 0 gives the number of the handwritten letter    

    # print((mist[0]))
    # mist should have a None in the front
w,b = net([784,300,10]) # architecture
w,b = algorithm(mist,7,distort=True)