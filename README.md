# Interactive DC - Map with Folium

## Overview

This project uses the Folium library to create an interactive map with custom markers. The map displays important places, universities, and metro stations, with each marker featuring a popup that includes a name and description. The map is centered on a specific location and saved to an HTML file for easy viewing in a web browser.

## Requirements

- **Python Version**: 3.x
- **Libraries**:
  - `folium`: For creating interactive maps.
  - `pandas`: For data manipulation and handling CSV files.

## Running the Script

To run this program and generate the interactive map, follow these steps:

1. **Install Python**:
   Ensure that you have Python 3.x installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

2. **Install Required Libraries**:
   You need to install the necessary Python libraries (`folium` and `pandas`). Open a terminal or command prompt and execute the following command:

   ```bash
   pip install folium pandas
   ```

3. **Run the Script**:
   Open a terminal or command prompt, navigate to the directory where app.py is saved, and execute the script with Python:

   ```bash
   python app.py
   ```

   Now open the created html file and open it on a web browser.

# To-Do List

## Map Enhancements

- [ ] **Add Appropriate Icons**: Include custom icons for different types of markers.
- [ ] **Add Polygons for DC Map and Its Wards**: Overlay polygons to represent different wards on the DC map.
- [ ] **Add More Points of Interest**: Include additional locations of interest on the map.

## Additional Tasks

- [ ] **Optimize Map Performance**: Ensure the map loads efficiently with large datasets.
- [ ] **Implement Search Functionality**: Add a search bar to allow users to find specific locations.
- [ ] **Include Legend for Map**: Add a legend to explain the meanings of different marker colors and icons.
- [ ] **Enhance Popup Styling**: Improve the design of popups for better readability and user experience.
- [ ] **Add Geolocation Feature**: Integrate a geolocation feature to center the map on the user's current location.
