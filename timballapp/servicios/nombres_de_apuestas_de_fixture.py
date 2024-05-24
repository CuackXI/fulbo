from ..models import *

class nombres_de_apuestas_de_fixture():
    def nombres_de_apuestas_de_fixture(self, fixture):
        return ApiApuestas.objects.filter(apuesta__IdApiFixture_id=fixture.IdApiFixture_id).distinct()