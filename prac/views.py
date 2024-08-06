import requests
from django.conf import settings
from django.shortcuts import render


def weather_view(request):
    city = request.GET.get('city', 'Karachi')  
    unit = request.GET.get('unit', 'metric')  
    api_key = settings.WEATHER_API_KEY
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units={unit}'
    
    response = requests.get(url)
    
    if response.status_code == 200:
        try:
            data = response.json()
            weather = {
                'city': city,
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'].capitalize(),  # Capitalize description
                'icon': data['weather'][0]['icon'],
                'unit': unit
            }
        except ValueError:
            weather = {
                'city': city,
                'temperature': 'N/A',
                'description': 'Error parsing weather data',
                'icon': '',
                'unit': unit
            }
    else:
        print(f"Error fetching data from API: {response.status_code} - {response.text}")
        weather = {
            'city': city,
            'temperature': 'N/A',
            'description': 'City not found',
            'icon': '',
            'unit': unit
        }

    context = {'weather': weather}
    return render(request, 'weather.html', context)
