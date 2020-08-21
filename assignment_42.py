#Maisa Ahmad
#June 27, 2018
#This program prompts for a CSV file, name of output, and creates a map with markers for all traffic collisions.

import folium
import pandas as pd

file = input("Enter CSV file name:")
cuny = pd.read_csv(file)

mapCUNY = folium.Map(location=[40.768731, -73.964915])

for index,row in cuny.iterrows():
    lat = row["LATITUDE"]
    lon = row["LONGITUDE"]
    name = row["TIME"]
    newMarker = folium.Marker([lat, lon], popup=name)
    newMarker.add_to(mapCUNY)
newF = input("Enter output file name:")
mapCUNY.save(outfile=newF)
