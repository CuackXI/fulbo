from ..models import *

class Actualizar_Porcentajes():
    def Actualizar_Porcentajes(self, porcentajes, apuestas):
        for apuesta in apuestas:
            Apuesta.objects.filter(id=apuesta.id).update(Porcentaje=porcentajes[apuesta.id-1])