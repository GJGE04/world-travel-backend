# weather.py
import requests

def get_weather_data(city_name):
    api_key = "your_openweather_api_key"  # Reemplaza con tu clave API
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    
    response = requests.get(base_url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None
