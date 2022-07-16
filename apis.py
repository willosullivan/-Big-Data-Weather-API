import requests
import json

longitude = 144.9578
latitude = -37.8082
apiKey = "37bed561bf48e9084076d98cb79237af"

url = f"https://api.openweathermap.org/data/2.5/onecall?lat={latitude}&lon={longitude}&exclude=minutely,hourly&appid={apiKey}"
data = requests.get(url=url)
info = json.loads(data.text)

info.dumps

