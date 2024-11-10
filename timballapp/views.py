from django.shortcuts import render, redirect
from .servicios.apuestasServicio import *
from .servicios.prediccionesServicio import *
from .servicios.fixturesServicio import *
from .servicios.equiposServicio import * 
from .servicios.jugadoresServicio import *
from .servicios.estadiosServicio import * 
from .servicios.competicionesServicio import *
from .servicios.apiFutbolServicio import *
from .models import *
from .forms import *
from django.urls import reverse

# Create your views here.

def index(request):
    if request.method == 'GET':
        servicio = fixturesServicio()
        fixtures = servicio.fixturesPorCompetencia(128)
        fixturesReal = []

        for fixture in fixtures:
            servicio = prediccionesServicio()

            servicio_estadisticas = equiposServicio()
            equipo_local_stats = servicio_estadisticas.obtenerEstadisticasPorEquipo(fixture.IdEquipoLocal)
            equipo_visitante_stats = servicio_estadisticas.obtenerEstadisticasPorEquipo(fixture.IdEquipoVisitante)

            predicts_por_fixture = servicio.calcular_probabilidades_partido(equipo_local_stats, equipo_visitante_stats)
            predict_string = servicio.comparar_equipos(equipo_local_stats, equipo_visitante_stats)

            local = predicts_por_fixture['Gana Local']
            empate = predicts_por_fixture['Empate']
            visitante = predicts_por_fixture['Gana Visitante']

            if len(predicts_por_fixture.keys()) == 0:
                fixturesReal.append(FixtureIndex(fixture, "--", "--", "--", "--"))
            else:
                fixturesReal.append(FixtureIndex(fixture, local, empate, visitante, predict_string))

        return render(request, 'index.html', {
            'fixtures': fixturesReal,
            'form': barraBusqueda()
        })
    else:
        query = request.POST['query']
        url = reverse('Search', args=[query])
        return redirect(url)

def fixture_detalle(request, id):
    try:
        servicio = fixturesServicio()
        fixture = servicio.fixturePorID(id)

        servicio = apuestasServicio()
        apuestas = servicio.apuestasPorFixture(id)

        servicio = apuestasServicio()
        apuestas_n = servicio.tiposApuestaPorFixture(fixture)

        return render(request, 'fixtures/fixture_detalle.html', {
            'fixture': fixture,
            'apuestas': apuestas,
            'apuestas_n': apuestas_n
        })
    except:
        return redirect(index)

def fixture_predicts(request, id):
    try:
        servicio = fixturesServicio()
        fixture = servicio.fixturePorID(id)

        servicio = prediccionesServicio()
        predicts = servicio.predictsPorFixture(id)

        servicio = apuestasServicio()
        apuestas_n = servicio.tiposApuestaPorFixture(fixture)

        return render(request, 'fixtures/fixture_predicts.html', {
            'fixture': fixture,
            'predicts': predicts,
            'apuestas_n': apuestas_n
        })
    except:
        return redirect(index)

