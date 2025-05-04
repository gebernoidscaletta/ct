import requests
import pandas as pd
from datetime import datetime, timedelta
from constants.constantsGeneral import ConstantsGeneral
from constants.constantsEndpoint import ConstantsEndpoint
from util.utilLogging import Log
from requests.auth import HTTPBasicAuth

log = Log ()
currTime = datetime.now()
formatTime = currTime.strftime("%Y%m%d")
fullUrl = f"{ConstantsGeneral.getIndonesiaBaseUrl()}{ConstantsEndpoint.getAlertNotificationEndpoint()}"

def fetchMonth(startDate, endDate):
    allData = []
    page = 1
    while True:
        params = {
            "filter[date_from]": startDate.strftime("%Y-%m-%d %H:%M:%S"),
            "filter[date_to]": endDate.strftime("%Y-%m-%d %H:%M:%S"),
            "page": page,
            "limit": 1000
        }
        response = requests.get(fullUrl, 
                                params = params,
                                auth = HTTPBasicAuth(ConstantsGeneral.getApiUsername(),
                                                     ConstantsGeneral.getApiPassword()) 
                                )
        response.raise_for_status()
        res = response.json()

        data = res.get("data", [])
        if not data:
            break
        allData.extend(data)

        meta = res.get("meta", {})
        lastPage = meta.get("last_page", 1)
        print(f"Fetched page {page}/{lastPage} for {startDate.strftime('%B %Y')}")
        if page >= lastPage:
            break
        page += 1

    return allData

# Loop Jan to Aug
for month in range(1, 5):
    start = datetime(2025, month, 1)
    end = (start + timedelta(days=32)).replace(day=1)  # first day of next month
    
    records = fetchMonth(start, end)
    if records:
        df = pd.DataFrame(records)
        filename = f"Z:/Programming/export/{formatTime}_{ConstantsGeneral.getApiUsername()}_ALERTS_{start.strftime('%Y_%m')}.xlsx"
        df.to_excel(filename, index=False)
        print(f"Exported {filename} ✅")
    else:
        print(f"No data found for {start.strftime('%B %Y')} ❗")

print("All months exported successfully 🚀")
