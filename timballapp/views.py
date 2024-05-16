from django.shortcuts import render
import requests
from .requests.clase_request import Request
from .models import *
from .forms import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

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
                    "from": "2024-05-17", 
                    "to": "2024-05-21"}

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
            dia = ""
            contador = 0
            for char in text:
                if char == "+":
                    break
                if char == "T":
                    date = False
                if char == ":":
                    time = True
                if time == False and date == True and contador != 2:
                    datestr += char
                elif contador == 2 and date == True:
                    dia += char
                elif time == True and char!="T":
                    timestr += char
                elif char!="T":
                    hora += char
                if char == "-":
                    contador+=1

            hora = int(hora) - 3

            if int(hora) < 0:
                hora = str(24 + int(hora))
                dia = str(int(dia)-1)

            timestr = str(hora) + timestr
            datestr = datestr + str(dia)

            Fixture.objects.create(
                IdApiFixture=response['response'][i]['fixture']['id'],
                Arbitro=response['response'][i]['fixture']['referee'],
                Fecha=datestr,
                Hora=timestr,
                IdApiEstadio=response['response'][i]['fixture']['venue']['id'],
                IdEquipoLocal=response['response'][i]['teams']['home']['id'],
                IdEquipoVisitante=response['response'][i]['teams']['away']['id'],
                Status=response['response'][i]['fixture']['status']['long']
            )
        print("Se ejecutó el POST :)")
        return render(request, 'index.html')