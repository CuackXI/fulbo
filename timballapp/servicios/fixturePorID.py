from ..models import *
from django.shortcuts import get_object_or_404

class fixturePorID():
    def fixturePorID(self, id):
        return Fixture.objects.get(IdApiFixture_id=id)