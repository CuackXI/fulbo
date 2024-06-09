from deep_translator import GoogleTranslator
import requests

url = "https://api-football-v1.p.rapidapi.com/v3/odds/bets"

headers = {
    "X-RapidAPI-Key": "36d0515859mshc128509052fcf97p1484c4jsn6f58a0e1bbb7",
    "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

response = response.json()

for i in range(len(response['response'])):
    nombre = GoogleTranslator(source='english', target='spanish').translate(response['response'][i]['name'])
    print(nombre)