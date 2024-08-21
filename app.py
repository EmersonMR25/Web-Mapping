import folium as fl  # Import the folium library for map creation
import pandas as pd  # Import the pandas library for data manipulation

def add_markers(df, group, color):
    """
    Adds markers to a Folium FeatureGroup based on data in a DataFrame.

    Parameters:
    - df (pd.DataFrame): DataFrame containing location data with columns 'Latitude', 'Longitude', 'Name', and 'Description'.
    - group (folium.FeatureGroup): Folium FeatureGroup to which the markers will be added.
    - color (str): Color of the marker icons (e.g., 'green', 'red', 'blue').

    Returns:
    - folium.FeatureGroup: The updated FeatureGroup with added markers.
    """
    for lt, ln, place, desc in zip(df["Latitude"], df["Longitude"], df["Name"], df["Description"]):
        # HTML content for the popup with center-aligned name and description
        popup_html = f"""
        <div style="text-align: center;">
            <strong>{place}</strong><br>
            {desc}
        </div>
        """
        # Create a marker with the specified location, popup, and icon color, then add it to the group
        group.add_child(fl.Marker(location=[lt, ln], popup=fl.Popup(popup_html, max_width=300), icon=fl.Icon(color=color)))
    
    return group

# Initialize the map centered at the specified location with the OpenStreetMap tile layer and set zoom level
map = fl.Map(location=[38.914031, -77.037238], tiles="OpenStreetMap", zoom_start=13)

# Load data from CSV files into DataFrames
historical_df = pd.read_csv("src/DC_Historical_Important_Places.csv")
universities_df = pd.read_csv("src/DC_Universities.csv")
metro_df = pd.read_csv("src/DC_Metro_Stations.csv")

# Create FeatureGroup objects for different categories of locations
hist_group = fl.FeatureGroup(name="Important Places")
uni_group = fl.FeatureGroup(name="Universities")
metro_group = fl.FeatureGroup(name="Metro Stations")  # Fixed typo from "Metro Starions" to "Metro Stations"

# Add markers for each category to the map using the add_markers function
map.add_child(add_markers(historical_df, hist_group, "green"))
map.add_child(add_markers(universities_df, uni_group, "red"))
map.add_child(add_markers(metro_df, metro_group, "blue"))

# Add a layer control to the map to allow users to toggle different feature groups
map.add_child(fl.LayerControl())

# Save the map to an HTML file for viewing in a web browser
map.save("dc_map.html")
