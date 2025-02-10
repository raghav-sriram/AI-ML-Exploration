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
    pixels = list(set([img.load()[i, j] for i in range(img.size[0]) for j in range(img.size[1])]))
    means = [random.choice(pixels)]
    clusters = [[] for _ in range(K)]

    for _ in range(K - 1):
        dist = [min([error((mean, pixel)) for mean in means]) for pixel in pixels]
        means.append(pixels[dist.index(max(dist))])

    changed = True
    while changed:
        changed = False
        for pixel in pixels:
            idx = [error((pixel, mean)) for mean in means].index(min([error((pixel, mean)) for mean in means]))
            clusters[idx].append(pixel)
        for i, pixel_list in enumerate(clusters):
            new_mean = (sum(pixel[i] for pixel in pixel_list) / len(pixel_list) for i in range(3))
            if not err >= error((means[i], w := tuple(new_mean))): 
                changed = True
            means[i] = w
        if changed: 
            clusters = [[] for _ in range(K)]

    return means

if __name__ == "__main__":
    
    
    
    img = Image.open(sys.argv[1])
    pix = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            pix[i,j] = color_naive_8(pix[i,j]) #color_naive_27 

    img.save("kmeansout.png") # Save the resulting image. Alter your filename as necessary.

    # means = [tuple(map(int, mean)) for mean in k_means(img)]
    # pixels = img.load()
    # for i in range(img.size[0]):
    #     for j in range(img.size[1]):
    #         pixels[i, j] = min(means, key=lambda mean: error((pixels[i,j], mean)))
    # img.save("kmeansout.png")
