#Maisa Ahmad
#June 27, 2018
#This program summarizes images, like koalastothemax.

import numpy as np
import matplotlib.pyplot as plt

def average(region):
     red, green, blue = 0,0,0  #<-- placeholder, can remove once defined.
     red = region[:,:,0].mean()
     green = region[:,:,1].mean()
     blue = region[:,:,2].mean()
    
     return(red,green,blue)

def setRegion(region, r,g,b):
    region[:,:,0] = r
    region[:,:,1] = g
    region[:,:,2] = b


def quarter(img2, levels):
     h = img2.shape[0]
     w = img2.shape[1]
     hReg = h//2**levels
     wReg = w//2**levels
     for i in range(2**levels):
          for j in range(2**levels):              
               #Average the region:
               r,g,b = average(img2[i*hReg:(i+1)*hReg,j*wReg:(j+1)*wReg])
               setRegion(img2[i*hReg:(i+1)*hReg,j*wReg:(j+1)*wReg],r,g,b)


def main():
     inFile = input('Enter image file name: ')
     img = plt.imread(inFile)

     #Divides the image in 1/2, 1/4, 1/8, ... 1/2^8, and displays each:
     for i in range(8):
          img2 = img.copy()   #Make a copy to average
          quarter(img2,i)     #Split in half i times, and average regions
     
          plt.imshow(img2)    #Load our new image into pyplot
          plt.show()          #Show the image (waits until closed to continue)

     #Shows the original image:
     plt.imshow(img)	      #Load image into pyplot
     plt.show()               #Show the image (waits until closed to continue)


#Allow script to be run directly:
if __name__ == "__main__":
     main()
