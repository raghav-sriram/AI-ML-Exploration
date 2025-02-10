import sys
from PIL import Image
import random

K = int(sys.argv[2])


def color_naive_27(pixel):
    if pixel[0] < 255 // 3:
        R = 0
    elif pixel[0] > 255 * 2 // 3:
        R = 255
    else:
        R = 127
        
    if pixel[1] < 255 // 3:
        G = 0
    elif pixel[1] > 255 * 2 // 3:
        G = 255
    else:
        G = 127
    
    if pixel[2] < 255 // 3:
        B = 0
    elif pixel[2] > 255 * 2 // 3:
        B = 255
    else:
        B = 127
    return (R,G,B)

def color_naive_8(pixel):
    if pixel[0] < 128:
        R = 0
    else:
        R = 255
        
    if pixel[1] < 128:
        G = 0
    else:
        G = 255

    if pixel[2] < 128:
        B = 0
    else:
        B = 255
    return (R,G,B)

def error(p):
    return sum((i-j) ** 2 for i, j in zip(p[0], p[1]))

def k_means(img, err=10 ** -3):
    result = list()
    for v in range(K):
        result.append(list())
    clusters = list(result)
    means = [random.choice(pixx := list(set([img.load()[i, j] for i in range(img.size[0]) for j in range(img.size[1])])))]
    
    


    for i in range(K - 1): means.append(pixx[(dist := [min([error((mean, pixel)) for mean in means]) for pixel in pixx]).index(max(dist))])

    diff = True
    while True == diff:
        
        for pixel in pixx: clusters[[error((pixel, mean)) for mean in means].index(min([error((pixel, mean)) for mean in means]))].append(pixel)
        diff = False
        for i, pixel_list in enumerate(clusters):
            if not err >= error((means[i], w := tuple(sum(pixel[i] for pixel in pixel_list) / len(pixel_list) for i in range(3)))):  diff = True
            means[i] = w
        if diff == True: 
            res = list()
            for v in range(K):
                res.append(list())
            clusters = list(res)

    return means
 

    
    
img = Image.open(sys.argv[1])
# pix = img.load()
# for i in range(img.size[0]):
#     for j in range(img.size[1]):
#         pix[i,j] = color_naive_8(pix[i,j]) #color_naive_27 

# img.save("lion8means.png") # Save the resulting image. Alter your filename as necessary.      #96

means = [tuple(map(int, mean)) for mean in k_means(img)]
pixels = img.load()
for i in range(img.size[0]):
    for j in range(img.size[1]):
        pixels[i, j] = min(means, key=lambda mean: error((pixels[i,j], mean)))
img.save("kmeansout.png")




