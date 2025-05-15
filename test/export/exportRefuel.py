import requests
import pandas as pd
import json
from datetime import datetime
from requests.auth import HTTPBasicAuth
from constants.constantsGeneral import ConstantsGeneral
from constants.constantsEndpoint import ConstantsEndpoint
from util.utilLogging import Log

log = Log()
fullUrl = f"{ConstantsGeneral.getIndonesiaBaseUrl()}{ConstantsEndpoint.getFuelFillsEndpoint()}"
timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
refuelData = []
fileDir = "D:/New/Programming/export/20250515_105632_SUMB00030_EXPORT-VEHICLES.xlsx"
startTime = "2025-05-01 00:00:00"
endTime = "2025-05-15 00:59:59"

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
        
        for item in data['data'] :
            refuelData.append({
                'Registration' : item.get('registration'),
                'Vehicle Description' : item.get('vehicle_description'),
                'Time & Date' : item.get('fill_timestamp'),
                'Odometer' : item.get('fill_odometer'),
                'Amount Filled (L)' : item.get('fill_amount_litres'),
                'Location' : item.get('fill_location')
            })
        
        log.info(f"Data Successfully Inserted to dataFrame for {registration}")
    else:
        log.error(f"Error fetching data for {registration}")
        log.error(f"Response Status Code : {response.status_code}")
        log.error(f"Response Text : {response.text}")
        

df = pd.DataFrame(refuelData)
df.reset_index(drop=True, inplace=True)
df.index += 1  # Start index at 1
df.index.name = 'No'
log.info(df.head())

# Save to Excel
# outputFile = f"Z:/Programming/export/{timestamp}_{ConstantsGeneral.getApiUsername()}_EXPORT-REFUELING.xlsx"
outputFile = f"D:/New/Programming/export/{timestamp}_{ConstantsGeneral.getApiUsername()}_EXPORT-REFUELING.xlsx"
df.to_excel(outputFile, index=False)
log.info(f"Export completed : {outputFile}")