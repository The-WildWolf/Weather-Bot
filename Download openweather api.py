import requests
import json
import config


class WeatherDownload:
    api_request = 'https://api.openweathermap.org/data/2.5/weather'
    api_key = config.API_key

    def download_openweather_api(self, city):
        request = f"{WeatherDownload.api_request}?q={city}&appid={WeatherDownload.api_key}&units=metric"
        response = requests.get(request)
        data = response.json()
        with open('weather.json', 'w') as f:
            json.dump(data, f)
        return data["main"]["temp"]

    def get_weather_description(self):
        with open('weather.json') as f:
            data = json.load(f)
        print(f"description: {data['weather'][0]['description']}")


c = WeatherDownload()
f = c.download_openweather_api("lodz")
print(f)
x = c.get_weather_description()
