from ..models import *
from django.db.models import Q

class fixturesServicio():

    def fixturePorID(self, id):
        return Fixture.objects.get(IdApiFixture_id=id)
    
    def fixturesPorCompetencia(self, competencia):
        return Fixture.objects.filter(IdApiComp=competencia).exclude(Status__in=["Match Finished", "Technical Loss", "Match Postponed"]).order_by('Fecha', 'Hora')
    
    def fixturesPorEquipo(self, id):
        return Fixture.objects.filter(Q(IdEquipoLocal_id = id) | Q(IdEquipoVisitante_id=id)).order_by('Fecha', 'Hora')
    
    def actualizarFixtures(self, response):
        for i in range(len(response)):
            texto = response[i]['fixture']['date']
            horarios = Fixture.calcularHorarioArgentino(texto)

            # calcularHorarioArgentino devuelve una lista con la fecha en [0] y el horario en [1]

            datestr = horarios[0]
            timestr = horarios[1]
            
            try:
                Fixture.objects.get(IdApiFixture_id=response[i]['fixture']['id'])
                Fixture.objects.filter(IdApiFixture_id=response[i]['fixture']['id']).update(Arbitro=response[i]['fixture']['referee'],Fecha=datestr,Hora=timestr,IdApiEstadio_id=response[i]['fixture']['venue']['id'],Status=response[i]['fixture']['status']['long'])
            except:
                Fixture.objects.create(
                    IdApiComp_id=response[i]['league']['id'],
                    IdApiFixture_id=response[i]['fixture']['id'],
                    Arbitro=response[i]['fixture']['referee'],
                    Fecha=datestr,
                    Hora=timestr,
                    IdApiEstadio_id=response[i]['fixture']['venue']['id'],
                    IdEquipoLocal_id=response[i]['teams']['home']['id'],
                    IdEquipoVisitante_id=response[i]['teams']['away']['id'],
                    Status=response[i]['fixture']['status']['long'])    

class FixtureIndex():
    def __init__(self, fixture, aplocal, apemp, apvis, predict):
        self.fixture = fixture
        self.aplocal = aplocal
        self.apemp = apemp
        self.apvis = apvis
        self.predict = predict
