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

    def forecast_print(self):
        filename = "forecast_data.csv"
        with open(filename, 'w') as file_object:
            for value in Forecast.data["list"]:
                # print(f"\n{value['main']['temp']}")
                # print(f"{value['weather'][0]['id']}")
                # print(f"{value['weather'][0]['description']}")
                # file_object.write(f"\n{value['main']['temp']}")
                # file_object.write(f"\n\tDescription_id: {value['weather'][0]['id']}")
                # file_object.write(f"\tDescription:{value['weather'][0]['description']}")
                file_object.write(f"\n[Temp: {value['main']['temp']}, Description_id: {value['weather'][0]['id']},"
                                  f"Description:{value['weather'][0]['description']}]")

#  czy można z ww/ stworzyć słownik? żeby def robiła return x.dict gdzie klucz to temp a wartość to liczba itd?

f = Forecast()
fp = f.forecast_print()
