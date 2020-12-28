import pickle
import os
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from appdirs import AppDirs
from pathlib import Path

SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']

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
         dirs = AppDirs("GTesterApp", "DBruce")
         if not os.path.exists(dirs.user_cache_dir):
            os.makedirs(dirs.user_cache_dir)
         token_pickle = dirs.user_cache_dir + '/token.pickle'
         if os.path.exists(token_pickle):
            with open(token_pickle, 'rb') as token:
               self.creds = pickle.load(token)
         # If there are no (valid) credentials available, let the user log in.
         if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
               self.creds.refresh(Request())
            else:
               client_file = Path(__file__).parent / "client_id.json"
               flow = InstalledAppFlow.from_client_secrets_file(client_file, SCOPES)
               self.creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open(token_pickle, 'wb') as token:
               pickle.dump(self.creds, token)
         GAPI.__instance = self

   def get_drive(self):
      return build('drive', 'v3', credentials=self.creds)

   def get_sheets(self):
      return build('sheets', 'v4', credentials=self.creds)
