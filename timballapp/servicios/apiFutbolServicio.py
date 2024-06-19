import requests

class apiFutbolServicio():
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

    # Querystring (parametros)

    @property
    def querystring(self):
        return self.__querystring
    
    @querystring.setter
    def querystring(self, querystring):
        if type(querystring) == dict:
            self.__querystring = querystring

    # Respuesta

    @property
    def Respuesta(self):
        response = requests.get(self.url, headers=self.headers, params=self.querystring)
        response = response.json()
        return response['response']
    
    # Requests

    def Paises(self):
        self.url = "https://api-football-v1.p.rapidapi.com/v3/countries"
        self.querystring = None

        return self.Respuesta
    
    def EquiposEstadios(self, competencia):
        self.url = "https://api-football-v1.p.rapidapi.com/v3/teams"

        self.querystring['league'] = str(competencia)
        self.querystring['season'] = "2024"

        return self.Respuesta
        
    def Competiciones(self, pais):
        self.url = "https://api-football-v1.p.rapidapi.com/v3/leagues"

        self.querystring['country'] = str(pais)

        return self.Respuesta

    def Fixtures(self, liga, inicio = None, fin = None):
        self.url = "https://api-football-v1.p.rapidapi.com/v3/fixtures"

        self.querystring['league'] = str(liga)
        self.querystring['season'] = "2024"

        if inicio != None and fin != None:
            self.querystring['from'] = str(inicio)
            self.querystring['to'] = str(fin)

        return self.Respuesta
    
    def Bookmakers(self):
        self.url = "https://api-football-v1.p.rapidapi.com/v3/odds/bookmakers"

        return self.Respuesta
    
    def Apuestas(self, liga, page):
        self.url = "https://api-football-v1.p.rapidapi.com/v3/odds"

        self.querystring['league'] = str(liga)
        self.querystring['page'] = page
        self.querystring['season'] = "2024"
        self.querystring['bookmaker'] = 26

        return self.Respuesta
    
    def tipoApuestas(self):
                
        self.url = "https://api-football-v1.p.rapidapi.com/v3/odds/bets"

        return self.Respuesta