from ..models import *

# 
# 
# NOTA: ESTOS SERVICIOS SON SOLO DE ADMINISTRACIÓN, por eso estos son modificados constantemente segun nuestras necesidades
# 
# 

class crearObjetos():
    def crear_paises(self, response):
        for i in range(len(response['response'])):
            Pais.objects.create(Nombre=response['response'][i]['name'], Image_URL=response['response'][i]['flag'])

    def crear_apuestas_id(self, response):
        for i in range(len(response['response'])):
            print(response['response'][i]['id'])
            print(response['response'][i]['name'])

    def response_to_apuestas(self, response):
        for i in range(len(response['response'])):
            for b in range(len(response['response'][i]['bookmakers'])):
                for y in response['response'][i]['bookmakers'][b]['bets']:
                    for x in y['values']:
                        try:
                            Apuesta.objects.get(IdApiFixture_id=response['response'][i]['fixture']['id'], IdApiApuesta_id=y['id'], Tipo=x['value'])
                        except:
                            Apuesta.objects.create(
                                IdApiFixture_id=response['response'][i]['fixture']['id'],
                                IdApiBookmaker_id=response['response'][i]['bookmakers'][b]['id'],
                                IdApiApuesta_id=y['id'],
                                Tipo=x['value'],
                                Multiplicador=x['odd'],
                                Porcentaje = -1
                            )

    def response_to_bookmaker(self, response):
        for i in range(len(response['response'])):
            Bookmaker.objects.create(
                Bookmaker=response['response'][i]['id'],
                Nombre=response['response'][i]['name']
            )

    def response_to_estadios(self, response):
        for i in range(len(response['response'])):
            Estadio.objects.create(
                IdApiEstadio=response['response'][i]['venue']['id'],
                Nombre=response['response'][i]['venue']['name'],
                Direccion=response['response'][i]['venue']['address'],
                Ciudad=response['response'][i]['venue']['city'],
                Capacidad=response['response'][i]['venue']['capacity'],
                Image_URL=response['response'][i]['venue']['image']
            )

    def response_to_fixtures(self, response):
        for i in range(len(response['response'])):
            text = response['response'][i]['fixture']['date']
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
                        dia = "30"

            timestr = str(hora) + timestr
            datestr = str(año) + "-" + str(mes) + "-" + str(dia)
            
            try:
                Fixture.objects.get(IdApiFixture_id=response['response'][i]['fixture']['id'])
                Fixture.objects.filter(IdApiFixture_id=response['response'][i]['fixture']['id']).update(Arbitro=response['response'][i]['fixture']['referee'],Fecha=datestr,Hora=timestr,IdApiEstadio_id=response['response'][i]['fixture']['venue']['id'],Status=response['response'][i]['fixture']['status']['long'])
            except:
                print("create")
                Fixture.objects.create(
                    IdApiComp_id=response['response'][i]['league']['id'],
                    IdApiFixture_id=response['response'][i]['fixture']['id'],
                    Arbitro=response['response'][i]['fixture']['referee'],
                    Fecha=datestr,
                    Hora=timestr,
                    IdApiEstadio_id=response['response'][i]['fixture']['venue']['id'],
                    IdEquipoLocal_id=response['response'][i]['teams']['home']['id'],
                    IdEquipoVisitante_id=response['response'][i]['teams']['away']['id'],
                    Status=response['response'][i]['fixture']['status']['long'])

    def response_to_equipos(self, response, competencia):
        for i in range(len(response['response'])):
            Equipo.objects.create(
                IdApiEquipo=response['response'][i]['team']['id'],
                IdApiComp=competencia,
                Nombre=response['response'][i]['team']['name'],
                IdApiEstadio=response['response'][i]['venue']['id'],
                Pais=response['response'][i]['team']['country'],
                Image_URL=response['response'][i]['team']['logo'],
                Fundacion=response['response'][i]['team']['founded']
            )
        pass

    def response_to_competiciones(self, response):
        for i in range(len(response['response'])):
            Competiciones.objects.create(
            IdApiComp=response['response'][i]['league']['id'],
            Nombre=response['response'][i]['league']['name'],
            Image_URL=response['response'][i]['league']['logo'],
            Temporada=2024,
            Pais=response['response'][i]['country']['name'])