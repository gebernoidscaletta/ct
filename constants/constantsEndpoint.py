class ConstantsEndpoint:
    _GEOFENCE = "/geofences"
    _GEOFENCE_GROUPS = "/geofences/groups"
    _ALERT_NOTIFICATION = "/alerts/notifications"

    @staticmethod
    def getGeofenceEndpoint():
        return ConstantsEndpoint._GEOFENCE
    
    @staticmethod
    def getGeofenceGroupsEndpoint():
        return ConstantsEndpoint._GEOFENCE_GROUPS
    
    @staticmethod
    def getAlertNotificationEndpoint():
        return ConstantsEndpoint._ALERT_NOTIFICATION