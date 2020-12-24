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
import numpy as np
import datetime
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

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
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
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

        #
        # List sheets and save id for leftmost.
        #
        metadata = service.spreadsheets().get(spreadsheetId=workbook_id).execute()
        for sheet in metadata['sheets']:
            print(f"index={sheet['properties']['index']} title={sheet['properties']['title']} sheetId={sheet['properties']['sheetId']}")
        orig_sheet_id = metadata['sheets'][0]['properties']['sheetId']

        #
        # Pull data from leftmost sheet.
        #
        result = service.spreadsheets().values().get(spreadsheetId=workbook_id, range="A1:I9").execute()
        pprint.pprint(result)
        grid = np.zeros((9,9),dtype=np.int8)
        for r,rval in enumerate(result['values']):
            for c,val in enumerate(rval):
                if val != '':
                    grid[r,c] = val
        
        print(grid)

        #
        # Create sheet titled "Output" and save it's id.
        #
        # body = {
        #     'requests': [
        #         {
        #             'addSheet': {
        #                 'properties': {
        #                     'title': 'Output',
        #                     'sheetType': 'GRID',
        #                     'gridProperties': {
        #                         'columnCount': 9,
        #                         'rowCount': 9
        #                     },
        #                 }
        #             }
        #         },
        #     ]
        # }
        # result = service.spreadsheets().batchUpdate(spreadsheetId=workbook_id, body=body).execute()
        # pprint.pprint(result)
        # new_sheet_id = result['replies'][0]['addSheet']['properties']['sheetId']

        #
        # Duplicate sheet.
        #
        body = {
            'requests': [
                {
                    'duplicateSheet': {
                        'sourceSheetId': orig_sheet_id,
                        # 'newSheetId': ,
                        'newSheetName': "Output"
                    }
                }
            ]
        }
        result = service.spreadsheets().batchUpdate(spreadsheetId=workbook_id, body=body).execute()
        pprint.pprint(result)
        #new_sheet_id = result['replies'][0]['duplicateSheet']['properties']['sheetId']

        #
        # Update data on the newly created sheet.
        #
        body = {
            "valueInputOption": "RAW",
            "data": [
                {
                    "range": "Output!A1:I9",
                    "majorDimension": "ROWS",
                    "values": grid.tolist()
                }
            ]
        }
        result = service.spreadsheets().values().batchUpdate(spreadsheetId=workbook_id, body=body).execute()
        pprint.pprint(result)

        #
        # Update formatting on the newly created sheet.
        #
        # body = {
        #     'requests': [
        #         'updateCells': 
        #     ]
        # }
        # result = service.spreadsheets().batchUpdate(spreadsheetId=workbook_id, body=body).execute()
        # pprint.pprint(result)

        # outputValues = []
        # for k in names_by_label.keys():
        #     names_by_label[k].sort(key = lambda x: x.dob, reverse=True)
        #     for child in names_by_label[k]:
        #         outputValues.append([k, child.name, child.sheet, child.dob.isoformat(), (ref_date-child.dob).days])

        # outputData = {'values': outputValues}
        # service.spreadsheets().values().update(spreadsheetId=outputSheetId, range='A1', body=outputData, valueInputOption='RAW').execute()
        

if __name__ == '__main__':
    main()


        # print(np.reshape(grid == 0, (81,1)))

        # print("Row sums")
        # print(45 - np.sum(grid, axis=1))

        # print("Col sums")
        # print(45 - np.sum(grid, axis=0))

        # print("Block sums")
        # for r in range(3):
        #     for c in range(3):
        #         print(45 - np.sum(grid[r*3:r*3+3,c*3:c*3+3]))
 
        # body = {
        #     'majorDimension': 'ROWS',
        #     'range': 'Sheet1!A1:I9',
        #     'values': grid.tolist()
        # }
        # result = service.spreadsheets().values().update(spreadsheetId=workbook_id, range="Sheet1!A1:I9", valueInputOption='RAW', body=body).execute()
