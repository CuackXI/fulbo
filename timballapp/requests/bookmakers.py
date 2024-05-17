import requests

url = "https://api-football-v1.p.rapidapi.com/v3/odds/bookmakers"

headers = {
	"X-RapidAPI-Key": "36d0515859mshc128509052fcf97p1484c4jsn6f58a0e1bbb7",
	"X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

response = response.json()

for i in range(len(response['response'])):
    print(response['response'][i]['id'])
    print(response['response'][i]['name'])
    print("")
# ESTO TAMBIEN HAY QUE HACER VARIOS REQUESTS PORQUE TE TIRA SOLO 10 PARTIDOS PERO EN REALIDAD SON MUCHISIMOS MAS :)
# HABRIA QUE HACER ESTO CADA SEMANA SOLO CON LOS PARTIDOS QUE SE JUEGAN ESA SEMANA