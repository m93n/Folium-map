# COLOR of Markers
# GREEN low of 20 meter
# ORANGE between of 20 and 50 meter
# RED upper of 50 meter

import folium
import pandas as pd

waterFalls = pd.read_csv("waterfalls.txt")
# If you want read from csv file
# waterFalls = pd.read_csv("waterfalls.csv")

lat = list(waterFalls['LATITUDE'])
lon = list(waterFalls['LONGITUDE'])
name = list(waterFalls['NAME'])
state = list((waterFalls['STATE']))
height = list(waterFalls['HEIGHT'])

map = folium.Map(location=[32, 53], zoom_start=5)

#waterfalls
fg_w = folium.FeatureGroup("Waterfalls")

def color_producer(height):
    if height < 20:
        color= "green"
    elif height <= 50:
        color = "orange"
    else:
        color = "red"
        
    return color

for lt, ln, nm, hg, st in zip(lat, lon, name, height, state):
    html = """
    <h1>Name: %s</h1>
    <h4>Height: %s</h4>
    <h4>State: %s</h4>
    <a href="https://google.com/search?q=%s" target="_blank">Read More</a>
    """ % (nm, hg, st, nm)
    iframe = folium.IFrame(html=html, width=300, height=200)
    fg_w.add_child(folium.Marker(location=[lt,ln], popup=folium.Popup(iframe), icon=folium.Icon(color=color_producer(hg))))

#countries borders
fg_b = folium.FeatureGroup(name="Countries Boredrs")
world_data = open("world.json", encoding='utf-8-sig').read()
folium.GeoJson(data=world_data).add_to(fg_b)

#adding fg(s) to map
fg_b.add_to(map)
map.add_child(fg_w)

#add layer control to map
map.add_child(folium.LayerControl())

map.save("waterFallsMap.html")