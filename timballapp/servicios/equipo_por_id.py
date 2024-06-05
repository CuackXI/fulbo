from ..models import *

class equipo_por_id():
    def equipo_por_id(self, id):
        return Equipo.objects.get(IdApiEquipo_id = id)