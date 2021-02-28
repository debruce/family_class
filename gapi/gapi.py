import os
import os.path
from pprint import pprint
from google.oauth2 import service_account
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from pathlib import Path
from collections import namedtuple

SCOPES = ['https://www.googleapis.com/auth/spreadsheets',
   'https://www.googleapis.com/auth/drive',
   'https://www.googleapis.com/auth/calendar',
   'https://www.googleapis.com/auth/gmail.send'
]

class GAPI:
   __instance = None
   creds = None

   @staticmethod 
   def getInstance():
      """ Static access method. """
      if GAPI.__instance == None:
         GAPI()
      return GAPI.__instance

   def __init__(self):
      """ Virtually private constructor. """
      if GAPI.__instance != None:
         raise Exception("This class is a singleton!")
      else:
         file = Path().home() / "compact-gadget-230820-186a0c1fc8d3.json"
         self.creds = service_account.Credentials.from_service_account_file(file, scopes=SCOPES)
         GAPI.__instance = self

   def get_drive(self):
      return build('drive', 'v3', credentials=self.creds)

   def get_sheets(self):
      return build('sheets', 'v4', credentials=self.creds)

   def get_cal(self):
      return build('calendar', 'v3', credentials=self.creds)

   def get_mail(self):
      creds = self.creds.with_subject(email)
      return build('gmail', 'v1', credentials=creds)

def _get_cell_name(r,c):
   if c < 26:
      s = chr(65+c)
   else:
      s = chr(64+(int(c/26))) + chr(65+(c%26))
   return f"{s}{r+1}"

class GSheet:
   _api = None
   _sheet_id = None

   def __init__(self, sheet_id):
      if GSheet._api == None:
         GSheet._api = GAPI().getInstance().get_sheets()
      self._sheet_id = sheet_id

   def get_sheet_size(self, title):
      sheet_data = GSheet._api.spreadsheets().get(spreadsheetId=self._sheet_id).execute()
      for sheet in sheet_data['sheets']:
         props = sheet['properties']
         if props['title'] == title:
            tup = namedtuple('Size', ['rows', 'columns'])
            tup.rows = props['gridProperties']['rowCount']
            tup.columns = props['gridProperties']['columnCount']
            return tup
      raise RuntimeError(f"{repr(title)} not found in sheet")
   
   def get_data_size(self, data):
      tup = namedtuple('Size', ['rows', 'columns'])
      tup.rows = len(data)
      tup.columns = len(data[0])
      return tup

   def set_sheet(self, title, data):
      # This should truncate extra rows and columns.
      sheet_size = self.get_sheet_size(title)
      data_size = self.get_data_size(data)
      range_ = f"{title}!{_get_cell_name(0,0)}:{_get_cell_name(data_size.rows,data_size.columns)}"
      body = {
         'majorDimension': 'ROWS',
         'range': range_,
         'values': data
      }
      GSheet._api.spreadsheets().values().update(spreadsheetId=self._sheet_id,
         range=range_,
         valueInputOption='USER_ENTERED',
         body=body).execute()

   
   # def make_sheet(self, title, data):
   #    data_size = self.get_data_size(data)
   #    range_ = f"{title}!{_get_cell_name(0,0)}:{_get_cell_name(data_size.rows,data_size.columns)}"
   #    body = {
   #       'data': [

   #       ]
   #       'majorDimension': 'ROWS',
   #       'range': range_,
   #       'values': data
   #    }
   #    GSheet._api.spreadsheets().values().batchUpdate(spreadsheetId=self._sheet_id,
   #       valueInputOption='USER_ENTERED',
   #       body=body).execute()