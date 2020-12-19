#!/usr/local/bin/python3

from __future__ import print_function
import pickle
import os.path
import pprint
import sys
import re
from urllib.parse import unquote, urlparse
from pathlib import PurePosixPath
from collections import namedtuple
import datetime
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

ref_date = datetime.date(2021,9,1)

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

def get_dobs_and_names(service, workbook_id):
    dobs_and_names = []
    sheet_metadata = service.spreadsheets().get(spreadsheetId=workbook_id).execute()
    sheets = sheet_metadata.get('sheets', '')
    for sheet in sheets:
        title = sheet.get("properties", {}).get("title", "Sheet1")
        sheet_id = sheet.get("properties", {}).get("sheetId", 0)
        range = f"{title}!A1:Z100"
        # print(f"Sheet title={title}")
        result = service.spreadsheets().values().get(spreadsheetId=workbook_id, range=range).execute()
        dob_col = -1
        name_col = -1
        names_on_sheet = 0
        children_on_sheet = set()
        for i,row in enumerate(result['values']):
            if 'DOB' in row and "Child's Name" in row:
                dob_col = row.index('DOB')
                name_col = row.index("Child's Name")
                #print(f"dob_col={dob_col} name_col={name_col}")
                continue
            if dob_col != -1 and dob_col < len(row) and row[0] == 'x':
                m = re.match(r'(\d+)/(\d+)/(20)?(\d\d)', row[dob_col])
                if m:
                    date = datetime.date(2000+int(m.group(4)),int(m.group(1)),int(m.group(2)))
                    name = row[name_col].strip()
                    dobs_and_names.append(namedtuple('child', ['dob', 'name'])(date, name))
                    names_on_sheet += 1
                    children_on_sheet.add(name)
                    #print(f"DOB={date} name=\"{name}\"")
        print(f"names_on_sheet={names_on_sheet} Sheet title={title}")
        print(children_on_sheet)
    return dobs_and_names

def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
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

    service = build('sheets', 'v4', credentials=creds)

    while True:
        url = input("Workbook URL? ")
        url_parts = urlparse(url)
        path = PurePosixPath(unquote(url_parts.path))
        if path.parts[1] != 'spreadsheets':
            print('Bad URL')
            continue
        workbook_id = path.parts[3]
        print(f"workbook_id={workbook_id}")
        dobs_and_names = get_dobs_and_names(service, workbook_id)
        pprint.pprint(dobs_and_names)
        print(len(dobs_and_names))



    # ages = []

    # for sheet_name in sheet_names:
    #     result = service.spreadsheets().values().get(spreadsheetId=sheet_id, range=f"{sheet_name}!A1:Z100").execute()
    #     # print(sheet_name)
    #     dob_col = -1
    #     for i,row in enumerate(result['values']):
    #         if 'DOB' in row:
    #             dob_col = row.index('DOB')
    #             continue
    #         if dob_col != -1 and dob_col < len(row) and row[0] == 'x':
    #             m = re.match(r'(\d+)/(\d+)/(20)?(\d\d)', row[dob_col])
    #             if m:
    #                 date = datetime.date(2000+int(m.group(4)),int(m.group(1)),int(m.group(2)))
    #                 day_diff = (ref_date-date).days / 30.4167
    #                 ages.append(day_diff)

    # ages.sort()
    # print(f"9 months to 12 months = {sum(9 < x < 12 for x in ages)}")
    # print(f"12 months to 24 months = {sum(12 < x < 24 for x in ages)}")
    # print(f"12 months to 36 months = {sum(12 < x < 36 for x in ages)}")
    # print(f"24 months to 36 months = {sum(24 < x < 36 for x in ages)}")
    # print(f"3 years to 5 years = {sum(3*11.99 < x < 5*11.99 for x in ages)}")
    # print(f"30 months to 42 months = {sum(30 < x < 42 for x in ages)}") 
    # print(f"42 months to 5 years = {sum(42 < x < 5*11.99 for x in ages)}") 
    # print(f"4 years to 5 years = {sum(4*11.99 < x < 5*11.99 for x in ages)}")               

if __name__ == '__main__':
    main()
