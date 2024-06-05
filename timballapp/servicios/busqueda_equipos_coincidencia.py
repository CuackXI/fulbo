from ..models import *
from django.db.models import Q

class busqueda_equipos_coincidencia():
    def busqueda_equipos_coincidencia(self, query):
        return Equipo.objects.filter(Q(Nombre__icontains=query))