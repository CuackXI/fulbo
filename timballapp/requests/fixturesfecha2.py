import requests

url = "https://api-football-v1.p.rapidapi.com/v3/fixtures"

querystring = {"league":"128","season":"2024","from":"2024-05-17","to":"2024-05-21"}

headers = {
	"X-RapidAPI-Key": "36d0515859mshc128509052fcf97p1484c4jsn6f58a0e1bbb7",
	"X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

response = response.json()

ids = [1158674, 1158675, 1158676, 1158677, 1158678, 1158679, 1158680, 1158681, 1158682, 1158683, 1158684, 1158685, 1158686, 1158687]

for i in range(len(response['response'])):
    # print(response['response'][i]['fixture']['id'])
    # print(response['response'][i]['fixture']['referee'])
    # print(response['response'][i]['fixture']['date']) # 3 HORAS MENOS QUE LO QUE DICE EL STRING PARA ARGENTINA :)
    # print(response['response'][i]['fixture']['venue']['id'])
    # print(response['response'][i]['fixture']['status']['long'])
    # print(response['response'][i]['teams']['home']['id'])
    # print(response['response'][i]['teams']['away']['id'])
    # print(f'{response['response'][i]['teams']['home']['name']} vs {response['response'][i]['teams']['away']['name']}')
    pass

print(ids)
print(len(ids))