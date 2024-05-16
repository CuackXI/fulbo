import requests

url = "https://api-football-v1.p.rapidapi.com/v3/fixtures"

querystring = {"league":"128",
               "season":"2024",
               "from": "2024-05-17", 
               "to": "2024-05-21"}

headers = {
	"X-RapidAPI-Key": "36d0515859mshc128509052fcf97p1484c4jsn6f58a0e1bbb7",
	"X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

response = response.json()

for i in range(len(response['response'])):
    print(response['response'][i]['fixture']['id'])
    print(response['response'][i]['fixture']['referee'])
    text = response['response'][i]['fixture']['date']
    time = False
    date = True
    datestr = ""
    timestr = ""
    hora = ""
    dia = ""
    contador = 0
    for char in text:
        if char == "+":
            break
        if char == "T":
            date = False
        if char == ":":
            time = True
        if time == False and date == True and contador != 2:
            datestr += char
        elif contador == 2 and date == True:
            dia += char
        elif time == True and char!="T":
            timestr += char
        elif char!="T":
            hora += char
        if char == "-":
            contador+=1

    hora = int(hora) - 3

    if int(hora) < 0:
        hora = str(24 + int(hora))
        dia = str(int(dia)-1)

    timestr = str(hora) + timestr
    datestr = datestr + str(dia)

    print(f'Fecha: {datestr}')
    print(f'Hora: {timestr}')
    print(response['response'][i]['fixture']['venue']['id'])
    print(response['response'][i]['fixture']['status']['long'])
    print(response['response'][i]['teams']['home']['id'])
    print(response['response'][i]['teams']['away']['id'])