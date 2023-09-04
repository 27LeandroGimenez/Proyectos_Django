from django.shortcuts import render
import requests
from decouple import config

# Create your views here.

def index(request):
    query = request.GET.get('q')
    api_key = config('API_KEY')
    base_url = 'https://api.openweathermap.org/data/2.5/weather?'

    params = {
        'q':query,
        'appid':api_key,
        'units':'metric',
    }

    response = requests.get(base_url, params=params)
    data = response.json()
    print(data)


    if 'name' in data:
        lugar = data['name']
        temperatura = data['main']['temp']
        descripcion = data['weather'][0]['description']
        icono = data['weather'][0]['icon']

        context = {
            'lugar': lugar,
            'temperatura': temperatura,
            'descripcion': descripcion,
            'icono': icono,
        }
    else:
        error = 'No se encontro ninguna lugar con ese nombre'
        context = {
            'error': error,
        }

    return render(request, 'datos/index.html', context)