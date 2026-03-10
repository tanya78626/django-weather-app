from django.shortcuts import render
from django.contrib import messages
import requests
import datetime


def home(request):

    if request.method == 'POST':
        city = request.POST.get('city')
    else:
        city = 'mumbai'

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=36926df1b92df91c7df8dc4b503a4197'
    PARAMS = {'units': 'metric'}

    try:
        data = requests.get(url, params=PARAMS).json()

        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']
        day = datetime.date.today()

        context = {
            'description': description,
            'icon': icon,
            'temp': temp,
            'day': day,
            'city': city,
            'exception_occurred': False
        }

    except KeyError:
        messages.error(request, 'City information is not available')

        context = {
            'description': 'clear sky',
            'icon': '01d',
            'temp': 25,
            'day': datetime.date.today(),
            'city': 'mumbai',
            'exception_occurred': True
        }

    return render(request, 'weatherapp/index.html', context)
