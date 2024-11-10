from ..models import *

class prediccionesServicio():

    def predictsPorFixture(self, id):
        query = f'SELECT id, IdApiApuesta_id, MAX(Porcentaje) from timballapp_apuesta where IdApiFixture_id = {id} group by IdApiApuesta_id'
        return Apuesta.objects.raw(query)
    
    def predictsResultado(self, fixture):
        apuestas = Apuesta.objects.filter(IdApiApuesta = 1, IdApiFixture_id = fixture.IdApiFixture_id)
        return apuestas

    def calcular_probabilidades(self, equipo):
        total_partidos = equipo.PartidosJugados
        prob_ganar = (equipo.PartidosGanados / total_partidos) * 100 if total_partidos > 0 else 0
        prob_perder = (equipo.PartidosPerdidos / total_partidos) * 100 if total_partidos > 0 else 0

        prob_ganar_local = (equipo.PartidosGanadosLocal / 
                            (equipo.PartidosGanadosLocal + equipo.PartidosPerdidosLocal + equipo.PartidosEmpatadosLocal)) * 100 if (equipo.PartidosGanadosLocal + equipo.PartidosPerdidosLocal + equipo.PartidosEmpatadosLocal) > 0 else 0
        prob_perder_local = (equipo.PartidosPerdidosLocal / 
                             (equipo.PartidosGanadosLocal + equipo.PartidosPerdidosLocal + equipo.PartidosEmpatadosLocal)) * 100 if (equipo.PartidosGanadosLocal + equipo.PartidosPerdidosLocal + equipo.PartidosEmpatadosLocal) > 0 else 0

        prob_ganar_visitante = (equipo.PartidosGanadosVisitante / 
                                (equipo.PartidosGanadosVisitante + equipo.PartidosPerdidosVisitante + equipo.PartidosEmpatadosVisitante)) * 100 if (equipo.PartidosGanadosVisitante + equipo.PartidosPerdidosVisitante + equipo.PartidosEmpatadosVisitante) > 0 else 0
        prob_perder_visitante = (equipo.PartidosPerdidosVisitante / 
                                 (equipo.PartidosGanadosVisitante + equipo.PartidosPerdidosVisitante + equipo.PartidosEmpatadosVisitante)) * 100 if (equipo.PartidosGanadosVisitante + equipo.PartidosPerdidosVisitante + equipo.PartidosEmpatadosVisitante) > 0 else 0

        prob_ganar_final = (prob_ganar * 0.6) + (prob_ganar_local * 0.2) + (prob_ganar_visitante * 0.2)
        prob_perder_final = (prob_perder * 0.6) + (prob_perder_local * 0.2) + (prob_perder_visitante * 0.2)
        prob_empatar_final = 100 - (prob_ganar_final + prob_perder_final)

        prob_ganar_final = round(prob_ganar_final, 2)
        prob_perder_final = round(prob_perder_final, 2)
        prob_empatar_final = round(prob_empatar_final, 2)

        return {
            "Gana Local": prob_ganar_final,
            "Empate": prob_empatar_final,
            "Gana Visitante": prob_perder_final
        }

    def calcular_probabilidades_partido(self, equipo_local, equipo_visitante):
        prob_local = self.calcular_probabilidades(equipo_local)
        prob_visitante = self.calcular_probabilidades(equipo_visitante)

        prob_gana_local = prob_local["Gana Local"]
        prob_empate = prob_local["Empate"]
        prob_gana_visitante = prob_visitante["Gana Visitante"]

        total_probabilidades = prob_gana_local + prob_empate + prob_gana_visitante

        if total_probabilidades > 0:
            prob_gana_local_final = (prob_gana_local / total_probabilidades) * 100
            prob_empate_final = (prob_empate / total_probabilidades) * 100
            prob_gana_visitante_final = (prob_gana_visitante / total_probabilidades) * 100
        else:
            prob_gana_local_final = prob_empate_final = prob_gana_visitante_final = 0

        return {
            "Gana Local": round(prob_gana_local_final, 2),
            "Empate": round(prob_empate_final, 2),
            "Gana Visitante": round(prob_gana_visitante_final, 2)
        }

    def comparar_equipos(self, equipo_local_stats, equipo_visitante_stats):
        prob_local = self.calcular_probabilidades(equipo_local_stats)
        prob_visitante = self.calcular_probabilidades(equipo_visitante_stats)

        if prob_local["Empate"] > prob_local["Gana Local"] and prob_local["Empate"] > prob_visitante["Gana Visitante"]:
            resultado = "Alta probabilidad de empate"
        elif prob_local["Gana Local"] > prob_visitante["Gana Visitante"]:
            resultado = "El equipo local tiene mayor probabilidad de ganar"
        else:
            resultado = "El equipo visitante tiene mayor probabilidad de ganar"

        return resultado