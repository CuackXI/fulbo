import requests
from django.db import models
from ..models import *

url = "https://api-football-v1.p.rapidapi.com/v3/countries"

headers = {
	"x-rapidapi-key": "36d0515859mshc128509052fcf97p1484c4jsn6f58a0e1bbb7",
	"x-rapidapi-host": "api-football-v1.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.get(url, headers=headers)
response = response.json()

print(response)
for i in range(len(response['response'])):
    Pais.objects.create(Nombre=response['response'][i]['name'], Image_URL=response['response'][i]['flag'])