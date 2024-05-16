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
            'fixture_id': id,
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
        # Este request ya fue ejecutado :)
        print("Se ejecutó el POST :)")
        return render(request, 'index.html')