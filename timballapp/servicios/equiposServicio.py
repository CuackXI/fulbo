from ..models import *
from django.db.models import Q

class equiposServicio():
    
    def equipoPorID(self, id):
        return Equipo.objects.get(IdApiEquipo_id = id)
    
    def realizarBusqueda(self, query):
        return Equipo.objects.filter(Q(Nombre__icontains=query))
    
    def obtenerEquiposPorCompetencia(self, competencia):
        return Equipo.objects.filter(IdApiComp = competencia)
    
    def crearEquipos(self, response, competencia):
        for i in range(len(response['response'])):
            Equipo.objects.create(
                IdApiEquipo=response['response'][i]['team']['id'],
                IdApiComp=competencia,
                Nombre=response['response'][i]['team']['name'],
                IdApiEstadio=response['response'][i]['venue']['id'],
                Pais=response['response'][i]['team']['country'],
                Image_URL=response['response'][i]['team']['logo'],
                Fundacion=response['response'][i]['team']['founded']
            )

    def obtenerPosicionDeUnEquipo(self, equipo):
        stats_equipo = self.obtenerEstadisticasPorEquipo(equipo)

        ranked_teams = (
            StatsEquipo.objects.all()
            .order_by(
                '-Puntos',
                '-DiferenciaGoles',
                '-GolesFavor',
                'GolesContra'
            )
        )

        for position, stat in enumerate(ranked_teams, start=1):
            if stat.IdApiEquipo_id == equipo:
                return position

    def actualizarEstadisticasEquipo(self, response, equipo):
        try:
            StatsEquipo.objects.get(IdApiEquipo_id=equipo) #Except
            StatsEquipo.objects.filter(IdApiEquipo_id=equipo).update(
            IdApiEquipo_id = equipo,
            GolesFavor = response['goals']['for']['total']['total'],
            GolesFavorLocal= response['goals']['for']['total']['home'],
            GolesFavorVisitante=response['goals']['for']['total']['away'],
            GolesContra=response['goals']['against']['total']['total'],
            GolesContraLocal=response['goals']['against']['total']['home'],
            GolesContraVisitante=response['goals']['against']['total']['away'],
            DiferenciaGoles=response['goals']['for']['total']['total'] - response['goals']['against']['total']['total'],
            PartidosJugados=response['fixtures']['played']['total'],
            PartidosGanados=response['fixtures']['wins']['total'],
            PartidosPerdidos=response['fixtures']['loses']['total'],
            PartidosEmpatados=response['fixtures']['draws']['total'],
            Puntos=int(response['fixtures']['wins']['total'])*3+int(response['fixtures']['draws']['total']),
            PuntosLocal=int(response['fixtures']['wins']['home'])*3+int(response['fixtures']['draws']['home']),
            PuntosVisitante=int(response['fixtures']['wins']['away'])*3+int(response['fixtures']['draws']['away']),
            PartidosGanadosLocal=response['fixtures']['wins']['home'],
            PartidosPerdidosLocal=response['fixtures']['loses']['home'],
            PartidosEmpatadosLocal=response['fixtures']['draws']['home'],
            PartidosGanadosVisitante=response['fixtures']['wins']['away'],
            PartidosEmpatadosVisitante=response['fixtures']['draws']['away'],
            PartidosPerdidosVisitante=response['fixtures']['loses']['away'],
            SinGoles=response['clean_sheet']['total'],
            SinGolesLocal=response['clean_sheet']['home'],
            SinGolesVisitante=response['clean_sheet']['away'],
            Penales=response['penalty']['total']
            )

        except:
            StatsEquipo.objects.create(
                IdApiEquipo_id = equipo,
                GolesFavor = response['goals']['for']['total']['total'],
                GolesFavorLocal= response['goals']['for']['total']['home'],
                GolesFavorVisitante=response['goals']['for']['total']['away'],
                GolesContra=response['goals']['against']['total']['total'],
                GolesContraLocal=response['goals']['against']['total']['home'],
                GolesContraVisitante=response['goals']['against']['total']['away'],
                DiferenciaGoles=response['goals']['for']['total']['total'] - response['goals']['against']['total']['total'],
                PartidosJugados=response['fixtures']['played']['total'],
                PartidosGanados=response['fixtures']['wins']['total'],
                PartidosPerdidos=response['fixtures']['loses']['total'],
                PartidosEmpatados=response['fixtures']['draws']['total'],
                Puntos=int(response['fixtures']['wins']['total'])*3+int(response['fixtures']['draws']['total']),
                PuntosLocal=int(response['fixtures']['wins']['home'])*3+int(response['fixtures']['draws']['home']),
                PuntosVisitante=int(response['fixtures']['wins']['away'])*3+int(response['fixtures']['draws']['away']),
                PartidosGanadosLocal=response['fixtures']['wins']['home'],
                PartidosPerdidosLocal=response['fixtures']['loses']['home'],
                PartidosEmpatadosLocal=response['fixtures']['draws']['home'],
                PartidosGanadosVisitante=response['fixtures']['wins']['away'],
                PartidosEmpatadosVisitante=response['fixtures']['draws']['away'],
                PartidosPerdidosVisitante=response['fixtures']['loses']['away'],
                SinGoles=response['clean_sheet']['total'],
                SinGolesLocal=response['clean_sheet']['home'],
                SinGolesVisitante=response['clean_sheet']['away'],
                Penales=response['penalty']['total'],
                PenalesMetidos = response['penalty']['scored']['total'],
                PenalesErrados = response['penalty']['missed']['total'],
            )

    def obtenerEstadisticasPorEquipo(self, equipo):
        return StatsEquipo.objects.get(IdApiEquipo_id = equipo.IdApiEquipo_id)

class EquipoConPosicion:
    def __init__(self, stats, posicion, equipo) -> None:
        self.stat = stats
        self.posicion = posicion
        self.equipo = equipo