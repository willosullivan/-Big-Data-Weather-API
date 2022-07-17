import requests
import json 
from api_utils.apikey import API_KEY
import pandas as pd

longitude = 144.9578
latitude = -37.8082
apiKey = API_KEY


def gettempData():
    
    url = f"https://api.openweathermap.org/data/2.5/onecall?lat={latitude}&lon={longitude}&exclude=minutely,hourly&appid={apiKey}"
    data = requests.get(url=url)
    info = json.loads(data.text)
    
    day = []
    min = []
    max = []
    night = []
    evening = []
    morning = []
    for i in info['daily']:
        day.append(i['temp']['day']-273)
        min.append(i['temp']['min']-273)
        max.append(i['temp']['max']-273)
        night.append(i['temp']['night']-273)
        evening.append(i['temp']['eve']-273)
        morning.append(i['temp']['morn']-273)

    return day, min, max, night, evening, morning


def getotherData():
    
    