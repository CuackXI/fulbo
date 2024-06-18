from ..models import *
from django.db.models import Q

class realizarBusqueda():
    def realizarBusqueda(self, query):
        return Equipo.objects.filter(Q(Nombre__icontains=query))