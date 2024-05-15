from django.db import models

# Create your models here.
# Todo lo que no les guste diganlo o modifiquenlo si quieren, para que se guarde tienen que poner
# python manage.py makemigrations y despues python manage.py migrate para que se guarde en la base de datos
class Pais(models.Model):
    IdApiPais = models.IntegerField()
    Nombre = models.CharField(max_length=200)
    Image_URL = models.CharField(max_length=200)

class Competiciones(models.Model):
    IdApiComp = models.IntegerField()
    IdApiPais = models.IntegerField()
    Nombre = models.CharField(max_length=200)
    Image_URL = models.CharField(max_length=200)

class Equipo(models.Model):
    IdApiEquipo = models.IntegerField()
    IdApiComp = models.IntegerField()
    Nombre = models.CharField(max_length=200)
    IdApiEstadio = models.IntegerField()
    IdApiPais = models.IntegerField()
    Image_URL = models.CharField(max_length=200)
    Fundacion = models.IntegerField()

class Estadio(models.Model):
    IdApiEstadio = models.IntegerField()
    Nombre = models.CharField(max_length=200)
    Ciudad = models.CharField(max_length=200)
    Direccion = models.CharField(max_length=200)
    Capacidad = models.IntegerField()
    Image_URL = models.CharField(max_length=200)

class Estadisticas_Equipo(models.Model):
    IdStats = models.IntegerField()
    IdApiEquipo = models.IntegerField()
    IdApiComp = models.IntegerField()
    Partidos_jugados = models.IntegerField()
    IdStats_Local = models.IntegerField()
    IdStats_Visitante = models.IntegerField()                          
    VictoriasTot = models.IntegerField()
    EmpatesTot = models.IntegerField()
    DerrotasTot = models.IntegerField()
    GolesAFTot = models.IntegerField()
    GolesECTot = models.IntegerField()
    IdFormaciones = models.IntegerField()
    IdMinutosgol = models.IntegerField()
    Posicion = models.IntegerField()

class Stats_Local(models.model):
    IdStats_Local = models.IntegerField()
    IdApiEquipo = models.IntegerField()
    IdApiComp = models.IntegerField()
    Victorias = models.IntegerField()
    Derrotas = models.IntegerField()
    Empates = models.IntegerField()
    GolesAF = models.IntegerField()
    GolesEC = models.IntegerField()

class Stats_Visitante(models.model):
    IdStats_Local = models.IntegerField()
    IdApiEquipo = models.IntegerField()
    IdApiComp = models.IntegerField()
    Victorias = models.IntegerField()
    Derrotas = models.IntegerField()
    Empates = models.IntegerField()
    GolesAF = models.IntegerField()
    GolesEC = models.IntegerField()

class Formaciones(models.model):
    Formaciones = models.IntegerField()
    IdApiEquipo = models.IntegerField()
    IdApiComp = models.IntegerField()
    Usados_Local = models.IntegerField()
    Usados_Visitante = models.IntegerField()

class Minutos_Gol(models.model):
    MinutosGol = models.IntegerField()
    IdApiEquipo = models.IntegerField()
    IdApiComp = models.IntegerField()
    GAF_Local = models.IntegerField()
    GAF_Visitante = models.IntegerField()
    GEC_Visitante = models.IntegerField()
    GEC_Local = models.IntegerField()

class Fixture(models.model):
    IdApiFixture = models.IntegerField()
    Arbitro = models.CharField(max_length=200)
    Fecha = models.DateField()
    Hora = models.TimeField()
    IdApiEstadio = models.IntegerField()
    IdEquipoLocal = models.IntegerField()
    IdEquipoVisitante = models.IntegerField()

class Fixture_stats(models.model):
    IdApiFixture = models.IntegerField()
    IdEquipo = models.IntegerField()
    GolesAF = models.IntegerField()
    GolesEC = models.IntegerField()
    TirosArco = models.IntegerField()
    TirosDesviados = models.IntegerField()

class Jugador(models.model):
    IdApiJugador = models.IntegerField()
    Nombre = models.CharField(max_length=200)
    Edad = models.IntegerField()
    Nacionalidad = models.CharField(max_length=200)
    Altura = models.CharField(max_length=200)
    Peso = models.CharField(max_length=200)
    Image_URL = models.CharField(max_length=200)
    IdApiEquipo = models.IntegerField()
    Posicion = models.CharField(max_length=200)

class Tecnico(models.model):
    IdApiTecnico = models.IntegerField()
    Nombre = models.CharField(max_length=200)
    Edad = models.IntegerField()
    Nacionalidad = models.CharField(max_length=200)
    Altura = models.CharField(max_length=200)
    Peso = models.CharField(max_length=200)
    Image_URL = models.CharField(max_length=200)
    IdApiEquipo = models.IntegerField()

class Bookmarker(models.model):
    IdApiBookmarker = models.IntegerField()
    Nombre = models.CharField(max_length=200)

class Apuesta(models.model):
    IdApiApuesta = models.IntegerField()
    Nombre = models.CharField(max_length=200)
    Tipo = models.CharField(max_length=200)
    Multiplicador = models.IntegerField()

    def MultiplicadorAPorcentaje(Tipos, Multiplicadores):
        Tipos = []
        Multiplicadores = []
        sumaMul = 0
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

class Porcentajes_apuesta(models.model):
    IdApiApuesta = models.IntegerField()
    Nombre = models.CharField(max_length=200)
    Tipo = models.CharField(max_length=200)
    Porcentaje = models.IntegerField()