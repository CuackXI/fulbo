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

        querystring = {"league":"128","season":"2024"}

        headers = {
            "X-RapidAPI-Key": "36d0515859mshc128509052fcf97p1484c4jsn6f58a0e1bbb7",
            "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)

        response = response.json()

        for i in range(len(response['response'])):
            print(response['response'][i]['fixture']['id'])
            print(response['response'][i]['fixture']['referee'])
            print(response['response'][i]['fixture']['date']) # 3 HORAS MENOS QUE LO QUE DICE EL STRING PARA ARGENTINA :)
            print(response['response'][i]['fixture']['venue']['id'])
            print(response['response'][i]['fixture']['status']['long'])
            print(response['response'][i]['teams']['home']['id'])
            print(response['response'][i]['teams']['away']['id'])
        print("Se ejecutó el POST :)")
        return render(request, 'index.html')