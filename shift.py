#Maisa Ahmad
#June 4, 2018
#This program prompts the user to enter a word and prints out the word shifted right by 2 letters.

word = input("Enter a word")
coded = ""
for ch in word:
    offset = ord(ch) - ord('a') + 2
    wrap = offset % 26 
    newchar = chr(ord('a') + wrap)
    coded = coded + newchar
    
    
print("The coded word is", coded)

