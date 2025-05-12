from constants.constantsEndpoint import ConstantsEndpoint
from util.utilLogging import Log

log = Log()

class General:

    infoClass = ""

    @staticmethod
    def endpointChecker(endpoint):

        if endpoint == ConstantsEndpoint.getAlertEndpoint():
            infoClass = "alertEndpoint"
            log.info("[ALERT]")

        elif endpoint == ConstantsEndpoint.getAlertGeofencesEndpoint():
            infoClass = "alertGeofence"
            log.info("[ALERT GEOFENCE]")

        elif endpoint == ConstantsEndpoint.getAlertIgnitionEndpoint():
            infoClass = "alertIgnition"
            log.info("[ALERT IGNITION]")

        elif endpoint == ConstantsEndpoint.getAlertNotificationEndpoint():
            infoClass = "alertNotification"
            log.info("[ALERT NOTIFICATION]")

        elif endpoint == ConstantsEndpoint.getFuelFillsEndpoint():
            infoClass = "fuelFills"
            log.info("[FUEL FILLS]")

        elif endpoint == ConstantsEndpoint.getGeofenceEndpoint():
            infoClass = "geofences"
            log.info("[GEOFENCE]")

        elif endpoint == ConstantsEndpoint.getGeofenceGroupsEndpoint():
            infoClass = "geofenceGroups"
            log.info("[GEOFENCE GROUPS]")

        elif endpoint == ConstantsEndpoint.getVehicleEndpoint():
            infoClass = "vehicles"
            log.info("[VEHICLES]")

        elif endpoint == ConstantsEndpoint.getVehicleGroupsEndpoint():
            infoClass = "vehiclesGroups"
            log.info("[VEHICLES GROUPS]")

        else:
            log.error("Class not found, please check the class again!")
            
        return infoClass