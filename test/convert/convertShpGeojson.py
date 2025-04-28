import sys
import os

# Setup QGIS paths
QGIS_PREFIX_PATH = r"C:/Program Files/QGIS 3.40.5"  # <-- adjust this if your QGIS version/path is different
sys.path.append(os.path.join(QGIS_PREFIX_PATH, 'apps', 'qgis', 'python'))
sys.path.append(os.path.join(QGIS_PREFIX_PATH, 'apps', 'qgis', 'python', 'plugins'))

# Set environment variables (important for Qt plugins)
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = os.path.join(QGIS_PREFIX_PATH, 'apps', 'Qt5', 'plugins')

# Now you can import QGIS modules
from qgis.core import (
    QgsApplication,
    QgsVectorLayer,
    QgsVectorFileWriter,
    QgsCoordinateReferenceSystem,
    QgsCoordinateTransformContext
)

# Initialize QGIS Application
qgs = QgsApplication([], False)
qgs.initQgis()

# Set your input and output folders
input_folder = "D:/New/Temp/Kecamatan Indonesia/JAWA/Kecamatan Area Jawa Tengah"
output_folder = "D:/New/Temp/Kecamatan Indonesia/JAWA/JawaTengah-Exported"

# Make sure output folder exists
os.makedirs(output_folder, exist_ok=True)

# Set target CRS (EPSG:4326)
target_crs = QgsCoordinateReferenceSystem("EPSG:4326")

# Loop through all files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".shp"):
        input_path = os.path.join(input_folder, filename)
        
        # Load shapefile
        layer = QgsVectorLayer(input_path, filename, "ogr")
        
        if not layer.isValid():
            print(f"Failed to load {filename}")
            continue
        
        # Set output filename (replace .shp with .geojson)
        output_filename = os.path.splitext(filename)[0] + ".geojson"
        output_path = os.path.join(output_folder, output_filename)
        
        # Export to GeoJSON with CRS transformation
        error = QgsVectorFileWriter.writeAsVectorFormatV3(
            layer,
            output_path,
            QgsCoordinateTransformContext(),
            driverName="GeoJSON",
            options=[],
            newCrs=target_crs
        )
        
        if error[0] == QgsVectorFileWriter.NoError:
            print(f"Successfully exported: {output_filename}")
        else:
            print(f"Error exporting {filename}: {error}")

print("Batch export complete.")

# Exit QGIS Application
qgs.exitQgis()
