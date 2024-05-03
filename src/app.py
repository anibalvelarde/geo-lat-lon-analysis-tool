import json
import numpy as np
import os
import sys
import folium
from geopy.distance import geodesic
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import markdown2

# Load the data file
def load_data(filepath):
    with open(filepath, 'r') as file:
        data = json.load(file)
    return data

# Calculate the common LAT/LON coordinates
def calculate_centroid(data):
    lats = [item['lat'] for item in data]
    lons = [item['lon'] for item in data]
    centroid_lat = np.mean(lats)
    centroid_lon = np.mean(lons)
    return (centroid_lat, centroid_lon)

# Perform Google-Map Searches
def google_maps_search_url(lat, lon, query):
    return f"https://www.google.com/maps/search/{query}/@{lat},{lon},14z"

def create_search_links(lat, lon):
    queries = ["restaurants", "hotels", "tourist"]
    return {query: google_maps_search_url(lat, lon, query) for query in queries}

# Generate the map with lines to centroid
def create_map(data, centroid, filename):
    m = folium.Map(location=centroid, zoom_start=5, tiles='OpenStreetMap')
    folium.Marker(centroid, popup='Centroid', icon=folium.Icon(color='red')).add_to(m)
    for item in data:
        point = [item['lat'], item['lon']]
        folium.Marker(point, popup=f"{item['thing-name']}").add_to(m)
        folium.PolyLine([point, centroid], color='blue').add_to(m)
    m.save(filename)

# Generate reports
def create_pdf_report(data, filename):
    c = canvas.Canvas(filename, pagesize=letter)
    text = c.beginText(40, 750)
    text.setFont("Helvetica", 12)
    text.textLines(f"Centroid Location: {data['centroid']}\n")
    for key, url in data['links'].items():
        text.textLines(f"{key.capitalize()} Search: {url}\n")
    c.drawText(text)
    c.save()

def create_markdown_report(data, filename):
    with open(filename, 'w') as mdfile:
        mdfile.write(f"## Centroid Location\n")
        mdfile.write(f"- Latitude, Longitude: {data['centroid']}\n")
        mdfile.write("## Links\n")
        for key, url in data['links'].items():
            mdfile.write(f"- [{key.capitalize()}]({url})\n")

def ensure_output_directory():
    directory = "./output"
    if not os.path.exists(directory):
        os.makedirs(directory)
        print("Directory './output' was created.")
    else:
        print("Directory './output' already exists.")

# Main Function
def main(filepath):
    if not os.path.exists(filepath):
        print(f"Error: The file '{filepath}' does not exist.")
        print("Usage: python app.py /path/to/file/data.json")
        sys.exit(1)

    data = load_data(filepath)
    centroid = calculate_centroid(data)
    links = create_search_links(*centroid)
    report_data = {
        "centroid": centroid,
        "links": links
    }
    ensure_output_directory()
    create_pdf_report(report_data, "output/report.pdf")
    create_markdown_report(report_data, "output/report.md")
    create_map(data, centroid, 'output/map.html')

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python app.py /path/to/file/data.json")
        sys.exit(1)
    main(sys.argv[1])
