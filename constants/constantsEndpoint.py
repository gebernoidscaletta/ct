class ConstantsEndpoint:
    _GEOFENCE = "/geofences"
    _GEOFENCE_GROUPS = "/geofences/groups"

    @staticmethod
    def getGeofenceEndpoint():
        return ConstantsEndpoint._GEOFENCE
    
    @staticmethod
    def getgGeofenceGroupsEndpoint():
        return ConstantsEndpoint._GEOFENCE_GROUPS