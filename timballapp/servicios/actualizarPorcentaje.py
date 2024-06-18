from ..models import *

class actualizarPorcentaje():
    def actualizarPorcentaje(self, porcentajes, apuestas):
        for apuesta in apuestas:
            Apuesta.objects.filter(id=apuesta.id).update(Porcentaje=porcentajes[apuesta.id-1])