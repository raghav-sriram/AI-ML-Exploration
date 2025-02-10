import sys
from math import inf
from PIL import Image
import random

k = int(sys.argv[2])

def get_squared_error(pixel_a, pixel_b):
    error = 0
    for i in range(len(pixel_a)):
        error += (pixel_a[i] - pixel_b[i]) ** 2
    return error

def get_closest_mean_index(pixel, means):
    min_index = -1
    min_error = inf
    for i, mean in enumerate(means):
        error = get_squared_error(pixel, mean)
        if error < min_error:
            min_index = i
            min_error = error
    return min_index

def get_new_mean(pixel_list):
    mean = [0, 0, 0]
    for pixel in pixel_list:
        for i, color in enumerate(pixel):
            mean[i] += color
    for i in range(len(mean)):
        mean[i] /= len(pixel_list)
    return tuple(mean)

def initialize_means(pixels):
    means = random.sample(pixels, 1)
    for _ in range(k - 1):
        distances = []
        for pixel in pixels:
            curr_dist = inf
            for mean in means:
                curr_dist = min(curr_dist, get_squared_error(mean, pixel))
            distances.append(curr_dist)
        means.append(pixels[distances.index(max(distances))])
    return means

def k_means(img, err=10 ** -3):
    pixels = list(set([img.load()[i, j] for i in range(img.size[0]) for j in range(img.size[1])]))
    means = initialize_means(pixels)
    pixel_lists = tuple([] for _ in range(k))
    changed = True

    while changed:
        changed = False
        for pixel in pixels:
            index = get_closest_mean_index(pixel, means)
            pixel_lists[index].append(pixel)
        for i, pixel_list in enumerate(pixel_lists):
            new_mean = get_new_mean(pixel_list)
            if get_squared_error(means[i], new_mean) > err:
                changed = True
            means[i] = new_mean
        if changed:
            pixel_lists = tuple([] for _ in range(k))

    return means

def vectorize_img_with_means(img, means):
    pixels = img.load()
    for i in range(0, img.size[0]):
        for j in range(0, img.size[1]):
            pixels[i, j] = means[get_closest_mean_index(pixels[i, j], means)]
    return img

if __name__ == "__main__":
    # File should be a local file name, provided as an argument.
    img = Image.open(sys.argv[1])
    means = [tuple(int(color) for color in mean) for mean in k_means(img)]
    img = vectorize_img_with_means(img, means)
    img.save("kmeansout.png")
