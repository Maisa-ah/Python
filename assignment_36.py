#Maisa Ahmad
#June 25, 2018
#The program runs a parking ticket program.

import pandas as pd

csvFile = input("Enter file name:")
tickets = pd.read_csv(csvFile)

attribute = input("Enter attribute:")
print("The 10 worst offenders are:")
print(tickets[attribute].value_counts()[:10])

