#Maisa Ahmad
#June 18, 2018
#This program prompts for borough and output file name and displays the population over time.

import matplotlib.pyplot as plt
import pandas as pd

borough = input("Enter borough name:")
pop = pd.read_csv('nycHistPop.csv', skiprows = 5)

pop["Fraction"] = pop[borough]/pop["Total"]

pop.plot(x = "Year", y = "Fraction")

plt.show()

fig = plt.gcf()
fig.savefig(input("Enter output file name:"))
