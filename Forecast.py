from datetime import datetime
import requests
import json
import config


class Forecast:
    api_request = 'https://api.openweathermap.org/data/2.5/forecast'
    key = config.forecast_API_key
    city = 'Lodz'

    request = f"{api_request}?q={city}&appid={key}&units=metric"
    response = requests.get(request)
    data = response.json()
    with open('dane.json', 'w') as x:
        json.dump(data, x)

    filename = 'values.json'
    for value in data["list"]:

        with open(filename, 'w') as f:
            json.dump(value, f)
        print(f"{value['main']['temp']}")
        print(f"{value['weather'][0]['id']}")
        print(f"{value['weather'][0]['description']}")



