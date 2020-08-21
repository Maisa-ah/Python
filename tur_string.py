#Maisa Ahmad
#June 13, 2018
#This program takes a string input and uses that string to control what the turtle draws on the screen.

import turtle

maisa = turtle.Turtle()
myWin = turtle.Screen()
commands = input("Please enter a command string:")

for ch in commands:
    if ch =="F":
        maisa.forward(50)
    elif ch == "L":
        maisa.left(90)
    elif ch == "R":
        maisa.right(90)
    elif ch == "^":
        maisa.penup()
    elif ch == "v":
        maisa.pendown()
    elif ch == "B":
        maisa.backward(50)
    elif ch == "S":
        maisa.stamp()
    elif ch == "l":
        maisa.left(45)
    elif ch == "r":
        maisa.right(45)
    elif ch == "p":
        maisa.color("purple")
    else:
        print("Error: do not know the command:",c)
