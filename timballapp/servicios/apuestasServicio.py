from ..models import *
from django.db.models import Q

class apuestasServicio():

    def actualizarPorcentaje(self, porcentajes, apuestas):
        for apuesta in apuestas:
            Apuesta.objects.filter(id=apuesta.id).update(Porcentaje=porcentajes[apuesta.id-1])

    def apuestasPorFixture(self, id):
        return Apuesta.objects.filter(IdApiFixture_id=id)
    
    def crearTiposApuesta(self, response):
        for i in range(len(response['response'])):
            print(response['response'][i]['id'])
            print(response['response'][i]['name'])

    def actualizarApuestas(self, response):
        for i in range(len(response)):
            for b in range(len(response[i]['bookmakers'])):
                for y in response[i]['bookmakers'][b]['bets']:
                    for x in y['values']:
                        try:
                            Apuesta.objects.get(IdApiFixture_id=response[i]['fixture']['id'], IdApiApuesta_id=y['id'], Tipo=x['value'])
                        except:
                            Apuesta.objects.create(
                                IdApiFixture_id=response[i]['fixture']['id'],
                                IdApiBookmaker_id=response[i]['bookmakers'][b]['id'],
                                IdApiApuesta_id=y['id'],
                                Tipo=x['value'],
                                Multiplicador=x['odd'],
                                Porcentaje = -1
                            )
    
    def generarPorcentajes(self, apuestas):
        id = 0
        multiplicadores = []
        porcentajes = []
        cant_apuestas = len(apuestas)
        for apuesta in apuestas:
            if id != apuesta.IdApiApuesta:
                id = apuesta.IdApiApuesta
                if len(multiplicadores) != 1:
                    porcentajes_t = Apuesta.MultiplicadorAPorcentaje(multiplicadores)                       
                    for porcentaje in porcentajes_t:
                        porcentajes.append(porcentaje)
                else:
                    porcentajes.append(0)
                multiplicadores = []
            multiplicadores.append(apuesta.Multiplicador)

        # Caso para el último registro que por alguna razon no lo toma el for
        ultima_apuesta = Apuesta.objects.get(id = cant_apuestas)
        multiplicadores.pop(-1)
        multiplicadores.append(ultima_apuesta.Multiplicador)
        if len(multiplicadores) != 1:
            porcentajes_t = Apuesta.MultiplicadorAPorcentaje(multiplicadores)                       
            for porcentaje in porcentajes_t:
                porcentajes.append(porcentaje)
        else:
            porcentajes.append(0)

        return porcentajes
    
    def obtenerApuestas(self):
        return Apuesta.objects.all()
    
    def tiposApuestaPorFixture(self, fixture):
        return ApiApuestas.objects.filter(apuesta__IdApiFixture_id=fixture.IdApiFixture_id).distinct()
    
    def crearBookmakers(self, response):
        for i in range(len(response['response'])):
            Bookmaker.objects.create(
                Bookmaker=response['response'][i]['id'],
                Nombre=response['response'][i]['name']
            )