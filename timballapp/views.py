from django.shortcuts import render, get_object_or_404, redirect
from django.db import connection
import requests
from .servicios.obtener_porcentajes import Obtener_Porcentajes
from .servicios.actualizar_porcentajes import Actualizar_Porcentajes
from .servicios.obtener_apuestas import Obtener_Apuestas
from .servicios.Obtener_Fixtures_Proximos_Por_Competencia import Obtener_Fixtures_Proximos_Por_Competencia
from .servicios.Apuestas_Match_Winner_Por_Fixture import Apuestas_Match_Winner_Por_Fixture
from .servicios.apuestas_por_fixture import Apuestas_Por_Fixture
from .servicios.Fixture_por_ID import Fixture_por_ID
from .servicios.nombres_de_apuestas_de_fixture import nombres_de_apuestas_de_fixture
from .servicios.Predicts_Por_Fixture import Predicts_Por_Fixture
from .requests.clase_request import Request
from .models import *
from .forms import *

# Create your views here.

def index(request):
    servicio = Obtener_Fixtures_Proximos_Por_Competencia()
    fixtures = servicio.Obtener_Fixtures_Proximos_Por_Competencia(128)

    servicio = Apuestas_Match_Winner_Por_Fixture()
    apuestas_por_fixture = servicio.Apuestas_Match_Winner_Por_Fixture(128, fixtures)

    return render(request, 'index.html', {
        'fixtures': fixtures,
        'apuestas': apuestas_por_fixture
    })

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

def about(request):
    return render(request, 'about.html')














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
        request_paises = Request(url="https://api-football-v1.p.rapidapi.com/v3/countries", querystring=None, headers={"x-rapidapi-key": "36d0515859mshc128509052fcf97p1484c4jsn6f58a0e1bbb7", "x-rapidapi-host": "api-football-v1.p.rapidapi.com", "Content-Type": "application/json"})

        paises = request_paises.request_response(request_paises.url, request_paises.querystring, request_paises.headers)

        response_to_paises(paises)

        return redirect('Home')
    
def post_equipos(request):
    if request.method == 'GET':
        return render(request, 'post_requests/post_equipos.html', {
            'form': activateRequest()
        })
    else:
        competencia = 128
        request_equipos = Request(url = "https://api-football-v1.p.rapidapi.com/v3/teams", querystring = {"league":str(competencia),"season":"2024"},         headers = {
            "x-rapidapi-key": "36d0515859mshc128509052fcf97p1484c4jsn6f58a0e1bbb7",
            "x-rapidapi-host": "api-football-v1.p.rapidapi.com",
            "Content-Type": "application/json"
        })

        equipos = request_equipos.request_response(request_equipos.url, request_equipos.querystring, request_equipos.headers)

        response_to_equipos(equipos, competencia)

        return redirect('Home')
    
def post_competiciones(request):
    if request.method == 'GET':
        return render(request, 'post_requests/post_competiciones.html', {
            'form': activateRequest()
        })
    else:
        request_competiciones = Request(url = "https://api-football-v1.p.rapidapi.com/v3/leagues", querystring = {"country":"Argentina"},         
        headers = {
            "x-rapidapi-key": "36d0515859mshc128509052fcf97p1484c4jsn6f58a0e1bbb7",
            "x-rapidapi-host": "api-football-v1.p.rapidapi.com",
            "Content-Type": "application/json"
        })

        competiciones = request_competiciones.request_response(request_competiciones.url, request_competiciones.querystring, request_competiciones.headers)

        response_to_competiciones(competiciones)

        return redirect('Home')
    
def post_fixtures(request):
    if request.method == 'GET':
        return render(request, 'post_requests/post_fixtures.html', {
            'form': activateRequest()
        })
    else:
        query = f'DELETE FROM timballapp_fixture where IdApiFixture_id > 0 and Status != "Match Finished"'
        with connection.cursor() as cursor:
            cursor.execute(query)

        request_fixtures = Request(url = "https://api-football-v1.p.rapidapi.com/v3/fixtures", 
                    querystring = {
                    "league":"128",
                    "season":"2024",
                    "from": "2024-05-09", 
                    "to": "2024-12-16"},
                    headers = {
                    "X-RapidAPI-Key": "36d0515859mshc128509052fcf97p1484c4jsn6f58a0e1bbb7",
                    "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"})

        fixtures = request_fixtures.request_response(request_fixtures.url, request_fixtures.querystring, request_fixtures.headers)

        response_to_fixtures(fixtures)

        return redirect('Home')
    
