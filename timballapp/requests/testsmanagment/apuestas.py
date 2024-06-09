from deep_translator import GoogleTranslator
import requests

pages = [1]
for page in pages:
    url = "https://api-football-v1.p.rapidapi.com/v3/odds"

    querystring = {"league":"128","season":"2024", "page":page}

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
                    print(IdApiFixture=response['response'][i]['fixture']['id'])
                    print(IdApiBookmaker=response['response'][i]['bookmakers'][b]['id'])
                    print(IdApiFixture=y['id'])
                    
                    print(Nombre=y['name'])
                    print(Tipo=x['value'])
                    print(Multiplicador=x['odd'])