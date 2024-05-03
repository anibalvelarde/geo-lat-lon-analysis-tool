# Geo-Coordinate Analysis Tool

This Python application processes a JSON file containing geographic data points to calculate a centroid coordinate equidistant from all provided points. It generates links to Google Maps for searching nearby restaurants, hotels, and tourist attractions and produces reports in both PDF and Markdown formats.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Installation

To run this project, you will need to install the necessary Python libraries. Install these dependencies via pip:

```bash
pip install geopy folium pandas reportlab markdown2
```

## Usage
Prepare a JSON file named data.json with the following format:

```json
[
    { "id": 123, "thing-type": "type-a", "thing-name": "name", "lat": 12.345, "lon": 67.890 },
    { "id": 456, "thing-type": "type-b", "thing-name": "another name", "lat": 23.456, "lon": 78.901 }
]
```

Execute the program with:
```bash
  $ python app.py
```

This generates a PDF and Markdown report detailing the centroid of the provided coordinates and links to Google Maps searches for nearby amenities.

## Features
- Centroid Calculation: Determines the geographic center from the latitude and longitude of input points.
- Google Maps Integration: Creates URLs for Google Maps searches for restaurants, hotels, and tourist attractions near the calculated centroid.
- Report Generation: Produces a comprehensive report in PDF and Markdown formats, containing details about the centroid and links to Google Maps searches.
- Interactive Map Creation: Uses Folium to create an interactive map that visualizes each point, the centroid, and lines connecting each point to the centroid.
- Output:
  - [Map Image](./assets/map-output.png) (embedded in HTML file) of where the centroid is located
  - [MARKDOWN file](./assets/markdown-output.png) with the lat/lon for centroid and links to Google Maps of what is `nearby` as far as Restaurants, Hotels, and Tourist Attractions.
  - [PDF file](./assets/pdf-output.png) version of the MARKDOWN content.

## Dependencies
This project utilizes the following Python libraries:

- **geopy** for geographic calculations.
- **folium** for map visualizations.
- **pandas** for data manipulation.
- **reportlab** for PDF report generation.
- **markdown2** for Markdown content generation.

## Contributing
We welcome contributions to this project. To contribute, please fork the repository, make your changes, and submit a pull request. We look forward to your suggestions and improvements.
