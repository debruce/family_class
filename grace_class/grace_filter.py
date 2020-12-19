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
from collections import defaultdict
from pprint import pformat
import datetime
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

ref_date = datetime.date(2021,9,1)

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

def get_dobs_and_names(service, workbook_id):
    dobs_and_names = []
    names_in_class = {}
    sheet_metadata = service.spreadsheets().get(spreadsheetId=workbook_id).execute()
    sheets = sheet_metadata.get('sheets', '')
    for sheet in sheets:
        title = sheet.get("properties", {}).get("title", "Sheet1")
        sheet_id = sheet.get("properties", {}).get("sheetId", 0)
        range = f"{title}!A1:Z100"
        result = service.spreadsheets().values().get(spreadsheetId=workbook_id, range=range).execute()
        dob_col = -1
        name_col = -1
        children_on_sheet = set()
        for i,row in enumerate(result['values']):
            if 'DOB' in row and "Child's Name" in row:
                dob_col = row.index('DOB')
                name_col = row.index("Child's Name")
                continue
            if dob_col != -1 and dob_col < len(row) and row[0] == 'x':
                m = re.match(r'(\d+)/(\d+)/(20)?(\d\d)', row[dob_col])
                if m:
                    date = datetime.date(2000+int(m.group(4)),int(m.group(1)),int(m.group(2)))
                    name = row[name_col].strip()
                    dobs_and_names.append(namedtuple('child', ['dob', 'name', 'sheet'])(date, name, title))
                    children_on_sheet.add(name)
        names_in_class[title] = children_on_sheet
    return (dobs_and_names, names_in_class)

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

    class MyTest:

        def __init__(self, lbl, mn, mx):
            self.label = lbl
            self.min = mn
            self.max = mx

        def is_member(self, child):
            days = (ref_date - child.dob).days / 30
            if days < self.min:
                return False
            if days >= self.max:
                return False
            return True

    test_list = [
        MyTest('one', 0, 9),
        MyTest('two', 9, 13),
        MyTest('three',13,24),
        MyTest('four',24,36),
        MyTest('five',36,48),
        MyTest('six',48,600),
    ]

    while True:
        url = input("Workbook URL? ")
        url_parts = urlparse(url)
        path = PurePosixPath(unquote(url_parts.path))
        if path.parts[1] != 'spreadsheets':
            print('Bad URL')
            continue
        workbook_id = path.parts[3]
        print(f"workbook_id={workbook_id}")

        (dobs_and_names, names_in_class) = get_dobs_and_names(service, workbook_id)

        print(f"\nTotal children = {len(dobs_and_names)}\n")

        for k,v in names_in_class.items():
            if bool(v):
                print(f"\"{k}\" has \n{pformat(v)}\n")

        def default_value():
            return list()

        names_by_label = defaultdict(default_value)

        for child in dobs_and_names:
            for tst in test_list:
                if tst.is_member(child):
                    print(child.name, " is ", tst.label)
                    names_by_label[tst.label].append(child)

        print('\n')
        for k in names_by_label.keys():
            print(k)
            names_by_label[k].sort(key = lambda x: x.dob, reverse=True)
            for child in names_by_label[k]:
                print(f"\t{child.name:30s} {child.sheet:20s} {child.dob}      {(ref_date-child.dob).days}")

        # Data for plotting
        t = np.arange(0.0, 2.0, 0.01)
        s = 1 + np.sin(2 * np.pi * t)

        fig, ax = plt.subplots()
        ax.plot(t, s)

        ax.set(xlabel='time (s)', ylabel='voltage (mV)',
            title='About as simple as it gets, folks')
        ax.grid()

        fig.savefig("test.png")
        plt.show()

if __name__ == '__main__':
    main()
