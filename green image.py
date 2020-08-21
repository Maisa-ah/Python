#Maisa Ahmad
#June 6, 2018
#This program prompts user for an image and produces the image through a green channel.

import matplotlib.pyplot as plt
import numpy as np
pic = 

img = plt.imread

plt.imshow(img)
plt.show(img)

img2 = img.copy()

img[:,:,0] = 0
img2[:,:,2] = 0

plt.imshow(img2)
plt.show()

plt.imsave("img2.png")


