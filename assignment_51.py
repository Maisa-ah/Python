#Maisa Ahmad
#July 2, 2018
#This program prompts for a string until user enters an non-empty string.

x = input("Enter a non-empty string: ")
while x == "":
    print("That was empty. Try again.")
    x = input("Enter a non-empty string: ")
print(x)
