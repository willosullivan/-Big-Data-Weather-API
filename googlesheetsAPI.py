from googleapiclient.discovery import build
from google.oauth2 import service_account


def readValues():
        
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
        result = sheet.values().get(
                spreadsheetId=SAMPLE_SPREADSHEET_ID,
                range="Sheet1!A1:C5"
                ).execute()
        values = result.get('values', [])

        return values



def appendValues(data):

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
        result = sheet.values().append(
                spreadsheetId=SAMPLE_SPREADSHEET_ID,
                range ="Sheet2!A1", valueInputOption="USER_ENTERED",
                insertDataOption="INSERT_ROWS", body={"values": data}
                ).execute()

        return result


def updateValues(data):
        
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
        result = sheet.values().update(
            spreadsheetId=SAMPLE_SPREADSHEET_ID, range ="Sheet2!A1", 
            valueInputOption="USER_ENTERED", body={"values": data}
            ).execute()

        return result

