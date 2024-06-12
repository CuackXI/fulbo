import requests

class Request():
    def __init__(self, url, querystring):
        self.url = url
        self.querystring = querystring
        self.__headers = {"X-RapidAPI-Key": "36d0515859mshc128509052fcf97p1484c4jsn6f58a0e1bbb7", "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com", "Content-Type": "application/json"}  

    @property
    def headers(self):
        return self.__headers


    def hacer_request(self):
        response = requests.get(self.url, headers=self.headers, params=self.querystring)

        response = response.json()

        return response