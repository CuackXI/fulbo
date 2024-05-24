from ..models import *

class nombres_de_apuestas_de_fixture():
    def nombres_de_apuestas_de_fixture(self, fixture):
        query = "SELECT DISTINCT timballapp_apiapuestas.IdApiApuesta from timballapp_apiapuestas join timballapp_apuesta on timballapp_apiapuestas.IdApiApuesta = timballapp_apuesta.IdApiApuesta_id where timballapp_apiapuestas.IdApiApuesta = timballapp_apuesta.IdApiApuesta_id"
        return ApiApuestas.objects.raw(query)