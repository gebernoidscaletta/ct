import requests
import pandas as pd
from requests.auth import HTTPBasicAuth
from constants.constantsGeneral import ConstantsGeneral
from constants.constantsEndpoint import ConstantsEndpoint
from util.utilLogging import Log

log = Log()

# Base URL
BASEURL = ConstantsGeneral.getIndonesiaBaseUrl()
ENDPOINT = ConstantsEndpoint.getVehicleGroupsEndpoint()
FULLURL = f"{BASEURL}{ENDPOINT}"

# Your Basic Auth credentials
USERNAME = ConstantsGeneral.getApiUsername()
PASSWORD = ConstantsGeneral.getApiPassword()

# Empty list to store geofence data
vehicleGroups = []

# Pagination start
page = 1
limit = 1000
sequence = 1

while True:
    log.info(f"Retrieve All Vehicle Groups")
    log.info(f"Username  : {USERNAME}")
    log.info(f"Initialize")
    log.info(f"Fetching page {page}")


    # Prepare parameters
    params = {
        "page": page,
        "limit": limit
    }

    # Perform the request with Basic Auth
    response = requests.get(url = f"{BASEURL}{ENDPOINT}",
                            params = params, 
                            auth = HTTPBasicAuth(USERNAME, PASSWORD))
    
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
    for item in data:  # assuming response["data"]
        group_id = item.get("group_id")
        name = item.get("name")
        description = item.get("description")
        vehicles = item.get("vehicles", [])

        for vehicle in vehicles:
            vehicleGroups.append({
                "group_id": group_id,
                "name": name,
                "description": description,
                "vehicle_id": vehicle.get("vehicle_id"),
                "registration": vehicle.get("registration")
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

# Create DataFrame
df = pd.DataFrame(vehicleGroups)
sequence += 1

# Save to Excel
output_file = f"D:/New/Programming/export/{ConstantsGeneral.getApiUsername()}_VEHICLE-GROUP_{sequence}.xlsx"
df.to_excel(output_file, index=False)
log.info(f"Export completed : {output_file}")