text = "2024-05-11T22:45:00+00:00"
time = False
date = True
datestr = ""
timestr = ""
hora = ""

for char in text:
    if char == "+":
        break
    if char == "T":
        date = False
    if char == ":":
        time = True
    if time == False and date == True:
        datestr += char
    elif time == True and char!="T":
        timestr += char
    elif char!="T":
        hora += char

hora = int(hora) - 3
timestr = str(hora) + timestr

print(f'Fecha: {datestr}')
print(f'Hora: {timestr}')