from ..models import *
from django.db.models import Q

class fixturesServicio():

    def fixturePorID(self, id):
        return Fixture.objects.get(IdApiFixture_id=id)
    
    def fixturesPorCompetencia(self, competencia):
        return Fixture.objects.filter(IdApiComp=competencia).exclude(Status__in=["Match Finished", "Technical Loss"]).order_by('Fecha', 'Hora')
    
    def fixturesPorEquipo(self, id):
        return Fixture.objects.filter(Q(IdEquipoLocal_id = id) | Q(IdEquipoVisitante_id=id)).order_by('Fecha', 'Hora')
    
    def actualizarFixtures(self, response):
        for i in range(len(response['response'])):
            texto = response['response'][i]['fixture']['date']
            horarios = Fixture.calcularHorarioArgentino(texto)

            # calcularHorarioArgentino devuelve una lista con la fecha en [0] y el horario en [1]

            datestr = horarios[0]
            timestr = horarios[1]
            
            try:
                Fixture.objects.get(IdApiFixture_id=response['response'][i]['fixture']['id'])
                Fixture.objects.filter(IdApiFixture_id=response['response'][i]['fixture']['id']).update(Arbitro=response['response'][i]['fixture']['referee'],Fecha=datestr,Hora=timestr,IdApiEstadio_id=response['response'][i]['fixture']['venue']['id'],Status=response['response'][i]['fixture']['status']['long'])
            except:
                print("create")
                Fixture.objects.create(
                    IdApiComp_id=response['response'][i]['league']['id'],
                    IdApiFixture_id=response['response'][i]['fixture']['id'],
                    Arbitro=response['response'][i]['fixture']['referee'],
                    Fecha=datestr,
                    Hora=timestr,
                    IdApiEstadio_id=response['response'][i]['fixture']['venue']['id'],
                    IdEquipoLocal_id=response['response'][i]['teams']['home']['id'],
                    IdEquipoVisitante_id=response['response'][i]['teams']['away']['id'],
                    Status=response['response'][i]['fixture']['status']['long'])