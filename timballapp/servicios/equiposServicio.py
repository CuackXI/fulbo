from ..models import *
from django.db.models import Q

class equiposServicio():
    
    def equipoPorID(self, id):
        return Equipo.objects.get(IdApiEquipo_id = id)
    
    def realizarBusqueda(self, query):
        return Equipo.objects.filter(Q(Nombre__icontains=query))
    
    def obtenerEquiposPorCompetencia(self, competencia):
        return Equipo.objects.filter(IdApiComp = competencia)
    
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

    def obtenerEstadisticasEquipo(self, response):
        respuesta = response['response']
        print(respuesta['goals']['for']['total']['total'])
        print(respuesta['goals']['against']['total'])
        print(respuesta['goals']['for']['total']['total'] - respuesta['goals']['against']['total']['total'])
        print(respuesta['fixtures']['played']['total'])
        print(respuesta['fixtures']['wins']['total'])
        print(respuesta['fixtures']['draws']['total'])
        print(respuesta['fixtures']['loses']['total'])
        print(int(respuesta['fixtures']['wins']['total'])*3+int(respuesta['fixtures']['draws']['total']))
        print(respuesta['fixtures']['wins']['home'])
        print(respuesta['fixtures']['wins']['away'])
        print(respuesta['fixtures']['draws']['home'])
        print(respuesta['fixtures']['draws']['away'])
        print(respuesta['fixtures']['loses']['home'])
        print(respuesta['fixtures']['loses']['away'])
        print(respuesta['goals']['for']['total']['home'])
        print(respuesta['goals']['for']['total']['away'])
        print(respuesta['goals']['against']['total']['home'])
        print(respuesta['goals']['against']['total']['away'])
        print(respuesta['clean_sheet']['total'])
        print(respuesta['clean_sheet']['home'])
        print(respuesta['clean_sheet']['away'])
        print(respuesta['penalties']['total'])
        print(respuesta['penalties']['scored']['total'])
        print(respuesta['penalties']['missed']['total'])