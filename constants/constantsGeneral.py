class ConstantsGeneral:
    _API_USERNAME = "BAHA00004"
    _API_PASSWORD = "9328ccf602f78bfdabef61a6f0d748f35559346bac09f49f94c41284240f8e4a"
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