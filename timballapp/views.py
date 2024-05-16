from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def fixture_detallado(request, id):
    return render(request, 'fixture_detallado.html', {
        'fixture_id': id
    })