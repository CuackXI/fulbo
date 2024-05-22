from django.shortcuts import render, get_object_or_404, redirect
from django.db import connection
import requests
from .requests.clase_request import Request
from .models import *
from .forms import *

# Create your views here.

def index(request):
    query = f'SELECT IdApiFixture_id from timballapp_fixture where timballapp_fixture.IdApiComp_id = 128 and Status != "Match Finished"'
    fixtures = Fixture.objects.raw(query)
    return render(request, 'index.html', {
        'fixtures': fixtures
    })

def about(request):
    return render(request, 'about.html')

def fixture_detalle(request, id):
    fixture = get_object_or_404(Fixture, IdApiFixture_id=id)
    apuestas = Apuesta.objects.filter(IdApiFixture_id=id)
    query = "SELECT DISTINCT timballapp_apiapuestas.IdApiApuesta from timballapp_apiapuestas join timballapp_apuesta on timballapp_apiapuestas.IdApiApuesta = timballapp_apuesta.IdApiApuesta_id where timballapp_apiapuestas.IdApiApuesta = timballapp_apuesta.IdApiApuesta_id"
    apuestas_n = ApiApuestas.objects.raw(query)
    # Apuestas_n son los nombres de las apuestas usadas por el bookmaker

    return render(request, 'fixtures/fixture_detalle.html', {
        'fixture': fixture,
        'apuestas': apuestas,
        'apuestas_n': apuestas_n
    })

def post_porcentajes(request):
    if request.method == 'GET':
        return render(request, 'post_requests/post_porcentajes.html', {
            'form': activateRequest()
        })
    else:
        query = "SELECT DISTINCT id, IdApiFixture_id from timballapp_apuesta group by IdApiFixture_id"
        fixtures = Apuesta.objects.raw(query)
        for fixture in fixtures:         
            query = f'SELECT DISTINCT id, IdApiApuesta_id from timballapp_apuesta where IdApiFixture_id = {fixture.IdApiFixture_id} group by IdApiApuesta_id'
            ids = Apuesta.objects.raw(query)
            for id in ids:
                query = f'SELECT id, Multiplicador, tipo from timballapp_apuesta where IdApiFixture_id = {fixture.IdApiFixture_id} and IdApiApuesta_id = {id.IdApiApuesta_id}'
                apuestas = Apuesta.objects.raw(query)
                tipos = []
                multiplicadores = []
                for apuesta in apuestas:
                    tipos.append(apuesta.Tipo)
                    multiplicadores.append(apuesta.Multiplicador)
                porcentajes = Apuesta.MultiplicadorAPorcentaje(multiplicadores)
                for i in range(len(porcentajes)):
                    query = f'UPDATE timballapp_apuesta SET Porcentaje = {porcentajes[i]} where id = {apuestas[i].id}'
                    with connection.cursor() as cursor:
                        cursor.execute(query)
                        
                    # Apuesta_P.objects.create(
                    #     IdApiBookmaker_id = id.IdApiBookmaker_id,
                    #     IdApiApuesta_id = id.IdApiApuesta_id,
                    #     Porcentaje = porcentajes[i],
                    #     Tipo = tipos[i],
                    #     IdApiFixture_id = fixture.IdApiFixture_id
                    # )

        return redirect(post_porcentajes)

def post_paises(request):
    if request.method == 'GET':
        return render(request, 'post_requests/post_paises.html', {
            'form': activateRequest()
        })
    else:
        # url = "https://api-football-v1.p.rapidapi.com/v3/countries"
        # headers = {
        #     "x-rapidapi-key": "36d0515859mshc128509052fcf97p1484c4jsn6f58a0e1bbb7",
        #     "x-rapidapi-host": "api-football-v1.p.rapidapi.com",
        #     "Content-Type": "application/json"
        # }
        # response = requests.get(url, headers=headers)
        # response = response.json()
        # print(response)
        # for i in range(len(response['response'])):
        #     Pais.objects.create(Nombre=response['response'][i]['name'], Image_URL=response['response'][i]['flag'])
        print("Se ejecutó el POST :)")
        return render(request, 'index.html')
    
def post_equipos(request):
    if request.method == 'GET':
        return render(request, 'post_requests/post_equipos.html', {
            'form': activateRequest()
        })
    else:
    #     url = "https://api-football-v1.p.rapidapi.com/v3/teams"

    #     competencia = 128

    #     querystring = {"league":str(competencia),"season":"2024"}

    #     headers = {
    #         "x-rapidapi-key": "36d0515859mshc128509052fcf97p1484c4jsn6f58a0e1bbb7",
    #         "x-rapidapi-host": "api-football-v1.p.rapidapi.com",
    #         "Content-Type": "application/json"
    #     }

    #     response = requests.get(url, headers=headers, params=querystring)

    #     response = response.json()
    #     for i in range(len(response['response'])):
    #         Equipo.objects.create(
    #             IdApiEquipo=response['response'][i]['team']['id'],
    #             IdApiComp=competencia,
    #             Nombre=response['response'][i]['team']['name'],
    #             IdApiEstadio=response['response'][i]['venue']['id'],
    #             Pais=response['response'][i]['team']['country'],
    #             Image_URL=response['response'][i]['team']['logo'],
    #             Fundacion=response['response'][i]['team']['founded']
    #         )
        print("Se ejecutó el POST :)")
        return render(request, 'index.html')
    
