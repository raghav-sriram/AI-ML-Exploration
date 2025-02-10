import random
import sys
import colorsys
import numpy as np
from PIL import Image
from math import inf
from itertools import product

k = int(sys.argv[2])


def get_naive_palette():
    colors = []

    if k == 8:
        colors = [0, 255]
    elif k == 27:
        colors = [0, 127, 255]

    return [elem for elem in product(colors, repeat=3)]


def find_closest_palette_color(color, type):
    if type == 27:
        if color < 255 // 3:
            return 0
        elif color > 255 * 2 // 3:
            return 255
        else:
            return 127
    elif type == 8:
        return 0 if color < 128 else 255

    return -1


def vectorize_img(img, type):
    pixels = img.load()

    for i in range(0, img.size[0]):
        for j in range(0, img.size[1]):
            pix = list(pixels[i, j])

            for k, color in enumerate(pix):
                pix[k] = find_closest_palette_color(color, type)

            pixels[i, j] = tuple(pix)


def pixels_to_list(pixels, img_size):
    pixel_list = []

    for i in range(0, img_size[0]):
        for j in range(0, img_size[1]):
            pixel_list.append(pixels[i, j])

    return pixel_list


def get_rgb_map(pixels, img_size):
    rgb_map = {}

    for i in range(0, img_size[0]):
        for j in range(0, img_size[1]):
            rgb_map[pixels[i, j]] = rgb_map[pixels[i, j]] + 1 if pixels[i, j] in rgb_map else 1

    return rgb_map


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
    print(len(pixels))

    for _ in range(k - 1):
        distances = []

        for i, pixel in enumerate(pixels):
            curr_dist = inf

            for j, mean in enumerate(means):
                curr_dist = min(curr_dist, get_squared_error(mean, pixel))

            distances.append(curr_dist)

        means.append(pixels[np.argmax(distances)])

    return means


def k_means(img, err=10 ** -3):
    pixels = list(get_rgb_map(img.load(), img.size).keys())
    means = initialize_means(pixels)
    pixel_lists = tuple([] for _ in range(k))
    changed = True

    while changed:
        changed = False

        for pixel in pixels:
            index = get_closest_mean_index(pixel, means)
            pixel_lists[index].append(pixel)

        for i, star_list in enumerate(pixel_lists):
            new_mean = get_new_mean(star_list)

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


def add_color_band(img, means):
    pixels = img.load()
    rect_size = img.size[0] // k

    print(img.size)

    for i, mean in enumerate(means):
        for j in range(i * rect_size, i * rect_size + rect_size):
            for l in range(1, rect_size + 1):
                pixels[j, img.size[1] - l] = mean


def dither_img(img, means=None):
    pixels = img.load()

    for j in range(0, img.size[1] - 1):
        for i in range(0, img.size[0] - 1):
            pixel = pixels[i, j] + tuple()
            closest_mean = (find_closest_palette_color(pixel[0], k),
                            find_closest_palette_color(pixel[1], k),
                            find_closest_palette_color(pixel[2], k)) if means is None else means[
                get_closest_mean_index(pixel, means)]
            pixels[i, j] = closest_mean
            quant_error = tuple(np.subtract(pixel, closest_mean))
            pixels[i + 1, j] = tuple(np.add(pixels[i + 1, j], tuple(round(c) for c in np.multiply(quant_error, 7 / 16))))
            pixels[i - 1, j + 1] = tuple(
                np.add(pixels[i - 1, j + 1], tuple(round(c) for c in np.multiply(quant_error, 3 / 16))))
            pixels[i, j + 1] = tuple(np.add(pixels[i, j + 1], tuple(round(c) for c in np.multiply(quant_error, 5 / 16))))
            pixels[i + 1, j + 1] = tuple(
                np.add(pixels[i + 1, j + 1], tuple(round(c) for c in np.multiply(quant_error, 1 / 16))))


def rainbow_order(colors):
    hls_colors = [colorsys.rgb_to_hls(color[0]/255.0, color[1]/255.0, color[2]/255.0) for color in colors]
    hls_colors.sort()
    return [colorsys.hls_to_rgb(hls_color[0], hls_color[1], hls_color[2]) for hls_color in hls_colors]


# Expect the image file path and the number of clusters as command line arguments
URL = sys.argv[1]
img = Image.open(URL)

means = [tuple(int(color) for color in mean) for mean in k_means(img)]
means = rainbow_order(means)
dither_img(img, means)
add_color_band(img, means)
img.save("kmeansout.png")
