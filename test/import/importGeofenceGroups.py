import requests
import base64 
import json
from util.utilLogging import Log
from constants.constantsEndpoint import ConstantsEndpoint
from constants.constantsGeneral import ConstantsGeneral

log = Log ()

auth = f"{ConstantsGeneral.getApiUsername()}:{ConstantsGeneral.getApiPassword()}"

auth_bytes = auth.encode('ascii')
base64_bytes = base64.b64encode(auth_bytes)
base64_auth = base64_bytes.decode('ascii')

log.info("Import Geofence Group")
log.info(f"Username : {ConstantsGeneral.getApiUsername()}")
log.info("Initialize")
url = f"{ConstantsGeneral.getIndonesiaBaseUrl}{ConstantsEndpoint.geofenceRetrieveAllGroups()}"
log.info(f"Full URL : {url}")
payload = json.dumps(
    {
        "name": "Jawa Barat",
        "description": "Geofence Import",
        "subuser_id": ""
        }
    )
log.info(f"Payload : {payload}")
#GROUP ID FOR TEST GEOFENCES BAHA 00004 : 2761
headers = {
    'Authorization': f'Basic {base64_auth}',
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)
if response.status_code != 200:
    log.error(f"Status Code : {response.status_code}")
else:
    log.info(f"Response : {response.text}")

log.info("Geofence Groups has been successfully created")