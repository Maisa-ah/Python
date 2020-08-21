#Maisa Ahmad
#June 18, 2018
#This program prompts for borough and output file name and displays the population over time.

import matplotlib.pyplot as plt
import pandas as pd


pop = pd.read_csv("nycHistPop.csv", skiprows = 5)

boro = input("Enter borough:")

print("Average population:", pop[boro].mean())
print("Maximum population:", pop[boro].max())
