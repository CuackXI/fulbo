import requests

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