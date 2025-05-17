import requests
import pandas as pd
import json
from datetime import datetime
from requests.auth import HTTPBasicAuth
from constants.constantsGeneral import ConstantsGeneral
from constants.constantsEndpoint import ConstantsEndpoint
from util.utilLogging import Log

log = Log()
fullUrl = f"{ConstantsGeneral.getIndonesiaBaseUrl()}{ConstantsEndpoint.getVehicleEndpoint()}"
timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
vehicleData = []

# Pagination start
page = 1
limit = 1000
sequence = 1

while True:
    log.info(f"Retrieve All Vehicles")
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
    
    for item in data:
        # log.info(f"Response Data : {json.dumps(item,indent = 4)}")

        vehicleData.append({
            "vehicle_id": item.get("vehicle_id"),
            "terminal_id": item.get("terminal_id"),
            "terminal_serial": item.get("terminal_serial"),
            "registration": item.get("registration"),
            "default_timezone": item.get("default_timezone"),
            "monthly_mileage_limit": item.get("monthly_mileage_limit"),
            "tolling_tag_id": item.get("tolling_tag_id"),
            "vehicle_name": item.get("vehicle_name"),
            "client_vehicle_description": item.get("client_vehicle_description"),
            "client_vehicle_description2": item.get("client_vehicle_description2"),
            "client_vehicle_description3": item.get("client_vehicle_description3"),
            "licence_code": item.get("licence_code"),
            "licence_issued_date": item.get("licence_issued_date"),
            "licence_expiry_date": item.get("licence_expiry_date"),
            "max_speed": item.get("max_speed"),
            "manufacturer": item.get("manufacturer"),
            "default_driver": item.get("default_driver"),
            "home_geofence": item.get("home_geofence"),
            "model": item.get("model"),
            "model_year": item.get("model_year"),
            "colour": item.get("colour"),
            "chassis_number": item.get("chassis_number"),
            "is_under_maintenance": item.get("is_under_maintenance"),
            "vehicle_type_id": item.get("vehicle_type_id"),
            "vehicle_type": item.get("vehicle_type"),
            "has_camera": item.get("has_camera"),
            "sensors": item.get("sensors"),
            "custom_fields": item.get("custom_fields")
        })
        # vehicleData.append({
        #     "geofence_id": item.get("geofence_id"),
        #     "name": item.get("name")
        # })
        
    log.info(f"Response Data : {vehicleData}")
    # Pagination control
    meta = result.get('meta', {})
    currentPage = meta.get('current_page', 1)
    lastPage = meta.get('last_page', 1)

    log.info(f"Processed Page {currentPage} - {lastPage}")

    # Check if we're done
    if currentPage >= lastPage:
        log.info("All pages successfully fetched")
        break

    # Otherwise, go to next page
    page += 1
    
# Create DataFrame
df = pd.DataFrame(vehicleData)

# Save to Excel
output_file = f"Z:/Programming/export/{timestamp}_{ConstantsGeneral.getApiUsername()}_EXPORT-VEHICLES.xlsx"
df.to_excel(output_file, index=False)
log.info(f"Export completed : {output_file}")