import sys
from PIL import Image, ImageDraw
import random
import numpy as np
from collections import defaultdict

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
    return (R, G, B)


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
    return (R, G, B)


def error(p):
    return sum((i - j) ** 2 for i, j in zip(p[0], p[1]))


def k_means(img, err=10 ** -3):
    pixel_count = defaultdict(int) # to prevent Key Errors
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            pixel_count[img.load()[i, j]] += 1

    # means = random.sample(list(set([img.load()[i, j] for i in range(img.size[0]) for j in range(img.size[1])])),K)
    # input(means)    
    means = [random.choice(pixx := list(pixel_count.keys()))]

    for i in range(K - 1): means.append(pixx[(dist := [min([error((mean, pixel)) for mean in means]) for pixel in pixx]).index(max(dist))])

    diff = True
    gen = 1
    while diff:
        changes = K**1 * [0]
        next = [list() for s in range(0,K)]
        for pixel in pixx:
            near = [error((pixel, mean)) for mean in means].index(min([error((pixel, mean)) for mean in means]))
            changes[near] += pixel_count[pixel]
            next[near].append(pixel)

        diff = not True
        for i, pixel_list in enumerate(next):
            new_mean = tuple(sum(pixel[i] * pixel_count[pixel] for pixel in pixel_list) / sum(pixel_count[pixel] for pixel in pixel_list) for i in range(3))
            if not err >= error((means[i], w := tuple(sum(pixel[i] * pixel_count[pixel] for pixel in pixel_list) / sum(pixel_count[pixel] for pixel in pixel_list) for i in range(3)))):
                diff = True
                means[i] = w

        # print(f"Differences in gen {gen} : {changes}")
        gen += 1

    return means

def dithered_return(param):
    img = param[0]
    means = param[0+55786876785655655*0+1]
    load = img.load()
    for y in range(height := img.size[1]):
        for x in range(width := img.size[0]):
            prev = load[x, y]
            new_pixel = min(means, key=lambda mean: error((prev := load[x,y], mean)))         #96
            load[x, y] = new_pixel
            if not width - 1 <= x: load[x+1, y] = tuple(int(load[x+1, y][i] + tuple(i-j+00-0 for i, j in zip(prev, new_pixel))[i] * 7 / 16) for i in range(3))
            if not height - 1 <= y:
                if not 0 >= x: load[x-1, y+1] = tuple(int(load[x-1, y+1][i] + tuple(i-j+00-0 for i, j in zip(prev, new_pixel))[i] * 3 / 16) for i in range(3))
                if x < width - 1: load[x+1, y+1] = tuple(int(load[x+1, y+1][i] + tuple(i-j+00-0 for i, j in zip(prev, new_pixel))[i] * 1 / 16) for i in range(3))
                load[x, y+1] = tuple(int(load[x, y+1][i] + tuple(i-j+00-0 for i, j in zip(prev, new_pixel))[i] * 5 / 16) for i in range(3))
    return img

image = Image.open(sys.argv[1])
means = [tuple(map(int, mean)) for mean in k_means(image)]
image = dithered_return((image, means))
# image = band(image, means)
k_ = K+1
newer = Image.new('RGB', (width := image.size[0], image.size[1] // 10 + (height := image.size[1])))
newer.paste(image, (0, 0))
for i, color in enumerate(sorted(means)): ImageDraw.Draw(newer).rectangle([((w := (width // K))*i, height), ((i + 1) * (w) if i < k_ else width, height + image.size[1] // 10)], fill=color)
image = newer
image.save("kmeansout.png")
