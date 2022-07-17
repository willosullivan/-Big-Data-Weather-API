from fetchWeatherData import retrieve_data
from mongodb import write_mongo_local



test_data = retrieve_data()
write_mongo_local(test_data=test_data)
