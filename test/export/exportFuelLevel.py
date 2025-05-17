import requests
import pandas as pd
import json
from datetime import datetime
from requests.auth import HTTPBasicAuth
from constants.constantsGeneral import ConstantsGeneral
from constants.constantsEndpoint import ConstantsEndpoint
from util.utilLogging import Log

log = Log()
fullUrl = f"{ConstantsGeneral.getIndonesiaBaseUrl()}{ConstantsEndpoint.getFuelLevelEndpoint()}"

timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
fuelLevelData = []
fileDir = "Z:/Programming/export/20250517013707_PERM00001_EXPORT-VEHICLES.xlsx"
startTime = "2025-05-15 00:00:00"
endTime = "2025-05-15 23:59:59"

dataSource = pd.read_excel(fileDir)
log.info(f"File Directory : {fileDir}")
params = {
    "start_timestamp" : startTime,
    "end_timestamp" : endTime
}

if 'registration' not in dataSource.columns :
    log.error("No 'Registration' column founds in the file")
    exit()

for idx, row in dataSource.iterrows():
    registration = row['registration']
    addedUrl = f"{fullUrl}/{registration}"
    
    log.info(f"Fetching Refueling Data - {registration}")
    
    response = requests.get(
        addedUrl,
        params = params,
        auth = HTTPBasicAuth(ConstantsGeneral.getApiUsername(),
                             ConstantsGeneral.getApiPassword())
    )
    
    if response.status_code == 200 :
        log.info(f"{registration} Data : {response.json()}")
        data = response.json()
        
        log.info(f"Inserting Data to dataFrame for {registration}")
        
        fuelLevelData.append({
            'Registration': registration,  # Using the registration from the request
            'Start Liters': data.get('data', {}).get('start_period', {}).get('liters'),
            'Start Timestamp': data.get('data', {}).get('start_period', {}).get('timestamp'),
            'Start Accurate': data.get('data', {}).get('start_period', {}).get('accurate'),
            'End Liters': data.get('data', {}).get('end_period', {}).get('liters'),
            'End Timestamp': data.get('data', {}).get('end_period', {}).get('timestamp'),
            'End Accurate': data.get('data', {}).get('end_period', {}).get('accurate'),
            'Estimated Fuel Used': data.get('data', {}).get('estimated_fuel_used'),
            'Calibrated': data.get('data', {}).get('calibrated')
        })
        
        log.info(f"Data Successfully Inserted to dataFrame for {registration}")
    else:
        log.error(f"Error fetching data for {registration}")
        log.error(f"Response Status Code : {response.status_code}")
        log.error(f"Response Text : {response.text}")
        

df = pd.DataFrame(fuelLevelData)
df.reset_index(drop=True, inplace=True)
df.index += 1  # Start index at 1
df.index.name = 'No'
log.info(df.head())

# Save to Excel
outputFile = f"Z:/Programming/export/{timestamp}_{ConstantsGeneral.getApiUsername()}_EXPORT-REFUELING.xlsx"
df.to_excel(outputFile, index=False)
log.info(f"Export completed : {outputFile}")