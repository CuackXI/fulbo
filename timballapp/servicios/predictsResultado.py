from ..models import *

class predictsResultado():
    def predictsResultado(self, fixtures):
        apuestas_por_fixture = []
        for fixture in fixtures:
            apuestas = Apuesta.objects.filter(IdApiApuesta = 1, IdApiFixture_id = fixture.IdApiFixture_id)
            apuestas_por_fixture.append(apuestas)
        return apuestas_por_fixture