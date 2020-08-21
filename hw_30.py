import pandas as pd
import matplotlib.pyplot as plt

homeless = pd.read\_csv(input("Enter name of the input file:"))
homeless.plot(x = "Date of Census", y = "Total Individuals in Shelter")
plt.show()

fig = plt.gcf()
fig.savefig(input("Enter name of the output file:"))
