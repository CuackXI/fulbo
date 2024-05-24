from ..models import *

class Obtener_Apuestas():
    def Obtener_Apuestas(self):
        return Apuesta.objects.all()