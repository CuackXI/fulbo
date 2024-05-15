import requests

url = "https://api-football-v1.p.rapidapi.com/v3/odds"

querystring = {"league":"128","season":"2024","bookmaker":"26"}

headers = {
	"X-RapidAPI-Key": "36d0515859mshc128509052fcf97p1484c4jsn6f58a0e1bbb7",
	"X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

response = response.json()

for i in range(len(response['response'])):
    print(response['response'][i]['fixture']['id'])
    print(response['response'][i]['bookmakers'][0]['id'])

    # for y in response['response'][i]['bookmakers'][0]['bets']:
    #     print(y['id'])
    #     print(y['name'])

    #     for x in y['values']:
    #         print(x['value'])
    #         print(x['odd'])
    
    print("")