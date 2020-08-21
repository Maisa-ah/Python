#Maisa Ahmad
#June 20, 2018
#This program prompts user for the name of image, output name and saves lower left quarter of the image.

import matplotlib.pyplot as plt
import numpy as np

img = plt.imread(input("Enter image file name:"))
height = img.shape[0]
width = img.shape[1]
img2=img[height//2:,:width//2]

plt.imshow(img2)
plt.show()

plt.imsave(input("Enter output name"),img2)