def feed_busqueda(request, query):
    try:
        exception = int(query)
        try:
            servicio = equiposServicio()
            equipo = servicio.equipoPorID(query)
        except:
            return redirect('Home')
    except:
        try:
            servicio = equiposServicio()
            equipos = servicio.realizarBusqueda(query)
            equipo = equipos[0]
        except:
            return redirect('Home')
        
    servicio = equiposServicio()

    equipo_stats = servicio.obtenerEstadisticasPorEquipo(equipo)
    equipo_con_posicion = EquipoConPosicion(equipo_stats, servicio.obtenerPosicionDeUnEquipo(equipo), equipo)

    equipos = servicio.obtenerEquiposPorCompetencia(128)

    stats_equipos = []

    for equipo_ in equipos:
        equipo_stats = servicio.obtenerEstadisticasPorEquipo(equipo_)
        stats_equipos.append(EquipoConPosicion(equipo_stats, servicio.obtenerPosicionDeUnEquipo(equipo_), equipo_))

    stats_equipos.sort(key=lambda x: x.posicion)

    fixturesReal = []

    servicio = jugadoresServicio()
    jugadores = servicio.jugadoresPorEquipo(equipo.IdApiEquipo_id, limit = 4)

    servicio = fixturesServicio()
    fixtures = servicio.fixturesPorEquipo(equipo.IdApiEquipo_id)

    for fixture in fixtures:
        servicio = prediccionesServicio()

        servicio_estadisticas = equiposServicio()
        equipo_local_stats = servicio_estadisticas.obtenerEstadisticasPorEquipo(fixture.IdEquipoLocal)
        equipo_visitante_stats = servicio_estadisticas.obtenerEstadisticasPorEquipo(fixture.IdEquipoVisitante)

        predicts_por_fixture = servicio.calcular_probabilidades_partido(equipo_local_stats, equipo_visitante_stats)
        predict_string = servicio.comparar_equipos(equipo_local_stats, equipo_visitante_stats)

        local = predicts_por_fixture['Gana Local']
        empate = predicts_por_fixture['Empate']
        visitante = predicts_por_fixture['Gana Visitante']

        if len(predicts_por_fixture.keys()) == 0:
            fixturesReal.append(FixtureIndex(fixture, "--", "--", "--", "--"))
        else:
            fixturesReal.append(FixtureIndex(fixture, local, empate, visitante, predict_string))

    return render(request, 'equipos/equipo.html', {
        'fixtures': fixturesReal,
        'jugadores': jugadores,
        'equipo': equipo_con_posicion,
        'stats_equipos': stats_equipos
    })

def jugadores_equipo(request, query):
    servicio = equiposServicio()
    equipo = servicio.equipoPorID(query)

    servicio = jugadoresServicio()
    jugadores = servicio.jugadoresPorEquipo(equipo.IdApiEquipo_id)

    return render(request, 'equipos/jugadores.html', {
        'jugadores': jugadores,
        'equipo': equipo
    })

def about(request):
    return render(request, 'about.html')

def login(request):
    return render(request,'usuario/iniciarsesion.html')

def signup(request):
    return render(request,'usuario/registrarse.html')

# 
# 
# VIEWS PARA POSTS
# 
# 
    
def post_equipos(request):
    if request.method == 'GET':
        return render(request, 'post_requests/post_equipos.html', {
            'form': activateRequest()
        })
    else:
        competencia = 128
        servicio = apiFutbolServicio()
        equipos = servicio.EquiposEstadios(competencia = competencia)

        servicio = equiposServicio()
        servicio.crearEquipos(equipos, competencia)

        return redirect('Home')
    
def post_competiciones(request):
    if request.method == 'GET':
        return render(request, 'post_requests/post_competiciones.html', {
            'form': activateRequest()
        })
    else:
        servicio = apiFutbolServicio()
        competiciones = servicio.Competiciones(pais = "Argentina")

        servicio = competicionesServicio()
        servicio.crearCompeticiones(competiciones)

        return redirect('Home')
    
def post_fixtures(request):
    if request.method == 'GET':
        return render(request, 'post_requests/post_fixtures.html', {
            'form': activateRequest()
        })
    else:
        servicio = apiFutbolServicio()
        fixtures = servicio.Fixtures(liga = "128", inicio = "2024-05-23", fin = "2024-12-16")

        servicio = fixturesServicio()
        servicio.actualizarFixtures(fixtures)

        return redirect('Home')
    
def post_estadios(request):
    if request.method == 'GET':
        return render(request, 'post_requests/post_estadios.html', {
            'form': activateRequest()
        })
    else:
        servicio = apiFutbolServicio()
        estadios = servicio.EquiposEstadios(128)

        servicio = estadiosServicio()
        servicio.crearEstadios(estadios)

        return redirect('Home')
    
def post_bookmakers(request):
    if request.method == 'GET':
        return render(request, 'post_requests/post_bookmakers.html', {
            'form': activateRequest()
        })
    else:
        servicio = apiFutbolServicio()
        bookmakers = servicio.Bookmakers()

        servicio = apuestasServicio()
        servicio.crearBookmakers(bookmakers)

        return redirect('Home')
    
