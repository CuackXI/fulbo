# import requests

# url = "https://api-football-v1.p.rapidapi.com/v3/players"

# querystring = {"league":"128","season":"2024"}

# headers = {
# 	"X-RapidAPI-Key": "36d0515859mshc128509052fcf97p1484c4jsn6f58a0e1bbb7",
# 	"X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers, params=querystring)

# response = response.json()

# for i in range(len(response['response'])):
#     print(response['response'][i]['player']['id'])
#     print(response['response'][i]['player']['name'])
#     print(response['response'][i]['player']['age'])
#     print(response['response'][i]['player']['nationality'])
#     print(response['response'][i]['player']['weight'])
#     print(response['response'][i]['player']['height'])
#     print(response['response'][i]['player']['photo'])
#     print(response['response'][i]['statistics'][0]['team']['id'])
#     print(response['response'][i]['statistics'][0]['games']['position'])
#     print("")
# Esto tambien hay que hacerlo por equipo creo (por ahora no)