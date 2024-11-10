from ...models import *

class paisesServicio():

    def crearPaises(self, response):
        for i in range(len(response['response'])):
            Pais.objects.create(Nombre=response['response'][i]['name'], Image_URL=response['response'][i]['flag'])