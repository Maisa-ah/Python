#Maisa Ahmad
#June 6, 2018
#This program demonstrates the shades of green.

import turtle

turtle.colormode(255)
maisa = turtle.Turtle()
maisa.shape("turtle")
maisa.backward(100)

for i in range(0,255,10):
    maisa.forward(10)
    maisa.pensize(i)
    maisa.color(0,i,0)
