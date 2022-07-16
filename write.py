
import enum
from googleapiclient.discovery import build
from google.oauth2 import service_account
import requests
import json
import pandas as pd
from api_utils.apikey import API_KEY

longitude = 144.9578
latitude = -37.8082
apiKey = API_KEY


SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'keys.json'

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)


# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1ErdS3uL89Nh8_Z-wqC8xnhHiyqkqOkuCPlZVI4LBgfQ'


service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
# result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
#                             range="Sheet1!A1:C5").execute()

# values = result.get('values', [])

# i = ["0"]
# Weather	Morning	Night	Humidity	Pattern

data = [["Sunny", "5", "1", "43", "Cloudy"]]

# res = sheet.values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID,
#                         range ="Sheet2!A1:G1", valueInputOption="USER_ENTERED",
#                         insertDataOption="INSERT_ROWS", body={"values": data}).execute()


# print(res)



url = f"https://api.openweathermap.org/data/2.5/onecall?lat={latitude}&lon={longitude}&exclude=minutely,hourly&appid={apiKey}"
data = requests.get(url=url)
info = json.loads(data.text)

url1 = 'https://api.openweathermap.org/data/3.0/onecall?lat={latitude}&lon={lonitude}&exclude={part}&appid={apiKey}'

KEYS = info.keys()

print(KEYS)



# df = pd.json_normalize(KEYS_DAILY_TEST)




# res = sheet.values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID,
#                 range ="Sheet2!A1:G1", valueInputOption="USER_ENTERED",
#                 insertDataOption="INSERT_ROWS", body={"values": KEYS_DAILY_TEST}).execute()


