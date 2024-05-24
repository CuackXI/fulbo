from ..models import *

class Apuestas_Por_Fixture():
    def Apuestas_Por_Fixture(self, id):
        return Apuesta.objects.filter(IdApiFixture_id=id)