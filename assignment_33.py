#Maisa Ahmad
#June 20, 2018
#This program prompts user for a list of nouns and approximates the fraction that are plural.

nouns = input("Enter nouns:")
#words = int(input("Number of words:"))
list=nouns.split(" ")
length = len(list)
print("Number of words", length)

count = 0
for nouns in list:
    if nouns[-1]=="s":
        count = count+1
        
fraction = count/length
print("Fraction of your list that is plural is", fraction)
        
