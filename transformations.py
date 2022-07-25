
from operator import index
from time import timezone
import requests
import json 
from api_utils.apikey import API_KEY
from datetime import datetime, timedelta
import pandas as pd
from googlesheetsAPI import updateValues

# Define the longitude of Melbourne
longitude = 144.9578
# Define the latitude of Melbourne
latitude = -37.8082
# import hidden API key for best-ptractice security
apiKey = API_KEY

url = f"https://api.openweathermap.org/data/2.5/onecall?lat={latitude}&lon={longitude}&exclude=hourly,minutely&units=metric&appid={apiKey}"
data = requests.get(url=url)
info = json.loads(data.text)


# KEYS = list(info['daily'][0].keys())


# >>>> HELP <<<<A
data_dict = info['daily']
# {
#       "dt": 1658109600,
#       "sunrise": 1658093468,
#       "sunset": 1658128869,
#       "moonrise": 1658147640,
#       "moonset": 1658104800,
#       "moon_phase": 0.66,
#       "temp": {
#          "day": 10.42,
#          "min": 6.79,
#          "max": 10.78,
#          "night": 7.25,
#          "eve": 9.21,
#          "morn": 7.42
#       },
#       "feels_like": {
#          "day": 9.4,
#          "night": 5.5,
#          "eve": 6.82,
#          "morn": 4.56
#       },
#       "pressure": 1021,
#       "humidity": 72,
#       "dew_point": 5.6,
#       "wind_speed": 5.82,
#       "wind_deg": 212,
#       "wind_gust": 11.3,
#       "weather": [
#          {
#             "id": 500,
#             "main": "Rain",
#             "description": "light rain",
#             "icon": "10d"
#          }
#       ],
#       "clouds": 80,
#       "pop": 0.89,
#       "rain": 2,
#       "uvi": 1.72
#    }

dt_to_update = ['dt', 'sunrise', 'sunset', 'moonrise', 'moonset']
for i in data_dict:
        for k in dt_to_update:
                # i[k] = datetime.utcfromtimestamp(i[k]).strftime('%Y-%m-%d %H:%M:%S')
                # i[k] = i[k]+36000
                i[k] = (datetime.utcfromtimestamp(i[k])+timedelta(hours=10)).strftime('%Y-%m-%d %H:%M:%S')
                # print(type(i[k]))

i = pd.json_normalize(data_dict)
print(i)


for index, row in i.iterrows():
        list_of_lists = []
        to_update = row.to_list()
        list_of_lists.append(to_update)
        # print(to_update)

        appendValues(list_of_lists)