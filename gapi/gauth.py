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

class GAuth:
   __instance = None
   creds = None

   @staticmethod 
   def getInstance():
      """ Static access method. """
      if GAuth.__instance == None:
         GAuth()
      return GAuth.__instance

   def __init__(self):
      """ Virtually private constructor. """
      if GAuth.__instance == None:
         file = Path().home() / "compact-gadget-230820-186a0c1fc8d3.json"
         self.creds = service_account.Credentials.from_service_account_file(file, scopes=SCOPES)
         GAuth.__instance = self

   def get_drive(self):
      return build('drive', 'v3', credentials=self.creds)

   def get_sheets(self):
      return build('sheets', 'v4', credentials=self.creds)

   def get_cal(self):
      return build('calendar', 'v3', credentials=self.creds)

   def get_mail(self):
      creds = self.creds.with_subject(email)
      return build('gmail', 'v1', credentials=creds)
