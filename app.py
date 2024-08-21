import folium as fl
import pandas as pd

# Initialize the map centered at a given location
map = fl.Map(location=[38.914031, -77.037238], zoom_start=12)

# Load data from CSV files
historical_df = pd.read_csv("src/DC_Historical_Important_Places.csv")
universities_df = pd.read_csv("src/DC_Universities.csv")
metro_df = pd.read_csv("src/DC_Metro_Stations.csv")

hist_group =fl.FeatureGroup(name="Important Places")
uni_group = fl.FeatureGroup(name="Universities")
metro_group = fl.FeatureGroup(name="Metro Starions")

# Add markers for historical/important places
for lt, ln, place in zip(historical_df["Latitude"], historical_df["Longitude"], historical_df["Name"]):
    hist_group.add_child(fl.Marker(location=[lt, ln], popup=place, icon=fl.Icon(color="green")))

map.add_child(hist_group)

# Add markers for historical/important places
for lt, ln, place in zip(universities_df["Latitude"], universities_df["Longitude"], universities_df["Name"]):
    uni_group.add_child(fl.Marker(location=[lt, ln], popup=place, icon=fl.Icon(color="red")))

map.add_child(uni_group)

# Add markers for historical/important places
for lt, ln, place in zip(metro_df["Latitude"], metro_df["Longitude"], metro_df["Name"]):
    metro_group.add_child(fl.Marker(location=[lt, ln], popup=place, icon=fl.Icon(color="blue")))

map.add_child(metro_group)

map.add_child(fl.LayerControl())

# Save the map to an HTML file
map.save("dc_map.html")
