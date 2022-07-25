import pymongo

# Writes JSON object to local MongoDB database
def write_mongo_local(test_data):

  myclient = pymongo.MongoClient("mongodb+srv://woz:THeIGuana2306!)@clusterinitial.mdrttii.mongodb.net/?retryWrites=true&w=majority")
  mydb = myclient["weather"]
  mycol = mydb["melb_hourly"]
  x = mycol.insert_many(test_data)

  return x.inserted_ids



