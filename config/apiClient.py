import requests

class apiClient:

    @staticmethod
    def sendPost (host, headers, request, endpoint):
        response = requests.post(url = host+endpoint,
                                 headers = headers,
                                 json = request)
        return response.json()

    @staticmethod
    def sendPut (host, headers, request, endpoint):
        response = request.put(url = host+endpoint,
                                 headers = headers,
                                 json = request)
        return response.json()
    
    