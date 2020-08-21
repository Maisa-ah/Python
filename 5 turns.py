#Maisa Ahmad
#June 11, 2018
#This program asks the user for 5 whole numbers and the turtle will turn with the degrees entered.

import turtle
maisa = turtle.Turtle()

for i in range(5):
    x=int(input("Enter a number:"))
    maisa.forward(100)
    maisa.left(x)

