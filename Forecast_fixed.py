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

    def forecast_extracted_data(self):
        with open('dane.json', 'r') as f:
            data = json.load(f)

        forecast_data = []

        for data in data['list']:
            date = data['dt_txt']
            temperature = data['main']['temp']
            description = data['weather'][0]['description']
            descr_id = data['weather'][0]['id']

            forecast_data.append({'date': date, 'temperature': temperature, 'description': description,
                                  'descr_id': descr_id})

        with open('forecast_data.json', 'w') as file:
            json.dump(forecast_data, file)


f = Forecast()
fp = f.forecast_extracted_data()
