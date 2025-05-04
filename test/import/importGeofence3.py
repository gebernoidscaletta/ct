import requests
import pandas as pd
import json
import time
from requests.auth import HTTPBasicAuth
from pathlib import Path
from constants.constantsGeneral import ConstantsGeneral
from constants.constantsEndpoint import ConstantsEndpoint
from util.utilLogging import Log

log = Log()
fullUrl = f"{ConstantsGeneral.getIndonesiaBaseUrl()}{ConstantsEndpoint.getGeofenceEndpoint()}"
folderPath = Path("Z:/Geofence/Kecamatan Indonesia/Converted/NusaTenggaraTimur/NusaTenggaraTimur-JSON")
jsonFiles = list(folderPath.glob('*.json'))
succImport = 0
failImport = 0 

log.info(f"Import Geofence")
log.info(f"Username : {ConstantsGeneral.getApiUsername()}")
log.info(f"Initialize")
log.info(f"Folder Path : {folderPath}")

for folderPath in jsonFiles:
    # if succImport > 0 or failImport > 0 :
    #     time.sleep(1)
        
    try :
        with open(folderPath,'r') as file:
            jsonData = json.load(file)

        payload = json.dumps(jsonData)

        response = requests.post(fullUrl,
                                 auth = HTTPBasicAuth(
                                     ConstantsGeneral.getApiUsername(),
                                     ConstantsGeneral.getApiPassword()),
                                 data = payload
                                 )
        log.info(f"Response Body : {response.json()}")
        if response.status_code == 200 :
            succImport += 1
        else :
            failImport += 1
            log.error(f"Failed Import File : {folderPath.name}")

    except Exception as e:
        failImport += 1
        log.error(f"Error Processing {folderPath.name}")
        log.error(f"Error Message : {e}")
        
log.info("Import Summary")
log.info(f"Successfully Imported : {succImport}")
log.info(f"Failed Imported : {failImport}")
log.info(f"Total Processed : {len(jsonFiles)}")