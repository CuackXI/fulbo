import requests

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
    print(response['response'][i]['team']['id'])
    print(response['response'][i]['team']['name'])
    print(response['response'][i]['team']['country'])
    print(response['response'][i]['venue']['id']) 
    print(response['response'][i]['team']['logo'])
    print(response['response'][i]['team']['founded'])
    print("")