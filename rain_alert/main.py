import requests
import config

OWM_Endpoint = 'https://api.openweathermap.org/data/2.5/weather'
api_key = config.WEATHER_API_KEY
LAT = 40.193649
LON = -85.386520

parameters = {
    'lat': LAT,
    'lon': LON,
    'appid': api_key,
}

response = requests.get(url=OWM_Endpoint, params=parameters)
response.raise_for_status()
data = response.json()
print(data)

weather_id = data['weather'][0]['id']
if weather_id < 700:
    print('Bring an umbrella.')

# use twillio to send sms message
