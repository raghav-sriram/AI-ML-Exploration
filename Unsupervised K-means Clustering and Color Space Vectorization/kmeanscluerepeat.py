# Raghav Sriram
# Tuesday 3/28/2023
# Unit 7 Unsupervised Machine Learning
# K-Means Color Space Vector Quant

from PIL import Image
import random
from math import log, sqrt

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


img = Image.open("puppy.jpg") # Just put the local filename in quotes.
# img.show() # Send the image to your OS to be displayed as a temporary file
print(img.size) # A tuple. Note: width first THEN height. PIL goes [x, y] with y counting from the top of the frame.
pix = img.load() # Pix is a pixel manipulation object; we can assign pixel values and img will change as we do so.
# print(pix[2,5]) # Access the color at a specific location; note [x, y] NOT [row, column].
# pix[2,5] = (255, 255, 255) # Set the pixel to white. Note this is called on “pix”, but it modifies “img”.
# pix = [color_naive_27(pix[i][j]) for i in range(img.size[0]) for j in range(img.size[1])] 
# for i in range(img.size[0]):
#     for j in range(img.size[1]):
#             pix[i,j] = color_naive_8(pix[i,j]) #color_naive_27 

# _ = [(pix.__setitem__((i, j), color_naive_8(pix[i, j])), None) for i in range(img.size[0]) for j in range(img.size[1])]

# img.show() # Now, you should see a single white pixel near the upper left corner
# img.save("my_image.png") # Save the resulting image. Alter your filename as necessary.



def K_Means(image,k):
    K = k # step 1
    pixels = image.load()
    
    pixies = list() 
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            pixies.append(pixels[i, j])
    
    means = random.sample(pixies, K)

    input(means)
    stable_means = None
    m = dict()
    # print(means)
    # input()
    ustable = True
    m = {x: [] for x in means}
    # means = stable_means
    for x in pixies: # step 3
        m_d = float("inf")
        stable_means = None
        for y in means:
            d = dist(x,y)

            if d < m_d:
                m_d = d
                c_s = y
                # x = y # try a dictionary and mapping x to y like {x: y}
        m[c_s].append(x)
    means = []
    # print(mapping)
    # input()
    for y in m.values(): #find the average star data for each of the means star types
        # print(y)
        means.append(average(y)) # step 4
    
    # print(means)
    # print(stable_means)
    # input()

    counter = 0
    while ustable: # step 5
        counter += 1
        mapping = {x: [] for x in means}
        # means = stable_means
        # mapping = {means[i] : [] for i in range(K)}
        for x in pixies: # step 3
            min_dist = float("inf")
            closest_mean = None
            for y in means:
                distance = dist(x,y)

                if distance < min_dist:
                    min_dist = distance
                    closest_mean = y
                    # x = y # try a dictionary and mapping x to y like {x: y}
            mapping[closest_mean].append(x)
        stable_means = []
        # print(mapping)
        # input()
        for y in mapping.values(): #find the average star data for each of the means star types
            # print(y)
            stable_means.append(average(y)) # step 4
        
        # print(means)
        # print(stable_means)
        # input()

        if stable_means == means:
            m = mapping
            # break
            ustable = False # step 6
            break
            # input("means")
        else:
            means = stable_means
            m = mapping
        # temp = stable_means
        # stable_means = None
        # means = temp
        # input()
        print(counter)
    # input(counter)
    return m
                                                


def dist(x,y):
    return sqrt( sum([(x[i]-y[i])**2 for i in range(len(x))]) )

def average(star_vectors):
    a1 = [x[0] for x in star_vectors]
    a2 = [x[1] for x in star_vectors]
    a3 = [x[2] for x in star_vectors]

    # a1 = sum([x[0] for x in star_vectors])/len(star_vectors)
    # a2 = sum([x[1] for x in star_vectors])/len(star_vectors)
    # a3 = sum([x[2] for x in star_vectors])/len(star_vectors)
    return (sum(a1)/len(a1),sum(a2)/len(a2),sum(a3)/len(a3))


spectral = K_Means(img,2)

for x in spectral:
    for y in spectral[x]:

        for i in range(img.size[0]):
            for j in range(img.size[1]):
                if pix[i,j] == y:
                    index1,index2 = i,j
                    # print(index1,index2)
        # print(y)
        # print(x)
        # print(pix[index1,index2])
        pix[index1,index2] = (int(x[0]),int(x[1]),int(x[2]))

img.show()
img.save("kmeansout.png")