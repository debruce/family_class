#!/usr/local/bin/python3

from __future__ import print_function
import os.path
from email.mime.text import MIMEText
import base64
import binascii
import pprint
from gapi import GAPI

def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """

    gapi = GAPI().getInstance()
    mail_service = gapi.get_mail()

    m = MIMEText("This is the new body.", _charset='UTF-8')
    m['from'] = "david.e.bruce@gmail.com"
    m['to'] = "david.e.bruce@icloud.com"
    m['subject'] = "subject of test message"

    raw_msg = base64.urlsafe_b64encode(m.as_string().encode('utf-8'))
    body = {
      'raw': raw_msg.decode('utf-8')
    }

    results = mail_service.users().messages().send(userId='me', body=body).execute()
    # pprint.pprint(results)

if __name__ == '__main__':
    main()
    
