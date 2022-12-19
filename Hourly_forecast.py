# from datetime import datetime
# import requests
# import json
# import config
#
#
# class Forecast:
#     api_request = 'https://api.openweathermap.org/data/2.5/forecast'
#     key = config.forecast_API_key
#
#     def download_forecast(self, city):
#         """Downloads forecast for 5 days to json file"""
#         request = f"{Forecast.api_request}?q={city}&appid={Forecast.key}&units=metric"
#         response = requests.get(request)
#         data = response.json()
#         with open('forecast.json', 'w') as f:
#             json.dump(data, f)
#         return data['list'][1]['main']
#
#
#     def assssssss(self):
#
#
#
# f = Forecast()
# x = f.download_forecast("Lodz")
# print(x)
