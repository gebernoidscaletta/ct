import requests
import pandas as pd
import json
import time
from datetime import datetime
from requests.auth import HTTPBasicAuth
from constants.constantsGeneral import ConstantsGeneral
from constants.constantsEndpoint import ConstantsEndpoint
from util.utilLogging import Log

log = Log()
fullUrl = f"{ConstantsGeneral.getIndonesiaBaseUrl()}{ConstantsEndpoint.getVehiclesStatusEndpoint()}"
vehicleData = []
registration = "DA1672KK"
def fetchVehicleStatus():
    params = {
        "filter[registration]": {registration}
    }
    
    try:
        response = requests.get(fullUrl,
                                params = params,
                                auth = HTTPBasicAuth(ConstantsGeneral.getApiUsername(),
                                                     ConstantsGeneral.getApiPassword())
        )
        
        if response.status_code == 200:
            data = response.json()
            log.info(f"Data fetched successfully: {data}")
            
            # Extract relevant data
            statusData = data.get('data', [])[0] if data.get('data') else {}

            driveData = statusData.get('driver', {})
            fuelData = statusData.get('fuel', {})
            electricData = statusData.get('electric', {})
            locationData = statusData.get('location', {})

            vehicleData.append({
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'vehicle_id': statusData.get('vehicle_id'),
                'registration': statusData.get('registration'),
                'engine_type': statusData.get('engine_type'),
                'chassis_number': statusData.get('chassis_number'),
                'event_ts': statusData.get('event_ts'),
                'bearing': statusData.get('bearing'),
                'speed': statusData.get('speed'),
                'ignition': statusData.get('ignition'),
                'idling': statusData.get('idling'),
                'odometer': statusData.get('odometer'),
                'clock': statusData.get('clock'),
                'altitude': statusData.get('altitude'),
                'rpm': statusData.get('rpm'),
                'road_speed': statusData.get('road_speed'),
                'vext': statusData.get('vext'),
                'temp1': statusData.get('temp1'),
                'temp2': statusData.get('temp2'),
                'temp3': statusData.get('temp3'),
                'temp4': statusData.get('temp4'),
                'last_identification_tag_id': statusData.get('last_identification_tag_id'),
                'io_panic': statusData.get('io_panic'),
                'io_disarm': statusData.get('io_disarm'),
                'dynamic1': statusData.get('dynamic1'),
                'dynamic2': statusData.get('dynamic2'),
                'dynamic3': statusData.get('dynamic3'),
                'dynamic4': statusData.get('dynamic4'),
                'input_state': statusData.get('input_state'),
                'input_state2': statusData.get('input_state2'),
                'input_state3': statusData.get('input_state3'),
                'central_locking_status': statusData.get('central_locking_status'),
                'tcu_battery_percentage': statusData.get('tcu_battery_percentage'),
                
                # Driver information
                'driver_id': driveData.get('driver_id'),
                'driver_first_name': driveData.get('first_name'),
                'driver_last_name': driveData.get('last_name'),
                'driver_id_number': driveData.get('id_number'),
                'driver_license_number': driveData.get('license_number'),
                'driver_tag_id': driveData.get('tag_id'),
                'driver_phone_number': driveData.get('phone_number'),
                
                # Fuel information
                'fuel_updated': fuelData.get('updated'),
                'fuel_level': fuelData.get('level'),
                'fuel_percentage_left': fuelData.get('precentage_left'),
                'fuel_total_consumed': fuelData.get('total_consumed'),
                
                # Electric information
                'battery_percentage_left': electricData.get('battery_percentage_left'),
                'battery_ts': electricData.get('battery_ts'),
                
                # Location information
                'location_updated': locationData.get('updated'),
                'longitude': locationData.get('longitude'),
                'latitude': locationData.get('latitude'),
                'gps_fix_type': locationData.get('gps_fix_type'),
                'position_description': locationData.get('position_description'),
                'geofence_ids': ','.join(locationData.get('geofence_ids', []))
            })
        else:
            log.error(f"Error fetching data. Status code: {response.status_code}")
            log.error(f"Response: {response.text}")
            
    except Exception as e:
        log.error(f"Exception occurred: {str(e)}")

def exportToExcel():
    if vehicleData:
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        df = pd.DataFrame(vehicleData)
        output_file = f"D:/New/Programming/export/{timestamp}_VEHICLE-STATUS_{registration}.xlsx"
        df.to_excel(output_file, index=False)
        log.info(f"Data exported to: {output_file}")

def main():
    log.info("Starting vehicle status monitoring...")
    try:
        while True:
            fetchVehicleStatus()
            time.sleep(30)  # Wait for 10 seconds
    except KeyboardInterrupt:
        log.info("Monitoring stopped by user")
        exportToExcel()  # Final export before exit

if __name__ == "__main__":
    main()