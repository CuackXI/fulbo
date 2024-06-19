from ..models import *
from django.db.models import Q

class equiposServicio():
    
    def equipoPorID(self, id):
        return Equipo.objects.get(IdApiEquipo_id = id)
    
    def realizarBusqueda(self, query):
        return Equipo.objects.filter(Q(Nombre__icontains=query))
    
    def crearEquipos(self, response, competencia):
        for i in range(len(response['response'])):
            Equipo.objects.create(
                IdApiEquipo=response['response'][i]['team']['id'],
                IdApiComp=competencia,
                Nombre=response['response'][i]['team']['name'],
                IdApiEstadio=response['response'][i]['venue']['id'],
                Pais=response['response'][i]['team']['country'],
                Image_URL=response['response'][i]['team']['logo'],
                Fundacion=response['response'][i]['team']['founded']
            )