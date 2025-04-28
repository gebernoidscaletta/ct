import requests
import pandas as pd
from requests.auth import HTTPBasicAuth
from constants.constantsGeneral import ConstantsGeneral
from constants.constantsEndpoint import ConstantsEndpoint
from util.utilLogging import Log
import time

log = Log()


fullUrl =  f"{ConstantsGeneral.getIndonesiaBaseUrl()}{ConstantsEndpoint.getGeofenceEndpoint()}"

# Basic Auth credentials
USERNAME = ConstantsGeneral.getApiUsername()
PASSWORD = ConstantsGeneral.getApiPassword()

fileDir = "D:/New/Programming/export/BAHA00004_EXPORT-GEOFENCE_2.xlsx"

log.info(f"Delete Bulk Geofence Groups From XLSX")
log.info(f"Username  : {USERNAME}")
log.info(f"Initialize")

# Read the geofences.xlsx
df = pd.read_excel(fileDir)
log.info(f"File Directory : {fileDir}")

# Check if 'geofence_id' column exists
if 'geofence_id' not in df.columns:
    log.error ("No 'geofence_id' column found in the Excel File")
    exit()

# Loop through each geofence_id
for idx, row in df.iterrows():
    geofence_id = row['geofence_id']
    delete_url = f"{fullUrl}/{geofence_id}"
    
    log.info(f"Delete Geofence - {geofence_id}")

    response = requests.delete(delete_url, auth=HTTPBasicAuth(USERNAME, PASSWORD))
    
    if response.status_code == 200:
        log.info(f"Successfully deleted {geofence_id}")
        print(f"✅ Successfully deleted {geofence_id}")
    else:
        log.error(f"❌ Failed to delete {geofence_id}. Status code: {response.status_code}")
    
    # Optional: Delay a little to avoid flooding the server
    time.sleep(0.1)

log.info("All delete request has been processed")