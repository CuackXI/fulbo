text = "2024-05-11T10:45:00+00:00"
time = False
datestr = ""
timestr = ""
hora = 0

for char in text:
        
    if char == "+":
        break

    if char == "T":
        time = True

    if time == False:
        datestr += char
    elif time == True and char!="T":
        timestr += char

hora = int(timestr[0] + timestr[1]) - 3
hora = str(hora)

if int(hora) < 10:
    timestr[0] = 0
    timestr[1] = list(hora)[0]
else:
    timestr[0] = list(hora)[0]
    timestr[1] = list(hora)[1]

print(f'Fecha: {datestr}')
print(f'Hora: {timestr}')