import os
from qgis.core import (
    QgsVectorLayer,
    QgsVectorFileWriter,
    QgsCoordinateReferenceSystem,
    QgsProject
)

# Input and output folders — update these paths!
# input_folder = r"Z:/Geofence/Kecamatan Indonesia/SUMATERA/Kecamatan Area Lampung"
input_folder = r"D:/New/Geofence/CARTRACK"
# output_folder = r"Z:/Geofence/Kecamatan Indonesia/Converted/Lampung"
output_folder = r"D:/New/Geofence/CARTRACK/Converted"

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Set target CRS (WGS 84)
target_crs = QgsCoordinateReferenceSystem("EPSG:4326")

for file in os.listdir(input_folder):
    if file.endswith(".shp"):
        input_path = os.path.join(input_folder, file)
        
        # Remove "WADMKC" prefix if present, and convert to Title Case
        base_name = os.path.splitext(file)[0]
        cleaned_name = base_name.removeprefix("WADMKC_").strip().title()

        # Create output file path
        output_path = os.path.join(output_folder, cleaned_name + ".geojson")

        layer = QgsVectorLayer(input_path, file, "ogr")
        if not layer.isValid():
            print(f"❌ Failed to load layer: {input_path}")
            continue

        # Convert and reproject to EPSG:4326
        err = QgsVectorFileWriter.writeAsVectorFormat(
            layer,
            output_path,
            "utf-8",
            target_crs,
            driverName="GeoJSON"
        )

        if err == QgsVectorFileWriter.NoError:
            print(f"✅ Converted to EPSG:4326: {file} ➜ {cleaned_name}.geojson")
        else:
            print(f"❌ Error converting: {file}")