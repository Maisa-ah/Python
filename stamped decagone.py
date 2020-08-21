#Maisa Ahmad
#May 31, 2018
#This program draws a purple decagon with turtle stamped at each corner.

import turtle

maisa = turtle.Turtle()
maisa.color("purple")
maisa.shape("turtle")

for i in range(10):
    maisa.forward(100)
    maisa.stamp()
    maisa.left(36)
