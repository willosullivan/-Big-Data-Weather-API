import requests
import json 
from api_utils.apikey import API_KEY

longitude = 144.9578
latitude = -37.8082
apiKey = API_KEY

def retrieve_data():
    
        url = f"https://api.openweathermap.org/data/2.5/onecall?lat={latitude}&lon={longitude}&exclude=minutely,hourly&appid={apiKey}"
        data = requests.get(url=url)
        info = json.loads(data.text)

        
        to_store = info['daily']

        return to_store


