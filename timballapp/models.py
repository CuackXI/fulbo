from django.db import models

# Create your models here.

class Pais(models.Model):
    Nombre = models.CharField(max_length=200)
    Image_URL = models.CharField(max_length=200)

class Competiciones(models.Model):
    IdApiComp_id = models.IntegerField(primary_key=True)
    Pais = models.CharField(max_length=200)
    Nombre = models.CharField(max_length=200)
    Image_URL = models.CharField(max_length=200)
    Temporada = models.IntegerField()

class Equipo(models.Model):
    IdApiEquipo_id = models.IntegerField(primary_key=True)
    IdApiComp = models.ForeignKey(Competiciones, on_delete=models.CASCADE)
    Nombre = models.CharField(max_length=200)
    IdApiEstadio = models.IntegerField()
    Pais = models.CharField(max_length=200)
    Image_URL = models.CharField(max_length=200)
    Fundacion = models.IntegerField()

class Estadio(models.Model):
    IdApiEstadio_id = models.IntegerField(primary_key=True)
    Nombre = models.CharField(max_length=200)
    Ciudad = models.CharField(max_length=200)
    Direccion = models.CharField(max_length=200)
    Capacidad = models.IntegerField()
    Image_URL = models.CharField(max_length=200)

# class Estadisticas_Equipo(models.Model):
#     IdApiEquipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
#     IdApiComp = models.ForeignKey(Competiciones, on_delete=models.CASCADE)
#     Partidos_jugados = models.IntegerField()
#     IdStats_Local = models.IntegerField()
#     IdStats_Visitante = models.IntegerField()                          
#     VictoriasTot = models.IntegerField()
#     EmpatesTot = models.IntegerField()
#     DerrotasTot = models.IntegerField()
#     GolesAFTot = models.IntegerField()
#     GolesECTot = models.IntegerField()
#     IdFormaciones = models.IntegerField()
#     IdMinutosgol = models.IntegerField()
#     Posicion = models.IntegerField()

# class Stats_Local(models.Model):
#     IdApiEquipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
#     IdApiComp = models.ForeignKey(Competiciones, on_delete=models.CASCADE)
#     Victorias = models.IntegerField()
#     Derrotas = models.IntegerField()
#     Empates = models.IntegerField()
#     GolesAF = models.IntegerField()
#     GolesEC = models.IntegerField()

# class Stats_Visitante(models.Model):
#     IdApiEquipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
#     IdApiComp = models.ForeignKey(Competiciones, on_delete=models.CASCADE)
#     Victorias = models.IntegerField()
#     Derrotas = models.IntegerField()
#     Empates = models.IntegerField()
#     GolesAF = models.IntegerField()
#     GolesEC = models.IntegerField()

# class Formaciones(models.Model):
#     IdApiEquipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
#     IdApiComp = models.ForeignKey(Competiciones, on_delete=models.CASCADE))
#     Formacion = models.CharField(max_length=200)
#     Usadas = models.IntegerField()

class Fixture(models.Model):
    IdApiComp = models.ForeignKey(Competiciones, on_delete=models.CASCADE)
    IdApiFixture_id = models.IntegerField(primary_key=True)
    Arbitro = models.CharField(max_length=200)
    Fecha = models.DateField()
    Hora = models.TimeField()
    IdApiEstadio = models.ForeignKey(Estadio, on_delete=models.CASCADE)
    IdEquipoLocal = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name="Local")
    IdEquipoVisitante = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name="Visitante")
    Status = models.CharField(max_length=200)

# class Fixture_stats(models.Model):
#     IdApiFixture = models.IntegerField()
#     IdEquipo = models.IntegerField()
#     GolesAF = models.IntegerField()
#     GolesEC = models.IntegerField()
#     TirosArco = models.IntegerField()
#     TirosDesviados = models.IntegerField()

class Jugador(models.Model):
    IdApiJugador_id = models.IntegerField(primary_key=True)
    Nombre = models.CharField(max_length=200)
    Edad = models.IntegerField()
    Nacionalidad = models.CharField(max_length=200)
    Altura = models.CharField(max_length=200)
    Peso = models.CharField(max_length=200)
    Image_URL = models.CharField(max_length=200)
    IdApiEquipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    Posicion = models.CharField(max_length=200)
    Numero = models.IntegerField()

class Tecnico(models.Model):
    IdApiTecnico_id = models.IntegerField(primary_key=True)
    Nombre = models.CharField(max_length=200)
    Edad = models.IntegerField()
    Nacionalidad = models.CharField(max_length=200)
    Image_URL = models.CharField(max_length=200)
    IdApiEquipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)

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

        return(Porcentajes)