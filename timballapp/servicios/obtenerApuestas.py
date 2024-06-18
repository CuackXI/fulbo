from ..models import *

class obtenerApuestas():
    def obtenerApuestas(self):
        return Apuesta.objects.all()