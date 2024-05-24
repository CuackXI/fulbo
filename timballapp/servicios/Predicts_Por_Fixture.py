from ..models import *
from django.db.models import Max

class Predicts_Por_Fixture():
    def Predicts_Por_Fixture(self, id):
        query = f'SELECT id, IdApiApuesta_id, MAX(Porcentaje) from timballapp_apuesta where IdApiFixture_id = {id} group by IdApiApuesta_id'
        return Apuesta.objects.raw(query)