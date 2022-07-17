
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

data_dict = info['daily']
KEYS = list(info['daily'][0].keys())
print(KEYS)

for i in data_dict:
        print(i.get('feels_like'))
        # j = int(i.get("sunrise"))
        # print(datetime.utcfromtimestamp(j).strftime('%Y-%m-%d %H:%M:%S'))