def post_competiciones(request):
    if request.method == 'GET':
        return render(request, 'post_requests/post_competiciones.html', {
            'form': activateRequest()
        })
    else:
        # url = "https://api-football-v1.p.rapidapi.com/v3/leagues"

        # querystring = {"country":"Argentina"}

        # headers = {
        #     "x-rapidapi-key": "36d0515859mshc128509052fcf97p1484c4jsn6f58a0e1bbb7",
        #     "x-rapidapi-host": "api-football-v1.p.rapidapi.com",
        #     "Content-Type": "application/json"
        # }

        # response = requests.get(url, headers=headers, params=querystring)

        # response = response.json()

        # for i in range(len(response['response'])):
        #     Competiciones.objects.create(
        #     IdApiComp=response['response'][i]['league']['id'],
        #     Nombre=response['response'][i]['league']['name'],
        #     Image_URL=response['response'][i]['league']['logo'],
        #     Temporada=2024,
        #     Pais=response['response'][i]['country']['name']
        #     )
        print("Se ejecutó el POST :)")
        return render(request, 'index.html')
    
def post_fixtures(request):
    if request.method == 'GET':
        return render(request, 'post_requests/post_fixtures.html', {
            'form': activateRequest()
        })
    else:
        url = "https://api-football-v1.p.rapidapi.com/v3/fixtures"

        querystring = {"league":"128",
                    "season":"2024",
                    "from": "2024-05-09", 
                    "to": "2024-12-15"}

        headers = {
            "X-RapidAPI-Key": "36d0515859mshc128509052fcf97p1484c4jsn6f58a0e1bbb7",
            "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)

        response = response.json()

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

            Fixture.objects.create(
                IdApiComp_id=response['response'][i]['league']['id'],
                IdApiFixture_id=response['response'][i]['fixture']['id'],
                Arbitro=response['response'][i]['fixture']['referee'],
                Fecha=datestr,
                Hora=timestr,
                IdApiEstadio_id=response['response'][i]['fixture']['venue']['id'],
                IdEquipoLocal_id=response['response'][i]['teams']['home']['id'],
                IdEquipoVisitante_id=response['response'][i]['teams']['away']['id'],
                Status=response['response'][i]['fixture']['status']['long']
            )
        print("Se ejecutó el POST :)")
        return render(request, 'index.html')
    
def post_estadios(request):
    if request.method == 'GET':
        return render(request, 'post_requests/post_estadios.html', {
            'form': activateRequest()
        })
    else:
        url = "https://api-football-v1.p.rapidapi.com/v3/teams"

        querystring = {"league":"128","season":"2024"}

        headers = {
            "x-rapidapi-key": "36d0515859mshc128509052fcf97p1484c4jsn6f58a0e1bbb7",
            "x-rapidapi-host": "api-football-v1.p.rapidapi.com",
            "Content-Type": "application/json"
        }

        response = requests.get(url, headers=headers, params=querystring)

        response = response.json()

        for i in range(len(response['response'])):
            Estadio.objects.create(
                IdApiEstadio=response['response'][i]['venue']['id'],
                Nombre=response['response'][i]['venue']['name'],
                Direccion=response['response'][i]['venue']['address'],
                Ciudad=response['response'][i]['venue']['city'],
                Capacidad=response['response'][i]['venue']['capacity'],
                Image_URL=response['response'][i]['venue']['image']
            )
        print("Se ejecutó el POST :)")
        return render(request, 'index.html')
    
def post_bookmakers(request):
    if request.method == 'GET':
        return render(request, 'post_requests/post_bookmakers.html', {
            'form': activateRequest()
        })
    else:
        url = "https://api-football-v1.p.rapidapi.com/v3/odds/bookmakers"

        headers = {
            "X-RapidAPI-Key": "36d0515859mshc128509052fcf97p1484c4jsn6f58a0e1bbb7",
            "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers)

        response = response.json()

        for i in range(len(response['response'])):
            Bookmaker.objects.create(
                Bookmaker=response['response'][i]['id'],
                Nombre=response['response'][i]['name']
            )
        print("Se ejecutó el POST :)")
        return render(request, 'index.html')
    
def post_apuestas(request):
    if request.method == 'GET':
        return render(request, 'post_requests/post_apuestas.html', {
            'form': activateRequest()
        })
    else:
        pages = [1,2,3]
        for page in pages:
            url = "https://api-football-v1.p.rapidapi.com/v3/odds"

            querystring = {"league":"128","season":"2024", "bookmaker": 26, "page":page}

            headers = {
                "X-RapidAPI-Key": "36d0515859mshc128509052fcf97p1484c4jsn6f58a0e1bbb7",
                "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
            }

            response = requests.get(url, headers=headers, params=querystring)

            response = response.json()

            for i in range(len(response['response'])):
                for b in range(len(response['response'][i]['bookmakers'])):
                    for y in response['response'][i]['bookmakers'][b]['bets']:
                        for x in y['values']:
                            Apuesta.objects.create(
                                IdApiFixture_id=response['response'][i]['fixture']['id'],
                                IdApiBookmaker_id=response['response'][i]['bookmakers'][b]['id'],
                                IdApiApuesta_id=y['id'],
                                Tipo=x['value'],
                                Multiplicador=x['odd']
                            )

        print("Se ejecutó el POST :)")
        return render(request, 'index.html')
    
def post_apuestas_id(request):
    if request.method == 'GET':
        return render(request, 'post_requests/post_apuestas_id.html', {
            'form': activateRequest()
        })
    else:
        url = "https://api-football-v1.p.rapidapi.com/v3/odds/bets"

        headers = {
            "X-RapidAPI-Key": "36d0515859mshc128509052fcf97p1484c4jsn6f58a0e1bbb7",
            "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers)

        response = response.json()

        for i in range(len(response['response'])):
            if response['response'][i]['name'] == None:
                text = ""
            else:
                text = response['response'][i]['name']
            nombre = GoogleTranslator(source='english', target='spanish').translate(text)
            print(nombre)
            # ApiApuestas.objects.create(
            #     IdApiApuesta=response['response'][i]['id'],
            #     Nombre=response['response'][i]['name']
            # )