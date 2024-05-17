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
                    # Apuesta.objects.create(
                    #     IdApiFixture=response['response'][i]['fixture']['id'],
                    #     IdApiBookmaker=response['response'][i]['bookmakers'][b]['id'],
                    #     IdApiFixture=y['id'],
                    #     Nombre=y['name'],
                    #     Tipo=x['value'],
                    #     Multiplicador=x['odd']
                    # )
                    pass