from ..models import *
from django.shortcuts import get_object_or_404

class Fixture_por_ID():
    def Fixture_por_ID(self, id):
        return get_object_or_404(Fixture, IdApiFixture_id=id)