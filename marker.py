# COLOR of Markers
# GREEN low of 20 meter
# ORANGE between of 20 and 50 meter
# RED upper of 50 meter

import folium
import pandas as pd

waterFalls = pd.read_csv("waterfalls.txt")
# If you want read from csv file
# waterFalls = pd.read_csv("waterfalls.csv")

map = folium.Map([32, 53], zoom_start=6)

for row in range(waterFalls.T.columns.stop):
    
    name = waterFalls.iloc[row, 0]
    STATE = waterFalls.iloc[row, 1]
    height = waterFalls.iloc[row, 2]
    latitude = float(waterFalls.iloc[row, 3])
    longitude = float(waterFalls.iloc[row, 4])
    
    color = 'red' # Default height is upper 50 so red color is default color
    
    if height < 20:
        color = "green"
    
    elif 50 > height > 20:
        color = "orange"
    
    
    folium.Marker(
        location=[latitude, longitude],
        popup=f"{name} در استان {STATE} با ارتفاع {height}",
        icon=folium.Icon(color=color),
    ).add_to(map)



map.save("waterFallsMap.html")