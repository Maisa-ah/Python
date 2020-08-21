#Maisa Ahmad
#June 20, 2018
#This program prompts user for input and output file names and makes a plot of the fraction of the total pop of children over time.

import pandas as pd
import matplotlib.pyplot as plt

pop = pd.read_csv(input("Enter a file name:"))
b= "Total Children in Shelter"
pop["Fraction Children"] = pop[b]/pop["Total Individuals in Shelter"]
pop.plot(x = "Date of Census", y = "Fraction Children")
fig = plt.gcf()
fig.savefig(input("Enter output file name:"))
