from django.db import models

# Create your models here.


class Competiciones(models.Model):
    IdApiComp_id = models.IntegerField(primary_key=True)
    Pais = models.CharField(max_length=200)
    Nombre = models.CharField(max_length=200)
    Image_URL = models.CharField(max_length=200)
    Temporada = models.IntegerField()


class Estadio(models.Model):
    IdApiEstadio_id = models.IntegerField(primary_key=True)
    Nombre = models.CharField(max_length=200)
    Ciudad = models.CharField(max_length=200)
    Direccion = models.CharField(max_length=200)
    Capacidad = models.IntegerField()
    Image_URL = models.CharField(max_length=200)


class Equipo(models.Model):
    IdApiEquipo_id = models.IntegerField(primary_key=True)
    IdApiComp = models.ForeignKey(Competiciones, on_delete=models.CASCADE)
    Nombre = models.CharField(max_length=200)
    IdApiEstadio = models.ForeignKey(Estadio, on_delete=models.CASCADE)
    Pais = models.CharField(max_length=200)
    Image_URL = models.CharField(max_length=200)
    Fundacion = models.IntegerField()


class Fixture(models.Model):
    IdApiComp = models.ForeignKey(Competiciones, on_delete=models.CASCADE)
    IdApiFixture_id = models.IntegerField(primary_key=True)
    Arbitro = models.CharField(max_length=200)
    Fecha = models.DateField()
    Hora = models.TimeField()
    IdApiEstadio = models.ForeignKey(Estadio, on_delete=models.CASCADE)
    IdEquipoLocal = models.ForeignKey(
        Equipo, on_delete=models.CASCADE, related_name="Local")
    IdEquipoVisitante = models.ForeignKey(
        Equipo, on_delete=models.CASCADE, related_name="Visitante")
    Status = models.CharField(max_length=200)

    def calcularHorarioArgentino(text):
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
            elif time == True and char != "T":
                timestr += char
            elif char != "T" and char != "-":
                hora += char
            if char == "-":
                contador += 1

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
                    dia = "30"
                elif mes == "11":
                    mes = "10"
                    dia = "31"
                elif mes == "12":
                    mes = "11"
                    dia = "30"

        timestr = str(hora) + timestr
        datestr = str(año) + "-" + str(mes) + "-" + str(dia)

        return [datestr, timestr]


class Bookmaker(models.Model):
    Bookmaker_id = models.IntegerField(primary_key=True)
    Nombre = models.CharField(max_length=200)


class ApiApuestas(models.Model):
    IdApiApuesta = models.IntegerField(primary_key=True)
    Nombre = models.CharField(max_length=200)


class Apuesta(models.Model):
    IdApiFixture = models.ForeignKey(Fixture, on_delete=models.CASCADE)
    IdApiBookmaker = models.ForeignKey(Bookmaker, on_delete=models.CASCADE)
    IdApiApuesta = models.ForeignKey(ApiApuestas, on_delete=models.CASCADE)
    Tipo = models.CharField(max_length=200)
    Multiplicador = models.DecimalField(max_digits=10, decimal_places=2)
    Porcentaje = models.DecimalField(max_digits=10, decimal_places=2)

    def MultiplicadorAPorcentaje(Multiplicadores):
        sumaMul = 0
        sumVal_P = 0
        Valores_porcentaje = []
        Porcentajes = []
        for Multiplicador in Multiplicadores:
            sumaMul += Multiplicador
        for Multiplicador in Multiplicadores:
            Valores_porcentaje.append((Multiplicador / sumaMul) ** (-1))
        for Valor in Valores_porcentaje:
            sumVal_P += Valor
        for Valor in Valores_porcentaje:
            Porcentajes.append(round((Valor*100)/sumVal_P, 2))

        return (Porcentajes)

class Jugador(models.Model):
    IdApiJugador_id = models.IntegerField(primary_key=True)
    Nombre = models.CharField(max_length=200, null = True)
    Edad = models.IntegerField(null = True)
    Image_URL = models.CharField(max_length=200, null = True)
    IdApiEquipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, null = True)
    Posicion = models.CharField(max_length=200, null = True)
    Numero = models.IntegerField(null = True)

class Tecnico(models.Model):
    IdApiTecnico_id = models.IntegerField(primary_key=True)
    Nombre = models.CharField(max_length=200)
    Edad = models.IntegerField()
    Nacionalidad = models.CharField(max_length=200)
    Image_URL = models.CharField(max_length=200)
    IdApiEquipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)


# class StatsJugador(models.Model):
#     IdApiJugador_id = models.IntegerField(primary_key=True)
#     Goles = models.IntegerField()
#     PorcentajePases = models.IntegerField()
#     PorcentajePasesF = models.IntegerField()
#     FaltasRecibidas = models.IntegerField()
#     FaltasDadas = models.IntegerField()
#     Asistencias = models.IntegerField()
#     Amarillas = models.IntegerField()
#     Rojas = models.IntegerField()
#     PasesClave = models.IntegerField()
#     Tiros = models.IntegerField()
#     Quites = models.IntegerField()
#     Minutos = models.IntegerField()
#     PartidosJugados = models.IntegerField()
#     Atajadas = models.IntegerField()
#     PromedioGoles = models.IntegerField()

class StatsEquipo(models.Model):
    IdApiEquipo_id = models.OneToOneField(Equipo, on_delete=models.CASCADE, primary_key=True)
    GolesFavor=models.IntegerField(default = 0)
    GolesContra=models.IntegerField(default = 0)
    DiferenciaGoles=models.IntegerField(null=True, default = None)
    PartidosJugados=models.IntegerField(default = 0)
    PartidosGanados=models.IntegerField(default = 0)
    PartidosPerdidos=models.IntegerField(default = 0)
    PartidosEmpatados=models.IntegerField(default = 0)
    Puntos=models.IntegerField(null=True, default = None)
    PuntosLocal=models.IntegerField(null=True, default = None)
    PuntosVisitante=models.IntegerField(null=True, default = None)
    PartidosGanadosLocal=models.IntegerField(default = 0)
    PartidosPerdidosLocal=models.IntegerField(default = 0)
    PartidosEmpatadosLocal=models.IntegerField(default = 0)
    PartidosGanadosVisitante=models.IntegerField(default = 0)
    PartidosEmpatadosVisitante=models.IntegerField(default = 0)
    PartidosPerdidosVisitante=models.IntegerField(default = 0)
    GolesFavorLocal=models.IntegerField(default = 0)
    GolesFavorVisitante=models.IntegerField(default = 0)
    SinGoles=models.IntegerField(default = 0)
    SinGolesLocal=models.IntegerField(default = 0)
    SinGolesVisitante=models.IntegerField(default = 0)
    Penales=models.IntegerField(default = 0)
    PenalesErrados = models.IntegerField(default = 0)
    PenalesMetidos = models.IntegerField(default = 0)
    Amarillas=models.IntegerField(null=True, default = None)
    Rojas=models.IntegerField(null=True, default = None)
    GolesContraLocal=models.IntegerField(default = 0)
    GolesContraVisitante=models.IntegerField(default = 0)