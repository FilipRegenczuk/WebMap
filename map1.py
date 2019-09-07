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
        return 'red'
    elif continent == "Asia":
        return 'darkred'
    elif continent == "North America":
        return 'darkblue'
    elif continent == "South America":
        return 'blue'
    elif continent == "Australia":
        return 'purple'


html = """<h4>%s:</h4>
Country: %s
<br>
Continent: %s
"""


fg = folium.FeatureGroup(name="My map")

for lat, lon, name, ctr, con in zip(capit_lat, capit_lon, capit_name, country_name, continent_name):
    frame = folium.IFrame(html=html % (name,ctr,con), width=200, height=100)
    fg.add_child(folium.Marker(location=[lat, lon], popup=folium.Popup(frame), icon=folium.Icon(color=set_color(con))))

map.add_child(fg)

map.save("Map1.html")