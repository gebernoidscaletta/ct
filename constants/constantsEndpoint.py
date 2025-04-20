class ConstantsEndpoint:
    _GEOFENCE_INSERT = "/geofences"
    _GEOFENCE_RETRIEVE_GROUPS = "/geofences/groups"

    @staticmethod
    def geofenceInsert():
        return ConstantsEndpoint._GEOFENCE_INSERT
    
    @staticmethod
    def geofenceRetrieveAllGroups():
        return ConstantsEndpoint._GEOFENCE_RETRIEVE_GROUPS