#Maisa Ahmad
#June 6, 2018
#This program prompts user for an image and produces the image through a green channel.

import matplotlib.pyplot as plt
import numpy as np
pic = input("Enter name of the input file:")

img = plt.imread(pic)
plt.imshow(img)
#plt.show()

img2 = img.copy()

img2[:,:,0] = 0
img2[:,:,2] = 0

plt.imshow(img2)
#plt.show()

out = input("Enter the name of the output file:")

plt.imsave(out,img2)


