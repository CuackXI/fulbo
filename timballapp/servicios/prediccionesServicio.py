from ..models import *

class prediccionesServicio():

    def predictsPorFixture(self, id):
        query = f'SELECT id, IdApiApuesta_id, MAX(Porcentaje) from timballapp_apuesta where IdApiFixture_id = {id} group by IdApiApuesta_id'
        return Apuesta.objects.raw(query)
    
    def predictsResultado(self, fixture):
        apuestas = Apuesta.objects.filter(IdApiApuesta = 1, IdApiFixture_id = fixture.IdApiFixture_id)
        print(apuestas)
        return apuestas