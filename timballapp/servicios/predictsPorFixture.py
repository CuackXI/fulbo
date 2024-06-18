from ..models import *
from django.db.models import Max

class predictsPorFixture():
    def predictsPorFixture(self, id):
        query = f'SELECT id, IdApiApuesta_id, MAX(Porcentaje) from timballapp_apuesta where IdApiFixture_id = {id} group by IdApiApuesta_id'
        return Apuesta.objects.raw(query)