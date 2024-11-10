import requests

ids = [434, 435, 436, 437, 438, 439, 440, 441, 442, 445, 446, 449, 450, 451, 452, 453, 455, 456, 457, 458, 460, 473, 474, 476, 478, 1064, 1065, 2432]
responses=[]
# for i in range(len(ids)):

url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"
querystring = {"league":"128","season":"2024","team":"450"}
headers = {
    "X-RapidAPI-Key": "36d0515859mshc128509052fcf97p1484c4jsn6f58a0e1bbb7",
    "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}
response = requests.get(url, headers=headers, params=querystring)
response = response.json()
# responses.append(response)

# for response in responses:
    # for i in range(len(response['response'])):
print("ID Liga:", response['response']['league']['id'])
print("ID Equipo:", response['response']['team']['id'])
print("Partidos jugados:", response['response']['fixtures']['played']['total'])
print("Partidos ganados de local:", response['response']['fixtures']['wins']['home'])
print("Partidos ganados de visitante:", response['response']['fixtures']['wins']['away'])
print("Partidos ganados en total:", response['response']['fixtures']['wins']['total'])
print("Partidos empatados de local:", response['response']['fixtures']['draws']['home'])
print("Partidos empatados de visitante:", response['response']['fixtures']['draws']['away'])
print("Partidos empatados en total:", response['response']['fixtures']['draws']['total'])
print("Partidos perdidos de local:", response['response']['fixtures']['loses']['home'])
print("Partidos perdidos de visitante:", response['response']['fixtures']['loses']['away'])
print("Partidos perdidos en total:", response['response']['fixtures']['loses']['total'])
print("Goles a favor de local:", response['response']['goals']['for']['total']['home'])
print("Goles a favor de visitante:", response['response']['goals']['for']['total']['away'])
print("Goles a favor en total:", response['response']['goals']['for']['total']['total'])
print("Goles en contra de visitante:", response['response']['goals']['against']['total']['home'])
print("Goles en contra de local:", response['response']['goals']['against']['total']['away'])
print("Goles en contra en total:", response['response']['goals']['against']['total']['total'])
print("Alineaciones:", response['response']['lineups'])