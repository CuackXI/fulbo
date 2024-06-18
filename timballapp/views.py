from django.shortcuts import render, redirect
from .servicios.generarPorcentajes import generarPorcentajes
from .servicios.actualizarPorcentaje import actualizarPorcentaje
from .servicios.obtenerApuestas import obtenerApuestas
from .servicios.fixturesPorCompetencia import fixturesPorCompetencia
from .servicios.predictsResultado import predictsResultado
from .servicios.apuestasPorFixture import apuestasPorFixture
from .servicios.fixturePorID import fixturePorID
from .servicios.nombres_de_apuestas_de_fixture import nombres_de_apuestas_de_fixture
from .servicios.predictsPorFixture import predictsPorFixture
from .servicios.crearObjetos import crearObjetos
from .servicios.jugadoresPorEquipo import jugadoresPorEquipo
from .servicios.equipoPorID import equipoPorID
from .servicios.fixturesPorEquipo import fixturesPorEquipo
from .servicios.realizarBusqueda import realizarBusqueda
from .requests.clase_request import Request
from .models import *
from .forms import *

# Create your views here.

def index(request):
    if request.method == 'GET':
        servicio = fixturesPorCompetencia()
        fixtures = servicio.fixturesPorCompetencia(128)

        servicio = predictsResultado()
        apuestas_por_fixture = servicio.predictsResultado(fixtures)

        return render(request, 'index.html', {
            'fixtures': fixtures,
            'apuestas': apuestas_por_fixture,
            'form': barraBusqueda()
        })
    else:
        query = request.POST['query']

        return redirect(f'busqueda/{query}')

def fixture_detalle(request, id):
    try:
        servicio = fixturePorID()
        fixture = servicio.fixturePorID(id)

        servicio = apuestasPorFixture()
        apuestas = servicio.apuestasPorFixture(id)

        servicio = nombres_de_apuestas_de_fixture()
        apuestas_n = servicio.nombres_de_apuestas_de_fixture(fixture)

        return render(request, 'fixtures/fixture_detalle.html', {
            'fixture': fixture,
            'apuestas': apuestas,
            'apuestas_n': apuestas_n
        })
    except:
        # placeholder
        return redirect(index)
        # aca iría una página de error

def fixture_predicts(request, id):
    try:
        servicio = fixturePorID()
        fixture = servicio.fixturePorID(id)

        servicio = predictsPorFixture()
        predicts = servicio.predictsPorFixture(id)

        servicio = nombres_de_apuestas_de_fixture()
        apuestas_n = servicio.nombres_de_apuestas_de_fixture(fixture)

        return render(request, 'fixtures/fixture_predicts.html', {
            'fixture': fixture,
            'predicts': predicts,
            'apuestas_n': apuestas_n
        })
    except:
        # placeholder
        return redirect(index)
        # aca iría una página de error

def equipo_especifico(request, id):
    try:
        servicio = equipoPorID()
        equipo = servicio.equipoPorID(id)

        servicio = jugadoresPorEquipo()
        jugadores = servicio.jugadoresPorEquipo(equipo.IdApiEquipo_id)

        servicio = fixturesPorEquipo()
        fixtures = servicio.fixturesPorEquipo(id)

        return render(request, 'equipos/equipo.html', {
            'equipo': equipo,
            'jugadores': jugadores,
            'fixtures': fixtures
        })
    except:
        # placeholder
        return redirect(index)
        # aca iría una página de error

def feed_busqueda(request, query):
    try:
        servicio = realizarBusqueda()
        equipos = servicio.realizarBusqueda(query)
        equipo = equipos[0]

        servicio = fixturesPorEquipo()
        fixtures = servicio.fixturesPorEquipo(equipo.IdApiEquipo_id)

        servicio = predictsResultado()
        apuestas_por_fixture = servicio.predictsResultado(fixtures)
        
        return render(request, 'search.html', {
        'fixtures': fixtures,
        'apuestas': apuestas_por_fixture,
        'equipo': equipo
        })
    except:
        return redirect(index)
    
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

