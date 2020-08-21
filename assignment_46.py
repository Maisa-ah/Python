#Maisa Ahmad
#July 2, 2018
#This program makes a turtle walk 100 times.

import turtle
import random

maisa = turtle.Turtle()
maisa.speed(10)

for i in range(100):
  maisa.forward(10)
  a = random.randrange(0,360,1)
  maisa.right(a)
