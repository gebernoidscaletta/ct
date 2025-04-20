import requests
import json
import pandas as pd
from requests.auth import HTTPBasicAuth

# API credentials
username = "ASLI00001"
apiToken = "f5ca1cd18c401d7dce04309b53ed78dd86236cd69704e3618ba86412269cb167"

# List of vehicle registrations
registrations = ["BP9532EY"]

# Define the date range
start_timestamp = '2024-09-15 00:00:00'
end_timestamp = '2024-09-31 23:59:59'

# List to store all vehicle data
all_rows = []

# Loop through each registration
for registration in registrations:
    response = requests.get(
        url=f"https://fleetapi-id.cartrack.com/rest/fuel/fills/{registration}?",
        params={
            'start_timestamp': start_timestamp,
            'end_timestamp': end_timestamp
        },
        auth=HTTPBasicAuth(
            username=username,
            password=apiToken
        )
    )

    if response.status_code == 200:
        data = response.json()  # Call .json() method to parse the response
        
        # Prepare data for DataFrame
        for entry in data['data']:
            all_rows.append({
                'Registration': entry['registration'],
                'Vehicle Description': entry['vehicle_description'],
                'Time and Date': entry['fill_timestamp'],
                'Odometer': entry['fill_odometer'],
                'Amount Filled': entry['fill_amount_litres'],
                'Location': entry['fill_location']
            })
    else:
        print(f"Error fetching data for {registration}: {response.status_code}, {response.text}")

# Create a DataFrame from all collected data
df = pd.DataFrame(all_rows)

# Add a counting column
df.reset_index(drop=True, inplace=True)
df.index += 1  # Start index at 1
df.index.name = 'No'

# Show the DataFrame
print(df.head())  # Preview the first few rows

# Save to Excel
output_file = 'D:/New/Programming/fuelFillData_BANG00008_3.xlsx'
df.to_excel(output_file, index=True)

print(f'Data successfully written to {output_file}')