from ..models import *

class fixturesPorCompetencia():
    def fixturesPorCompetencia(self, competencia):
        return Fixture.objects.filter(IdApiComp=competencia).exclude(Status__in=["Match Finished", "Technical Loss"]).order_by('Fecha', 'Hora')