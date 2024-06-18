from ..models import *
from django.db.models import Q

class fixturesPorEquipo():
    def fixturesPorEquipo(self, id):
        return Fixture.objects.filter(Q(IdEquipoLocal_id = id) | Q(IdEquipoVisitante_id=id)).order_by('Fecha', 'Hora')