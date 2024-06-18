from ..models import *

class generarPorcentajes():
    def generarPorcentajes(self, apuestas):
        id = 0
        multiplicadores = []
        porcentajes = []
        cant_apuestas = len(apuestas)
        print(cant_apuestas)
        for apuesta in apuestas:
            if id != apuesta.IdApiApuesta:
                id = apuesta.IdApiApuesta
                if len(multiplicadores) != 1:
                    porcentajes_t = Apuesta.MultiplicadorAPorcentaje(multiplicadores)                       
                    for porcentaje in porcentajes_t:
                        porcentajes.append(porcentaje)
                else:
                    porcentajes.append(0)
                multiplicadores = []
            multiplicadores.append(apuesta.Multiplicador)

        # Caso para el último registro que por alguna razon no lo toma el for
        ultima_apuesta = Apuesta.objects.get(id = cant_apuestas)
        multiplicadores.pop(-1)
        multiplicadores.append(ultima_apuesta.Multiplicador)
        if len(multiplicadores) != 1:
            porcentajes_t = Apuesta.MultiplicadorAPorcentaje(multiplicadores)                       
            for porcentaje in porcentajes_t:
                porcentajes.append(porcentaje)
        else:
            porcentajes.append(0)

        return porcentajes