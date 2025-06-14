import gspread
from google.oauth2.service_account import Credentials

import pprint

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("happy_valley_bnb")

availability = SHEET.worksheet("availability")

data = availability.get_all_values()

print("Hello World!")
pprint.pprint(data)