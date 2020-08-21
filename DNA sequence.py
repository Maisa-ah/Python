#Maisa Ahmad
#June 4, 2018
#This program prints the length and GC-content of the DNA string.

insulin = input("Enter a DNA string")
l=len(insulin)
print("The length is", l)

numC = insulin.count("C")
numG = insulin.count("G")
print("Number of C nucleotides", numC)
print("Number of G nucleotides", numG)

gc = (numC + numG) / l
gcPercent = gc * 100
print("GC-content is", gcPercent)
