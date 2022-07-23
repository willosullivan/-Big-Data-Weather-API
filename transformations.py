
import requests
import json 
from api_utils.apikey import API_KEY
from datetime import datetime

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

# print(data_dict)

# THE FUCNTION to apply: 
# datetime.utcfromtimestamp(i).strftime('%Y-%m-%d %H:%M:%S')

# The keys to apply it on: ['dt', 'sunrise', 'sunset', 'moonrise', 'moonset']

dt_to_update = ['dt', 'sunrise', 'sunset', 'moonrise', 'moonset']

for i in data_dict:
        for key, value in i:
                if key in dt_to_update:
                        print('lfg fam')
        

# for element in dt_to_update:
#         for i in data_dict:
#                 if str(element) == str(i):
#                         print(data_dict[i])
#                         data_dict[i] = int(data_dict[i])
#                         data_dict[i].update(datetime.utcfromtimestamp(data_dict[i]).strftime('%Y-%m-%d %H:%M:%S'))

# for i in data_dict:
#         for key in dt_to_update:
#                 if key in dt_to_update:
#                         print(type(key))

                




# p = [data_dict.update(datetime.utcfromtimestamp(j).strftime('%Y-%m-%d %H:%M:%S')) for j in data_dict[0] if data_dict[0].keys() in dt_to_update]
# print(p)


# for i in dt_to_update:
#         data_dict[i] - data_dict.update(datetime.utcfromtimestamp(i).strftime('%Y-%m-%d %H:%M:%S'))
#         print(i)

def update_dict(data, dt, sunrise, sunset, moonrise, moonset):
        
        data.update({
                'dt': datetime.utcfromtimestamp(dt).strftime('%Y-%m-%d %H:%M:%S'),
                'sunrise': datetime.utcfromtimestamp(sunrise).strftime('%Y-%m-%d %H:%M:%S'),
                'sunset': datetime.utcfromtimestamp(sunset).strftime('%Y-%m-%d %H:%M:%S'),
                'moonrise': datetime.utcfromtimestamp(moonrise).strftime('%Y-%m-%d %H:%M:%S'),
                'moonset': datetime.utcfromtimestamp(moonset).strftime('%Y-%m-%d %H:%M:%S')})
        return data
        




# print(data_dict[0]['dt'])

# for index in data_dict:
#         for key in index:
#                 if key in dt_to_update:
#                         key.it

        
        # j = int(i.get("sunrise"))
        # print(datetime.utcfromtimestamp(j).strftime('%Y-%m-%d %H:%M:%S'))



# take each value in specified keys
# update with new format, date time variation

