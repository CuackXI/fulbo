from ..models import Fixture

class Fixtures_Jugados():
    def obtener_por_competencia_y_status(self, id_competencia, Status):
        return Fixture.objects.filter(IdApiComp=id_competencia, Status=Status)