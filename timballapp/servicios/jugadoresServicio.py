from ..models import *

class jugadoresServicio():

    def jugadoresPorEquipo(self, id, limit = None):
        return Jugador.objects.filter(IdApiEquipo_id = id).order_by("Posicion")[:limit]
    
    def crearJugadores(self, jugadores):
        for jugador in jugadores[0]['players']:
            Jugador.objects.create(
                IdApiJugador_id = jugador['id'],
                Nombre = jugador['name'],
                Edad = jugador['age'],
                Numero = jugador['number'],
                IdApiEquipo_id = jugadores[0]['team']['id'],
                Posicion = jugador['position'],
                Image_URL = jugador['photo']
            )