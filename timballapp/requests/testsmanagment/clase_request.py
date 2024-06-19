import requests

class ApiFutbolServicio():
    def __init__(self):
        self.__url = ""
        self.__querystring = {}
        self.__headers = {"X-RapidAPI-Key": "36d0515859mshc128509052fcf97p1484c4jsn6f58a0e1bbb7", "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com", "Content-Type": "application/json"}  

    # Headers

    @property
    def headers(self):
        return self.__headers
    
    # Url

    @property
    def url(self):
        return self.__url
    
    @url.setter
    def url(self, url):
        if type(url) == str:
            self.__url = url

    # Querystring

    @property
    def querystring(self):
        return self.__querystring
    
    @querystring.setter
    def querystring(self, querystring):
        if type(querystring) == dict:
            self.__querystring = querystring

    def Paises(self):
        self.url = "https://api-football-v1.p.rapidapi.com/v3/countries"
        self.querystring = None
        response = requests.get(self.url, headers=self.headers, params=self.querystring)
        response = response.json()
        return response['response']
    
    def Equipos(self, competencia = None):
        if competencia != None:
            self.url = "https://api-football-v1.p.rapidapi.com/v3/teams"

            self.querystring['league'] = str(competencia)
            self.querystring['season'] = "2024"

            response = requests.get(self.url, headers=self.headers, params=self.querystring)
            response = response.json()
            return response['response']
        else:
            return "Ingresa una competencia para hacer el request"