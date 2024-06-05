from ..models import *

class jugadores_por_equipo():
    def jugadores_por_equipo(self, id):
        return Jugador.objects.filter(IdApiEquipo_id = id).order_by("Posicion")