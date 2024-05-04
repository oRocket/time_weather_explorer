#!/usr/bin/python3

import requests

def get_weather(api_key, city_name):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"  # You can change this to imperial for Fahrenheit
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        weather_condition = data['weather'][0]['description']
        return temperature, weather_condition
    else:
        return None, None

# Example usage:
api_key = 'your_openweathermap_api_key'
city_name = 'London'
temperature, weather_condition = get_weather(api_key, city_name)
print(f'Temperature in {city_name}: {temperature}°C')
print(f'Weather condition in {city_name}: {weather_condition}')