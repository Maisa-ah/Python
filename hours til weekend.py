#Maisa Ahmad
#June 11, 2018
#This program converts hours to days and leftover hours.

hrs = int(input("Enter number of hours until the weekend:"))

days = hrs//24

print("Days:", days)

leftover = hrs%24
print("Hours:", leftover)
