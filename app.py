import folium as fl
import pandas as pd

def add_markers(df, group, color):
    for lt, ln, place in zip(df["Latitude"], df["Longitude"], df["Name"]):
        group.add_child(fl.Marker(location=[lt, ln], popup=place, icon=fl.Icon(color=color)))
    return group


# Initialize the map centered at a given location
map = fl.Map(location=[38.914031, -77.037238], zoom_start=12)

# Load data from CSV files
historical_df = pd.read_csv("src/DC_Historical_Important_Places.csv")
universities_df = pd.read_csv("src/DC_Universities.csv")
metro_df = pd.read_csv("src/DC_Metro_Stations.csv")

hist_group =fl.FeatureGroup(name="Important Places")
uni_group = fl.FeatureGroup(name="Universities")
metro_group = fl.FeatureGroup(name="Metro Starions")

map.add_child(add_markers(historical_df, hist_group, "green"))
map.add_child(add_markers(universities_df, uni_group, "red"))
map.add_child(add_markers(metro_df, metro_group, "blue"))

map.add_child(fl.LayerControl())

# Save the map to an HTML file
map.save("dc_map.html")
