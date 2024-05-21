text = "2024-01-01T00:45:00+00:00"
time = False
date = True
datestr = ""
timestr = ""
hora = ""
año = ""
mes = ""
dia = ""
contador = 0
for char in text:
    if char == "+":
        break
    if char == "T":
        date = False
    if char == ":":
        time = True
    if time == False and date == True and contador == 0 and char != "-":
        año += char
    elif contador == 1 and char != "-":
        mes += char
    elif contador == 2 and date == True and char != "-":
        dia += char
    elif time == True and char!="T":
        timestr += char
    elif char!="T" and char != "-":
        hora += char
    if char == "-":
        contador+=1

print(hora, timestr, dia, mes, año)

hora = int(hora) - 3

if int(hora) < 0:
    hora = str(24 + int(hora))
    if dia != "01":
        dia = str(int(dia)-1)
    else:
        if mes == "01":
            dia = "31"
            mes = "12"
            año = str(int(año)-1)
        elif mes == "02":
            if año % 4 == 0:
                dia = "29"
                mes = "01"
            else:
                dia = "28"
                mes = "01"
        elif mes == "03":
            dia = "31"
            mes = "02"
        elif mes == "04":
            dia = "30"
            mes = "03"
        elif mes == "05":
            dia = "31"
            mes = "04"
        elif mes == "06":
            dia = "30"
            mes = "05"
        elif mes == "07":
            dia = "31"
            mes = "06"
        elif mes == "08":
            dia = "31"
            mes = "07"
        elif mes == "09":
            mes = "08"
            dia = "30"
        elif mes == "10":
            mes = "09"
            dia = "31"
        elif mes == "11":
            mes = "10"
            dia = "30"
        elif mes == "12":
            mes = "11"
            dia = "31"

timestr = str(hora) + timestr
datestr = str(año) + "-" + str(mes) + "-" + str(dia)

print(timestr)
print(datestr)