# import requests
import base64 
# from util.utilLogging import Log
from constants.constantsGeneral import ConstantsGeneral

# log = Log()

class fetchGeofencesGroups:
    # log.info("fetchGeofenceGroups")
    # username = "CART00013"
    # password = "13f582b1290c43a1a548a4f104d3002444dd5a1a30264209f93731629106356e"
    # log.info(f"Credentials fetched using username - {username}")
    username = ConstantsGeneral.getApiUsername()
    print(username)

    # auth = f"{username}:{password}"
    # authBytes = auth.encode('ascii')
    # base64Bytes = base64.b64encode(authBytes)
    # base64Auth = base64Bytes.decode('ascii')

    # fullUrl = "https://fleetapi-id.cartrack.com/rest/geofences/groups"
    # headers = {
    #     'Authorization': f'Basic {base64Auth}',
    #     'Content-Type': 'application/json'
    # }
    # payload = {
    # }

    # response = requests.request("GET", fullUrl, headers=headers, data=payload)
    # print(response.json())
    # log.info(response)