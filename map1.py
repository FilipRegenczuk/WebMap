import folium
import pandas

map = folium.Map(location=[50,8], zoom_start=4, titles="Stamen Terrain")

capitals = pandas.read_csv("capitals.csv")      # csv file cntaining country capitals
capit_lat = list(capitals["CapitalLatitude"])
capit_lon = list(capitals["CapitalLongitude"])
capit_name = list(capitals["CapitalName"])
country_name = list(capitals["CountryName"])
continent_name = list(capitals["ContinentName"])

# function setting a color depending on the continent
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


# html message for circle marker
html = """<h4>%s:</h4>
Country: %s
<br>
Continent: %s
"""

# feature group of populations of countries
fgp = folium.FeatureGroup(name="Populations")
fgp.add_child(folium.GeoJson(data=open("population.json", 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005']<5000000
else 'yellow' if 5000000 <= x['properties']['POP2005'] < 20000000
else 'orange' if 20000000 <= x['properties']['POP2005'] < 50000000
else 'lightred' if 50000000 <= x['properties']['POP2005'] < 100000000
else 'red'}))

# feature group of capitals
fgc = folium.FeatureGroup(name="Capitals")
for lat, lon, name, ctr, con in zip(capit_lat, capit_lon, capit_name, country_name, continent_name):
    frame = folium.IFrame(html=html % (name,ctr,con), width=200, height=100)
    fgc.add_child(folium.CircleMarker(location=[lat, lon], radius=5, popup=folium.Popup(frame), fill_color=set_color(con), color='grey', fill_opacity=0.9))

# adding feature groups and layer control
map.add_child(fgp)
map.add_child(fgc)
map.add_child(folium.LayerControl())

map.save("Map1.html")
