import gspread
from oauth2client.service_account import ServiceAccountCredentials
from config import GSHEETS_CREDENTIALS, SPREADSHEET_KEY

def init_gsheets():
    scope = ["https://spreadsheets.google.com/feeds", 
             "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name(GSHEETS_CREDENTIALS, scope)
    client = gspread.authorize(creds)
    return client

def get_character_sheet(client):
    return client.open_by_key(SPREADSHEET_KEY).worksheet("персонажи")

def get_safes_sheet(client):
    return client.open_by_key(SPREADSHEET_KEY).worksheet("сейфы")
