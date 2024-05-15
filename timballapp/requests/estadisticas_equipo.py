import requests

ids = [434, 435, 436, 437, 438, 439, 440, 441, 442, 445, 446, 449, 450, 451, 452, 453, 455, 456, 457, 458, 460, 473, 474, 476, 478, 1064, 1065, 2432]
responses=[]
for i in range(len(ids)):
    url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"
    querystring = {"league":"128","season":"2024","team":ids[i]}
    headers = {
        "X-RapidAPI-Key": "36d0515859mshc128509052fcf97p1484c4jsn6f58a0e1bbb7",
        "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    response = response.json()
    responses.append(response)

print(responses)