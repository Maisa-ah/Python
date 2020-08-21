#Maisa Ahmad
#June 11, 2018
#This program prints binary to decimal.

base = input("Enter a digit:")
decNum = 0

for c in base:
    n = int(c)
    decNum = 2*decNum + n
print(decNum)
