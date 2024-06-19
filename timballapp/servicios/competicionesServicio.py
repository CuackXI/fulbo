from ..models import *

class competicionesServicio():

    def crearCompeticiones(self, response):
        for i in range(len(response['response'])):
            Competiciones.objects.create(
            IdApiComp=response['response'][i]['league']['id'],
            Nombre=response['response'][i]['league']['name'],
            Image_URL=response['response'][i]['league']['logo'],
            Temporada=2024,
            Pais=response['response'][i]['country']['name'])