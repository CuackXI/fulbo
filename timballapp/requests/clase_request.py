import requests

class Request():
    def __init__(self, url, querystring, headers):
        self.url = url
        self.querystring = querystring
        self.headers = headers  

    def request_response(self, url, querystring, headers):
        if querystring != None:
            response = requests.get(url, headers=headers)
        else:
            response = requests.get(url, headers=headers, params=querystring)

        response = response.json()

        return response