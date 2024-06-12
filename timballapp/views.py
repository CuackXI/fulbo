from django.shortcuts import render, redirect
from .servicios.obtener_porcentajes import Obtener_Porcentajes
from .servicios.actualizar_porcentajes import Actualizar_Porcentajes
from .servicios.obtener_apuestas import Obtener_Apuestas
from .servicios.Obtener_Fixtures_Proximos_Por_Competencia import Obtener_Fixtures_Proximos_Por_Competencia
from .servicios.Apuestas_Match_Winner_Por_Fixture import Apuestas_Match_Winner_Por_Fixture
from .servicios.apuestas_por_fixture import Apuestas_Por_Fixture
from .servicios.Fixture_por_ID import Fixture_por_ID
from .servicios.nombres_de_apuestas_de_fixture import nombres_de_apuestas_de_fixture
from .servicios.Predicts_Por_Fixture import Predicts_Por_Fixture
from .servicios.crear_objetos import crear_objetos
from .servicios.get_fixtures import get_all_fixtures
from .servicios.jugadores_por_equipo import jugadores_por_equipo
from .servicios.equipo_por_id import equipo_por_id
from .servicios.fixtures_por_equipo import fixtures_por_equipo
from .servicios.busqueda_equipos_coincidencia import busqueda_equipos_coincidencia
from .requests.clase_request import Request
from .models import *
from .forms import *

# Create your views here.

def index(request):
    if request.method == 'GET':
        servicio = Obtener_Fixtures_Proximos_Por_Competencia()
        fixtures = servicio.Obtener_Fixtures_Proximos_Por_Competencia(128)

        servicio = Apuestas_Match_Winner_Por_Fixture()
        apuestas_por_fixture = servicio.Apuestas_Match_Winner_Por_Fixture(128, fixtures)

        return render(request, 'index.html', {
            'fixtures': fixtures,
            'apuestas': apuestas_por_fixture,
            'form': barraBusqueda()
        })
    else:
        query = request.POST['query']

        return redirect(f'busqueda/{query}')

def fixture_detalle(request, id):
    servicio = Fixture_por_ID()
    fixture = servicio.Fixture_por_ID(id)

    servicio = Apuestas_Por_Fixture()
    apuestas = servicio.Apuestas_Por_Fixture(id)

    servicio = nombres_de_apuestas_de_fixture()
    apuestas_n = servicio.nombres_de_apuestas_de_fixture(fixture)

    return render(request, 'fixtures/fixture_detalle.html', {
        'fixture': fixture,
        'apuestas': apuestas,
        'apuestas_n': apuestas_n
    })

def fixture_predicts(request, id):
    servicio = Fixture_por_ID()
    fixture = servicio.Fixture_por_ID(id)

    servicio = Predicts_Por_Fixture()
    predicts = servicio.Predicts_Por_Fixture(id)

    servicio = nombres_de_apuestas_de_fixture()
    apuestas_n = servicio.nombres_de_apuestas_de_fixture(fixture)

    return render(request, 'fixtures/fixture_predicts.html', {
        'fixture': fixture,
        'predicts': predicts,
        'apuestas_n': apuestas_n
    })

def equipo_especifico(request, id):

    servicio = equipo_por_id()
    equipo = servicio.equipo_por_id(id)

    servicio = jugadores_por_equipo()
    jugadores = servicio.jugadores_por_equipo(equipo.IdApiEquipo_id)

    servicio = fixtures_por_equipo()
    fixtures = servicio.fixtures_por_equipo(id)

    return render(request, 'equipos/equipo.html', {
        'equipo': equipo,
        'jugadores': jugadores,
        'fixtures': fixtures
    })

def feed_busqueda(request, query):
    servicio = busqueda_equipos_coincidencia()
    equipos = servicio.busqueda_equipos_coincidencia(query)
    print(equipos)
    if equipos.exists():
        equipo = equipos[0]
        servicio = fixtures_por_equipo()
        fixtures = servicio.fixtures_por_equipo(equipo.IdApiEquipo_id)
        servicio = Apuestas_Match_Winner_Por_Fixture()
        apuestas_por_fixture = servicio.Apuestas_Match_Winner_Por_Fixture(128, fixtures)
        return render(request, 'index.html', {
        'fixtures': fixtures,
        'apuestas': apuestas_por_fixture,
        'equipo': equipo
        })
    else:
        equipo = 440
        servicio = Obtener_Fixtures_Proximos_Por_Competencia()
        fixtures = servicio.Obtener_Fixtures_Proximos_Por_Competencia(128)
        servicio = Apuestas_Match_Winner_Por_Fixture()
        apuestas_por_fixture = servicio.Apuestas_Match_Winner_Por_Fixture(128, fixtures)
        return render(request, 'index.html', {
        'fixtures': fixtures,
        'apuestas': apuestas_por_fixture
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

def post_paises(request):
    if request.method == 'GET':
        return render(request, 'post_requests/post_paises.html', {
            'form': activateRequest()
        })
    else:
        request_paises = Request(url="https://api-football-v1.p.rapidapi.com/v3/countries", querystring=None)

        paises = request_paises.hacer_request()

        servicio = crear_objetos()
        servicio.response_to_paises(paises)

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

        servicio = crear_objetos()
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

        servicio = crear_objetos()
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

        servicio = crear_objetos()
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

        servicio = crear_objetos()
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

            servicio = crear_objetos()
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

        servicio = crear_objetos()
        servicio.response_to_apuestas_id(apuestas_id)

        return redirect('Home')
    
def post_porcentajes(request):
    if request.method == 'GET':
        return render(request, 'post_requests/post_porcentajes.html', {
            'form': activateRequest()
        })
    else:
        servicio = Obtener_Apuestas()
        apuestas = servicio.Obtener_Apuestas()

        servicio = Obtener_Porcentajes()
        porcentajes = servicio.obtener_porcentajes_a_partir_de_apuestas(apuestas)

        servicio = Actualizar_Porcentajes()
        servicio.Actualizar_Porcentajes(porcentajes, apuestas)

        return redirect('Home')