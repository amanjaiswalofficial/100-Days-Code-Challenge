import gspread
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# json credentials you downloaded earlier
json_key = json.load(open('credentials.json'))
scope = ['https://spreadsheets.google.com/feeds']

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    'DraftOne.json', scope)  # get email and key from creds

file = gspread.authorize(credentials)  # authenticate with Google
sheet = file.open("DraftOne").sheet1  # open sheet

all_cells = sheet.range('A1:C6')
print(all_cells)

for cell in all_cells:
    	print(cell.value)
