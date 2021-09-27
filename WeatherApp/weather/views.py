import requests
from django.shortcuts import render


def index(request):
    appid = '917141f235d42ccfd93a7c33ec0c4780'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=' + appid

    city = 'London'
    res = requests.get(url.format(city)).json()

    city_info = {
        'city': city,
        'temp': res['main']['temp'],
        'icon': res['weather'][0]['icon'],
    }
    context = {'info': city_info}
    return render(request, 'weather/index.html', context)
