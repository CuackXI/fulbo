from ..models import *

class jugadoresPorEquipo():
    def jugadoresPorEquipo(self, id):
        return Jugador.objects.filter(IdApiEquipo_id = id).order_by("Posicion")