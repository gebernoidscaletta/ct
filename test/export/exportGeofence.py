import requests
import pandas as pd
from requests.auth import HTTPBasicAuth
from constants.constantsGeneral import ConstantsGeneral
from constants.constantsEndpoint import ConstantsEndpoint
from util.utilLogging import Log

log = Log()

fullUrl = F"{ConstantsGeneral.getIndonesiaBaseUrl()}{ConstantsEndpoint.getGeofenceEndpoint()}"

# Empty list to store geofence data
geofences = []

# Pagination start
page = 1
limit = 1000
sequence = 3

while True:
    log.info(f"Retrieve All Geofences To XLSX")
    log.info(f"Username  : {ConstantsGeneral.getApiUsername()}")
    log.info(f"Initialize")
    log.info(f"Full URL : {fullUrl}")
    log.info(f"Fetching page {page}")


    # Prepare parameters
    params = {
        "page": page,
        "limit": limit
    }

    # Perform the request with Basic Auth
    response = requests.get(fullUrl, 
                            params = params, 
                            auth = HTTPBasicAuth(ConstantsGeneral.getApiUsername(), 
                                                 ConstantsGeneral.getApiPassword())
                            )
    
    if response.status_code != 200:
        log.error(f"Failed to fetch page {page}. Status Code : {response.status_code}")
        break

    # Load JSON
    result = response.json()

    # Extract 'data'
    data = result.get('data', [])
    
    if not data:
        log.error(f"No data found on page {page}. Stopping")
        break

    # Extract geofence_id and name
    for item in data:
        geofences.append({
            "geofence_id": item.get("geofence_id"),
            "name": item.get("name"),
            "description" : item.get("description"),
            "polygon" : item.get("polygon"),
            "create_ts" : item.get("create_ts"),
            "update_ts" : item.get("update_ts")
        })

    # Pagination control
    meta = result.get('meta', {})
    current_page = meta.get('current_page', 1)
    last_page = meta.get('last_page', 1)

    log.info(f"Processed Page {current_page} - {last_page}")

    # Check if we're done
    if current_page >= last_page:
        log.info("All pages successfully fetched")
        break

    # Otherwise, go to next page
    page += 1
    sequence += 1
    
# Create DataFrame
df = pd.DataFrame(geofences)
sequence += 1

# Save to Excel
output_file = f"Z:/Programming/export/{ConstantsGeneral.getApiUsername()}_EXPORT-GEOFENCE_{sequence}.xlsx"
# output_file = f"/home/gebernoid-mattisse-scaletta/Documents/code/export/{ConstantsGeneral.getApiUsername()}_EXPORT-GEOFENCE_{sequence}.xlsx"
df.to_excel(output_file, index=False)
log.info(f"Export completed : {output_file}")