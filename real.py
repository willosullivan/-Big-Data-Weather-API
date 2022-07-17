
from api_utils.apikey import API_KEY
from apis import gettempData
from write import readValues, appendValues, updateValues
import numpy as np
import pandas as pd
import requests
import json


longitude = 144.9578
latitude = -37.8082
apiKey = API_KEY


url = f"https://api.openweathermap.org/data/2.5/onecall?lat={latitude}&lon={longitude}&exclude=minutely,hourly&appid={apiKey}"
data = requests.get(url=url)
info = json.loads(data.text)
p = json.dumps(info, indent=3)


