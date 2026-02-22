import requests
import csv
from notifier import Weather_Notifier

API_KEY = 'YOUR_API_KEY'
headers = ['city','country','weather','temp','feels_like','temp_min','temp_max']
header = ['Type','City','Temperature']

# Allow user to input Cities
def get_cities():
    cities = input('Enter which cities you would like to check separated by commas: ')
    return [city.strip() for city in cities.split(',')]

def get_weather(city):
    url = 'https://api.openweathermap.org/data/2.5/weather'

    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        
        weather_data = {
            'city': data['name'],
            'country': data['sys']['country'],
            'weather': data['weather'][0]['main'],
            'temp': data['main']['temp'],
            'feels_like': data['main']['feels_like'],
            'temp_min': data['main']['temp_min'],
            'temp_max': data['main']['temp_max']
        }

        return weather_data

    else:
        print('Error has occured')
        return None
    
def multiple_city_weather(cities):
    all_weather = []
    for city in cities:
        weather = get_weather(city)
        if weather:
            all_weather.append(weather)
        else:
            print(f'Skipping {city} - Could not fetch data')
       
    return all_weather

# Hottest Country
def hottest_country(weather_data):
    hottest = weather_data[0]
    for weather in weather_data:
        if weather['temp'] > hottest['temp']:
            hottest = weather
    return hottest['city'], hottest['temp']

# Coldest Country
def coldest_country(weather_data):
    coldest = weather_data[0]
    for weather in weather_data:
        if weather['temp'] < coldest['temp']:
            coldest = weather
    return coldest['city'], coldest['temp']

# 5 day forecast
def get_forecast(city):
    url = 'https://api.openweathermap.org/data/2.5/forecast'
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()

        for entry in data['list']:
            print(entry['dt_txt'],entry['main']['temp'],data['city']['name'])
    else:
        return None


cities = get_cities()
weather = get_weather('Trivandrum')
weathers = multiple_city_weather(cities)
hottest = hottest_country(weathers)
coldest = coldest_country(weathers)

city = 'Kochi'
forecast = get_forecast(city)
print(forecast)
with open('Weather.csv','w', newline='', encoding= 'utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=headers)
    writer.writeheader()
    writer.writerows(weathers)

rows = [
    ['Hottest',hottest[0],hottest[1]],
    ['Coldest',coldest[0],coldest[1]]
]
with open('Hottest and Coldest.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(rows)

print(weathers)
print('The hottest country in the list is: ', hottest)
print('The coldest country in the list is: ', coldest)

