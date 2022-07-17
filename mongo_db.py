from fetch import retrieve_data
import pymongo
import requests
import json 
from api_utils.apikey import API_KEY

# Define the longitude of Melbourne
longitude = 144.9578
# Define the latitude of Melbourne
latitude = -37.8082
# import hidden API key for best-ptractice security
apiKey = API_KEY

# Retrives weather data for Melbourne for the last 8 hours
def retrieve_data():
    url = f"https://api.openweathermap.org/data/2.5/onecall?lat={latitude}&lon={longitude}&exclude=minutely,hourly&appid={apiKey}"
    data = requests.get(url=url)
    info = json.loads(data.text)
    
    test_data = info['daily']

    return test_data

# Writes JSON object to local MongoDB database
def write_data_mongo(test_data):

  myclient = pymongo.MongoClient("mongodb://localhost:27017/")

  mydb = myclient["mydatabase"]
  mycol = mydb["weather"]

  x = mycol.insert_many(test_data)
  
  return x.inserted_ids

test_data = retrieve_data()
write_data_mongo(test_data=test_data)