import numpy as np
import sys
import random
import pickle
import matplotlib.pyplot as plt
from scipy.ndimage import shift, rotate

# DEMO

# This is just for demonstration, in the actual lab you will replace the image with the image of the misclassified points
# Creating a random grayscale image
random_image = np.random.random([100, 100])

# Creating a new figure
plt.figure()

plt.show() # Displays the figure

plt.close() # Closes the figure

# Setting the title of the figure
plt.title("Random Grayscale Image")

plt.show() # Displays the figure
plt.pause(interval=2)  # pausing for n seconds
plt.close() # Closes the figure

# Displaying the image with a grayscale colormap
plt.imshow(random_image, cmap='gray')

# Displaying the figure
plt.show()

# Pausing for a while for you to see the image
plt.pause(interval=2)  # pausing for n seconds

# Closing the figure
plt.close()