def post_estadios(request):
    if request.method == 'GET':
        return render(request, 'post_requests/post_estadios.html', {
            'form': activateRequest()
        })
    else:
        request_estadios = Request(url = "https://api-football-v1.p.rapidapi.com/v3/teams", querystring = {"league":"128","season":"2024"},headers = {
            "x-rapidapi-key": "36d0515859mshc128509052fcf97p1484c4jsn6f58a0e1bbb7",
            "x-rapidapi-host": "api-football-v1.p.rapidapi.com",
            "Content-Type": "application/json"
        })

        estadios = request_estadios.request_response(request_estadios.url, request_estadios.querystring, request_estadios.headers)

        response_to_estadios(estadios)

        return redirect('Home')
    
def post_bookmakers(request):
    if request.method == 'GET':
        return render(request, 'post_requests/post_bookmakers.html', {
            'form': activateRequest()
        })
    else:
        request_bookmakers = Request(url = "https://api-football-v1.p.rapidapi.com/v3/odds/bookmakers", querystring=None, headers = {
            "X-RapidAPI-Key": "36d0515859mshc128509052fcf97p1484c4jsn6f58a0e1bbb7",
            "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
        })

        bookmakers = request_bookmakers.request_response(request_bookmakers.url, request_bookmakers.querystring, request_bookmakers.headers)

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
            request_apuestas = Request(url = "https://api-football-v1.p.rapidapi.com/v3/odds", querystring = {"league":"128","season":"2024", "bookmaker": 26, "page":page}, headers = {"X-RapidAPI-Key": "36d0515859mshc128509052fcf97p1484c4jsn6f58a0e1bbb7", "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"})

            apuestas = request_apuestas.request_response(request_apuestas.url, request_apuestas.querystring, request_apuestas.headers)

            response_to_apuestas(apuestas)

        return redirect('Home')
    
def post_apuestas_id(request):
    if request.method == 'GET':
        return render(request, 'post_requests/post_apuestas_id.html', {
            'form': activateRequest()
        })
    else:
        request_apuestas = Request(url = "https://api-football-v1.p.rapidapi.com/v3/odds/bets", querystring = None, headers = {
            "X-RapidAPI-Key": "36d0515859mshc128509052fcf97p1484c4jsn6f58a0e1bbb7",
            "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
        })

        apuestas_id = request_apuestas.request_response(request_apuestas.url, request_apuestas.querystring, request_apuestas.headers)

        response_to_apuestas_id(apuestas_id)

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

















# FUNCIONES PARA LAS VIEWS

def response_to_paises(response):
    for i in range(len(response['response'])):
        # Pais.objects.create(Nombre=response['response'][i]['name'], Image_URL=response['response'][i]['flag'])
        print(response['response'][i]['name'])

def response_to_apuestas_id(response):
    for i in range(len(response['response'])):
        print(response['response'][i]['id'])
        print(response['response'][i]['name'])

def response_to_apuestas(response):
    for i in range(len(response['response'])):
        for b in range(len(response['response'][i]['bookmakers'])):
            for y in response['response'][i]['bookmakers'][b]['bets']:
                for x in y['values']:
                    # Apuesta.objects.create(
                    #     IdApiFixture_id=response['response'][i]['fixture']['id'],
                    #     IdApiBookmaker_id=response['response'][i]['bookmakers'][b]['id'],
                    #     IdApiApuesta_id=y['id'],
                    #     Tipo=x['value'],
                    #     Multiplicador=x['odd']
                    # )
                    pass

def response_to_bookmaker(response):
    for i in range(len(response['response'])):
        # Bookmaker.objects.create(
        #     Bookmaker=response['response'][i]['id'],
        #     Nombre=response['response'][i]['name']
        # )
        pass

