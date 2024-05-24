from ..models import *
from django.db import connection

class Actualizar_Porcentajes():
    def Actualizar_Porcentajes(self, porcentajes, apuestas):
        for apuesta in apuestas:
            query = f'UPDATE timballapp_apuesta SET Porcentaje = {porcentajes[apuesta.id-1]} where id = {apuesta.id}'
            with connection.cursor() as cursor:
                cursor.execute(query)