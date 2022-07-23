import pymongo


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

retrieve_data()

# Writes JSON object to local MongoDB database
def write_mongo_local(test_data):

  myclient = pymongo.MongoClient("mongodb+srv://woz:THeIGuana2306!)@clusterinitial.mdrttii.mongodb.net/?retryWrites=true&w=majority")
  mydb = myclient["weather"]
  mycol = mydb["melb_hourly"]
  x = mycol.insert_many(test_data)

  return x.inserted_ids

# Run function to retrieve data and store it in variable test_data
test_data = retrieve_data

# Write test data to MongoDB Atlas cluster
write_mongo_local(test_data=test_data)