def post_paises(request):
    if request.method == 'GET':
        return render(request, 'post_requests/post_paises.html', {
            'form': activateRequest()
        })
    else:
        request_paises = Request(url="https://api-football-v1.p.rapidapi.com/v3/countries", querystring=None)

        paises = request_paises.hacer_request()

        servicio = crearObjetos()
        servicio.crear_paises(paises)

        return redirect('Home')
    
def post_equipos(request):
    if request.method == 'GET':
        return render(request, 'post_requests/post_equipos.html', {
            'form': activateRequest()
        })
    else:
        competencia = 128
        request_equipos = Request(url = "https://api-football-v1.p.rapidapi.com/v3/teams", querystring = {"league":str(competencia),"season":"2024"})

        equipos = request_equipos.hacer_request()

        servicio = crearObjetos()
        servicio.response_to_equipos(equipos, competencia)

        return redirect('Home')
    
def post_competiciones(request):
    if request.method == 'GET':
        return render(request, 'post_requests/post_competiciones.html', {
            'form': activateRequest()
        })
    else:
        request_competiciones = Request(url = "https://api-football-v1.p.rapidapi.com/v3/leagues", querystring = {"country":"Argentina"})

        competiciones = request_competiciones.hacer_request()

        servicio = crearObjetos()
        servicio.response_to_competiciones(competiciones)

        return redirect('Home')
    
def post_fixtures(request):
    if request.method == 'GET':
        return render(request, 'post_requests/post_fixtures.html', {
            'form': activateRequest()
        })
    else:
        request_fixtures = Request(url = "https://api-football-v1.p.rapidapi.com/v3/fixtures", 
                    querystring = {
                    "league":"128",
                    "season":"2024",
                    "from": "2024-05-23", 
                    "to": "2024-12-16"},)

        fixtures = request_fixtures.hacer_request()

        print(fixtures)

        servicio = crearObjetos()
        servicio.response_to_fixtures(fixtures)

        return redirect('Home')
    
def post_estadios(request):
    if request.method == 'GET':
        return render(request, 'post_requests/post_estadios.html', {
            'form': activateRequest()
        })
    else:
        request_estadios = Request(url = "https://api-football-v1.p.rapidapi.com/v3/teams", 
            querystring = {"league":"128","season":"2024"})

        estadios = request_estadios.hacer_request()

        servicio = crearObjetos()
        servicio.response_to_estadios(estadios)

        return redirect('Home')
    
def post_bookmakers(request):
    if request.method == 'GET':
        return render(request, 'post_requests/post_bookmakers.html', {
            'form': activateRequest()
        })
    else:
        request_bookmakers = Request(url = "https://api-football-v1.p.rapidapi.com/v3/odds/bookmakers", querystring=None)

        bookmakers = request_bookmakers.hacer_request()

        request_bookmakers(bookmakers)
        return redirect('Home')
    
def post_apuestas(request):
    if request.method == 'GET':
        return render(request, 'post_requests/post_apuestas.html', {
            'form': activateRequest()
        })
    else:
        pages = [1,2,3]
        for page in pages:
            request_apuestas = Request(url = "https://api-football-v1.p.rapidapi.com/v3/odds", querystring = {"league":"128","season":"2024", "bookmaker": 26, "page":page})

            apuestas = request_apuestas.hacer_request()

            servicio = crearObjetos()
            servicio.response_to_apuestas(apuestas)

        return redirect('Home')
    
def post_apuestas_id(request):
    if request.method == 'GET':
        return render(request, 'post_requests/post_apuestas_id.html', {
            'form': activateRequest()
        })
    else:
        request_apuestas = Request(url = "https://api-football-v1.p.rapidapi.com/v3/odds/bets", querystring = None)

        apuestas_id = request_apuestas.hacer_request()

        servicio = crearObjetos()
        servicio.crear_apuestas_id(apuestas_id)

        return redirect('Home')
    
def post_porcentajes(request):
    if request.method == 'GET':
        return render(request, 'post_requests/post_porcentajes.html', {
            'form': activateRequest()
        })
    else:
        servicio = obtenerApuestas()
        apuestas = servicio.obtenerApuestas()

        servicio = generarPorcentajes()
        porcentajes = servicio.generarPorcentajes(apuestas)

        servicio = actualizarPorcentaje()
        servicio.actualizarPorcentaje(porcentajes, apuestas)

        return redirect('Home')