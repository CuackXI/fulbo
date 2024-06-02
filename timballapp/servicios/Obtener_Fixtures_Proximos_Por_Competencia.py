from ..models import *

class Obtener_Fixtures_Proximos_Por_Competencia():
    def Obtener_Fixtures_Proximos_Por_Competencia(self, competencia):
        return Fixture.objects.filter(IdApiComp=competencia).exclude(Status__in=["Match Postponed", "Match Finished", "Technical Loss", "WalkOver", "Time to be defined"]).order_by('Fecha', 'Hora')