def post_apuestas(request):
    if request.method == 'GET':
        return render(request, 'post_requests/post_apuestas.html', {
            'form': activateRequest()
        })
    else:
        # Se necesita hacer la request por páginas ya que asi se maximiza la cantidad de datos obtenidos por request
        pages = [1,2,3]

        for page in pages:
            competicion = 128
            servicio = apiFutbolServicio()
            apuestas = servicio.Apuestas(competicion, page)

            servicio = apuestasServicio()
            servicio.actualizarApuestas(apuestas)

        return redirect('Home')
    
def post_apuestas_id(request):
    if request.method == 'GET':
        return render(request, 'post_requests/post_apuestas_id.html', {
            'form': activateRequest()
        })
    else:
        servicio = apiFutbolServicio()
        apuestas_id = servicio.tipoApuestas()

        servicio = apuestasServicio()
        servicio.crearTiposApuesta(apuestas_id)

        return redirect('Home')
    
def post_porcentajes(request):
    if request.method == 'GET':
        return render(request, 'post_requests/post_porcentajes.html', {
            'form': activateRequest()
        })
    else:
        servicio = apuestasServicio()
        apuestas = servicio.obtenerApuestas()

        servicio = apuestasServicio()
        porcentajes = servicio.generarPorcentajes(apuestas)

        servicio = apuestasServicio()
        servicio.actualizarPorcentaje(porcentajes, apuestas)

        return redirect('Home')
    
def post_jugadores(request):
    if request.method == 'GET':
        return render(request, 'post_requests/post_jugadores.html', {
            'form': activateRequest()
        })
    else:
        servicio = equiposServicio()
        equipos = servicio.obtenerEquiposPorCompetencia(128)

        servicio = apiFutbolServicio()
        for equipo in equipos:
            jugadores = servicio.Jugadores(equipo.IdApiEquipo_id)
            
            servicio_jugadores = jugadoresServicio()
            servicio_jugadores.crearJugadores(jugadores)

        return redirect('Home')

def post_equipos_estadisticas(request):
    if request.method == 'GET':
        return render(request, 'post_requests/post_equipos_estadisticas.html', {
            'form': activateRequest()
        })
    else:
        servicio = equiposServicio()
        equipos = servicio.obtenerEquiposPorCompetencia(128)

        servicio = apiFutbolServicio()
        for equipo in equipos:
            estadisticas = servicio.equipoEstadisticas(equipo.IdApiEquipo_id)
            
            servicio_equipos = equiposServicio()
            servicio_equipos.actualizarEstadisticasEquipo(estadisticas, equipo)

        return redirect('Home')
    
def actualizar_todo(request):
    if request.method == 'GET':
        return render(request, 'post_requests/post_equipos_estadisticas.html', {
            'form': activateRequest()
        })
    else:
        servicio = apiFutbolServicio()
        fixtures = servicio.Fixtures(liga = "128", inicio = "2024-05-23", fin = "2024-12-16")

        servicio = fixturesServicio()
        servicio.actualizarFixtures(fixtures)

        servicio = equiposServicio()
        equipos = servicio.obtenerEquiposPorCompetencia(128)

        servicio = apiFutbolServicio()
        for equipo in equipos:
            estadisticas = servicio.equipoEstadisticas(equipo.IdApiEquipo_id)
            
            servicio_equipos = equiposServicio()
            servicio_equipos.actualizarEstadisticasEquipo(estadisticas, equipo)

        servicio = equiposServicio()
        equipos = servicio.obtenerEquiposPorCompetencia(128)
        servicio = apiFutbolServicio()
        for equipo in equipos:
            jugadores = servicio.Jugadores(equipo.IdApiEquipo_id)
            
            servicio_jugadores = jugadoresServicio()
            servicio_jugadores.crearJugadores(jugadores)

        pages = [1,2,3]

        for page in pages:
            competicion = 128
            servicio = apiFutbolServicio()
            apuestas = servicio.Apuestas(competicion, page)

            servicio = apuestasServicio()
            servicio.actualizarApuestas(apuestas)

        servicio = apuestasServicio()
        apuestas = servicio.obtenerApuestas()

        servicio = apuestasServicio()
        porcentajes = servicio.generarPorcentajes(apuestas)

        servicio = apuestasServicio()
        servicio.actualizarPorcentaje(porcentajes, apuestas)

        return redirect('Home')