import requests
import json 
from api_utils.apikey import API_KEY

longitude = 144.9578
latitude = -37.8082
apiKey = API_KEY


# def fetch_data():
#     url = f"https://api.openweathermap.org/data/2.5/onecall?lat={latitude}&lon={longitude}&exclude=minutely,hourly&appid={apiKey}"
#     data = requests.get(url=url)
#     info = json.loads(data.text)
#     keys = ['1', '2', '3', '4', '5', '6', '7', '8']

#     for i in info['daily']:
#         day.append(i['temp']['day']-273)
#         min.append(i['temp']['min']-273)
#         max.append(i['temp']['max']-273)
#         night.append(i['temp']['night']-273)
#         evening.append(i['temp']['eve']-273)
#         morning.append(i['temp']['morn']-273)

#     pretty = json.dumps(data.text, indent=4)


#     print(json.dumps(info, indent=3))

# hourly

# url = f"https://api.openweathermap.org/data/2.5/onecall?lat={latitude}&lon={longitude}&exclude=minutely,daily&appid={apiKey}"
# r = requests.get(url)
# data = json.loads(r.text)

# a pretty print of our data
# pretty_print = json.dumps(data, indent=3)



# this gets us headers
# print(data['hourly'][0].keys())

# last 7 days


def retrieve_data():
    url = f"https://api.openweathermap.org/data/2.5/onecall?lat={latitude}&lon={longitude}&exclude=minutely,hourly&appid={apiKey}"
    data = requests.get(url=url)
    info = json.loads(data.text)

    
    to_store = info['daily']

    return to_store



