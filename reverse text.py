#Maisa Ahmad
#June 6, 2018
#This program prompts user for a message and prints the message in reverse order.

text = input("Enter a message:")
index = -1
while index < len(text):
    y = text[index]
    print(y)
    index = index - 1

