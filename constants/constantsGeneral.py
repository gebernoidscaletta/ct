class ConstantsGeneral:
    _API_USERNAME = "CART00013"
    _API_PASSWORD = "13f582b1290c43a1a548a4f104d3002444dd5a1a30264209f93731629106356e"
    _INDONESIA_BASE_URL = "https://fleetapi-id.cartrack.com/rest"
    _THAILAND_BASE_URL = "https://fleetapi-th.cartrack.com/rest"
    _MALAYSIA_BASE_URL = "https://fleetapi-my.cartrack.com/rest"
    _SINGAPORE_BASE_URL = "https://fleetapi-sg.cartrack.com/rest"

    @staticmethod
    def getApiUsername():
        return ConstantsGeneral._API_USERNAME
    
    @staticmethod
    def getApiPassword():
        return ConstantsGeneral._API_PASSWORD

    @staticmethod
    def getIndonesiaBaseUrl():
        return ConstantsGeneral._INDONESIA_BASE_URL
    
    @staticmethod
    def getThailandBaseUrl():
        return ConstantsGeneral._THAILAND_BASE_URL
    
    @staticmethod
    def getMalaysiaBaseUrl():
        return ConstantsGeneral._MALAYSIA_BASE_URL
    
    @staticmethod
    def getSingaporeBaseUrl():
        return ConstantsGeneral._SINGAPORE_BASE_URL