from ..models import *

class apuestasPorFixture():
    def apuestasPorFixture(self, id):
        return Apuesta.objects.filter(IdApiFixture_id=id)