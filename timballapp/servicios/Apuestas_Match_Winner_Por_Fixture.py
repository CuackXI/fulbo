from ..models import *

class Apuestas_Match_Winner_Por_Fixture():
    def Apuestas_Match_Winner_Por_Fixture(self, competencia, fixtures):
        apuestas_por_fixture = []
        for fixture in fixtures:
            apuestas = Apuesta.objects.filter(IdApiApuesta = 1, IdApiFixture_id = fixture.IdApiFixture_id)
            apuestas_por_fixture.append(apuestas)
        return apuestas_por_fixture