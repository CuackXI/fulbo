from ..models import *

class get_all_fixtures():
    def get_all_fixtures(self):
        return Fixture.objects.all()