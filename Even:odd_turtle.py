#Maisa Ahmad
#June 14, 2018
#This program prompts users for a whole number and determines if it's even or odd.

import turtle
maisa = turtle.Turtle()

x = int(input("Enter a number:"))

if x % 2 == 0:
        maisa.color("blue")
        maisa.backward(100)
else:
        maisa.color("red")
        maisa.forward(100)
