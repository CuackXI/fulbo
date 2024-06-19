from ..models import *

class estadiosServicio():
    
    def crearEstadios(self, response):
        for i in range(len(response['response'])):
            Estadio.objects.create(
                IdApiEstadio=response['response'][i]['venue']['id'],
                Nombre=response['response'][i]['venue']['name'],
                Direccion=response['response'][i]['venue']['address'],
                Ciudad=response['response'][i]['venue']['city'],
                Capacidad=response['response'][i]['venue']['capacity'],
                Image_URL=response['response'][i]['venue']['image']
            )