class ConstantsEndpoint:
    _GEOFENCE = "/geofences"
    _GEOFENCE_GROUPS = "/geofences/groups"
    _ALERT = "/alerts"
    _ALERT_IGNITION = "/alerts/ignition"
    _ALERT_GEOFENCES = "/alerts/geofences"
    _ALERT_NOTIFICATION = "/alerts/notifications"
    _ALERT_NOTIFICATION_TYPES = "/alert/notifications/types"
    _FUEL_CONSUMED = "/fuel/consumed"
    _FUEL_FILLS = "/fuel/fills"
    _FUEL_LEVEL = "/fuel/level"
    _FUEL_LEVEL_HISTORY = "/fuel/level/history"
    _VEHICLES = "/vehicles"
    _VEHICLES_GROUPS = "/vehicles/groups"

    @staticmethod
    def getGeofenceEndpoint():
        return ConstantsEndpoint._GEOFENCE
    
    @staticmethod
    def getGeofenceGroupsEndpoint():
        return ConstantsEndpoint._GEOFENCE_GROUPS
    
    @staticmethod
    def getAlertEndpoint():
        return ConstantsEndpoint._ALERT
    
    @staticmethod
    def getAlertIgnitionEndpoint():
        return ConstantsEndpoint._ALERT_IGNITION

    @staticmethod
    def getAlertGeofencesEndpoint():
        return ConstantsEndpoint._ALERT_GEOFENCES
    
    @staticmethod
    def getAlertNotificationEndpoint():
        return ConstantsEndpoint._ALERT_NOTIFICATION
    
    @staticmethod
    def getFuelConsumedEndpoint():
        return ConstantsEndpoint._FUEL_CONSUMED
    
    @staticmethod
    def getFuelFillsEndpoint():
        return ConstantsEndpoint._FUEL_FILLS
    
    @staticmethod
    def getFuelLevelEndpoint():
        return ConstantsEndpoint._FUEL_LEVEL
    
    @staticmethod
    def getFuelLevelHistoryEndpoint():
        return ConstantsEndpoint._FUEL_LEVEL_HISTORY
    
    @staticmethod
    def getVehicleEndpoint():
        return ConstantsEndpoint._VEHICLES
    
    @staticmethod
    def getVehicleGroupsEndpoint():
        return ConstantsEndpoint._VEHICLES_GROUPS