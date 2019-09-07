import folium
import pandas

map = folium.Map(location=[50,8], zoom_start=4, titles="Stamen Terrain")
capitals = pandas.read_csv("capitals.csv")
capit_lat = list(capitals["CapitalLatitude"])
capit_lon = list(capitals["CapitalLongitude"])
capit_name = list(capitals["CapitalName"])
country_name = list(capitals["CountryName"])
continent_name = list(capitals["ContinentName"])

def set_color(continent):
    if continent == "Africa":
        return 'darkgreen'
    elif continent == "Europe":
        return 'orange'
    elif continent == "Asia":
        return 'red'
    elif continent == "North America":
        return 'blue'
    elif continent == "South America":
        return 'lightblue'
    elif continent == "Australia":
        return 'beige'
    else:
        return 'gray'


html = """<h4>%s:</h4>
Country: %s
<br>
Continent: %s
"""


fg = folium.FeatureGroup(name="My map")

for lat, lon, name, ctr, con in zip(capit_lat, capit_lon, capit_name, country_name, continent_name):
    frame = folium.IFrame(html=html % (name,ctr,con), width=200, height=100)
    fg.add_child(folium.CircleMarker(location=[lat, lon], radius=5, popup=folium.Popup(frame), fill_color=set_color(con), color='black', fill_opacity=0.8))

map.add_child(fg)

map.save("Map1.html")
