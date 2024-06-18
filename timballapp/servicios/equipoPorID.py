from ..models import *

class equipoPorID():
    def equipoPorID(self, id):
        return Equipo.objects.get(IdApiEquipo_id = id)