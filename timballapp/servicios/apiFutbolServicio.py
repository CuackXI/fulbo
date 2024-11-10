import requests
from key import secret_key

class apiFutbolServicio():
    def __init__(self):
        self.__url = ""
        self.__querystring = {}
        self.__headers = secret_key

    # Headers

    @property
    def headers(self):
        return self.__headers
    
    # Url

    @property
    def url(self):
        return self.__url
    
    def __set_url(self, url):
        if type(url) == str:
            self.__url = url

    # Querystring (parametros)

    @property
    def querystring(self):
        return self.__querystring
    
    def __set_querystring(self, key, parametro):
        self.__querystring[key] = parametro

    # Respuesta

    @property
    def Respuesta(self):
        response = requests.get(self.url, headers=self.headers, params=self.querystring)
        response = response.json()
        return response['response']
    
    # Requests

    def Paises(self):
        self.__set_url("https://api-football-v1.p.rapidapi.com/v3/countries")

        return self.Respuesta
    
    def EquiposEstadios(self, competencia):
        self.__set_url("https://api-football-v1.p.rapidapi.com/v3/teams")

        self.__set_querystring('league', str(competencia))
        self.__set_querystring('season', "2024")

        return self.Respuesta
        
    def Competiciones(self, pais):
        self.__set_url("https://api-football-v1.p.rapidapi.com/v3/leagues")

        self.__set_querystring('country', str(pais))

        return self.Respuesta

    def Fixtures(self, liga, inicio = None, fin = None):
        self.__set_url("https://api-football-v1.p.rapidapi.com/v3/fixtures")

        self.__set_querystring('league', str(liga))
        self.__set_querystring('season', "2024")

        if inicio != None and fin != None:
            self.__set_querystring('from', str(inicio))
            self.__set_querystring('to', str(fin))

        return self.Respuesta
    
    def Bookmakers(self):
        self.__set_url("https://api-football-v1.p.rapidapi.com/v3/odds/bookmakers")

        return self.Respuesta
    
    def Apuestas(self, liga, page):
        self.__set_url("https://api-football-v1.p.rapidapi.com/v3/odds")

        self.__set_querystring('league', str(liga))
        self.__set_querystring('page', page)
        self.__set_querystring('season', "2024")
        self.__set_querystring('bookmaker', 26)

        return self.Respuesta
    
    def Jugadores(self, equipo):
        self.__set_url("https://api-football-v1.p.rapidapi.com/v3/players/squads")

        self.__set_querystring('team', equipo)

        return self.Respuesta
    
    def tipoApuestas(self):
                
        self.__set_url("https://api-football-v1.p.rapidapi.com/v3/odds/bets")

        return self.Respuesta
    
    def equipoEstadisticas(self, equipo):
        self.__set_url("https://api-football-v1.p.rapidapi.com/v3/teams/statistics")

        self.__set_querystring('league', 128)
        self.__set_querystring('season', 2024)
        self.__set_querystring('team', equipo)

        return self.Respuesta