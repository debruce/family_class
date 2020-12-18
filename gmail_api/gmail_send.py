#!/usr/local/bin/python3

from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from email.mime.text import MIMEText
import base64
import binascii
import pprint


# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)

    #print(help(service.users().messages().send))

    m = MIMEText("This is the new body.", _charset='UTF-8')
    m['from'] = "david.e.bruce@gmail.com"
    m['to'] = "david.e.bruce@icloud.com"
    m['subject'] = "subject of test message"

    raw_msg = base64.urlsafe_b64encode(m.as_string().encode('utf-8'))
    body = {
      'raw': raw_msg.decode('utf-8')
    }

    results = service.users().messages().send(userId='me', body=body).execute()
    # pprint.pprint(results)

if __name__ == '__main__':
    main()
    