def response_to_estadios(response):
    for i in range(len(response['response'])):
        pass
        # Estadio.objects.create(
        #     IdApiEstadio=response['response'][i]['venue']['id'],
        #     Nombre=response['response'][i]['venue']['name'],
        #     Direccion=response['response'][i]['venue']['address'],
        #     Ciudad=response['response'][i]['venue']['city'],
        #     Capacidad=response['response'][i]['venue']['capacity'],
        #     Image_URL=response['response'][i]['venue']['image']
        # )

def response_to_fixtures(response):
    for i in range(len(response['response'])):
        text = response['response'][i]['fixture']['date']
        time = False
        date = True
        datestr = ""
        timestr = ""
        hora = ""
        año = ""
        mes = ""
        dia = ""
        contador = 0
        for char in text:
            if char == "+":
                break
            if char == "T":
                date = False
            if char == ":":
                time = True
            if time == False and date == True and contador == 0 and char != "-":
                año += char
            elif contador == 1 and char != "-":
                mes += char
            elif contador == 2 and date == True and char != "-":
                dia += char
            elif time == True and char!="T":
                timestr += char
            elif char!="T" and char != "-":
                hora += char
            if char == "-":
                contador+=1

        print(hora, timestr, dia, mes, año)

        hora = int(hora) - 3

        if int(hora) < 0:
            hora = str(24 + int(hora))
            if dia != "01":
                dia = str(int(dia)-1)
            else:
                if mes == "01":
                    dia = "31"
                    mes = "12"
                    año = str(int(año)-1)
                elif mes == "02":
                    if año % 4 == 0:
                        dia = "29"
                        mes = "01"
                    else:
                        dia = "28"
                        mes = "01"
                elif mes == "03":
                    dia = "31"
                    mes = "02"
                elif mes == "04":
                    dia = "30"
                    mes = "03"
                elif mes == "05":
                    dia = "31"
                    mes = "04"
                elif mes == "06":
                    dia = "30"
                    mes = "05"
                elif mes == "07":
                    dia = "31"
                    mes = "06"
                elif mes == "08":
                    dia = "31"
                    mes = "07"
                elif mes == "09":
                    mes = "08"
                    dia = "30"
                elif mes == "10":
                    mes = "09"
                    dia = "31"
                elif mes == "11":
                    mes = "10"
                    dia = "30"
                elif mes == "12":
                    mes = "11"
                    dia = "30"

        timestr = str(hora) + timestr
        datestr = str(año) + "-" + str(mes) + "-" + str(dia)

        print(timestr)
        print(datestr)

        # Fixture.objects.create(
        #     IdApiComp_id=response['response'][i]['league']['id'],
        #     IdApiFixture_id=response['response'][i]['fixture']['id'],
        #     Arbitro=response['response'][i]['fixture']['referee'],
        #     Fecha=datestr,
        #     Hora=timestr,
        #     IdApiEstadio_id=response['response'][i]['fixture']['venue']['id'],
        #     IdEquipoLocal_id=response['response'][i]['teams']['home']['id'],
        #     IdEquipoVisitante_id=response['response'][i]['teams']['away']['id'],
        #     Status=response['response'][i]['fixture']['status']['long']
        # )

def response_to_equipos(response, competencia):
    # for i in range(len(response['response'])):
    #     Equipo.objects.create(
    #         IdApiEquipo=response['response'][i]['team']['id'],
    #         IdApiComp=competencia,
    #         Nombre=response['response'][i]['team']['name'],
    #         IdApiEstadio=response['response'][i]['venue']['id'],
    #         Pais=response['response'][i]['team']['country'],
    #         Image_URL=response['response'][i]['team']['logo'],
    #         Fundacion=response['response'][i]['team']['founded']
    #     )
    pass

def response_to_competiciones(response):
    # for i in range(len(response['response'])):
    #     Competiciones.objects.create(
    #     IdApiComp=response['response'][i]['league']['id'],
    #     Nombre=response['response'][i]['league']['name'],
    #     Image_URL=response['response'][i]['league']['logo'],
    #     Temporada=2024,
    #     Pais=response['response'][i]['country']['name'])
    pass