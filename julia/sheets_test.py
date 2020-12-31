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
from gapi import GAPI


def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    gapi = GAPI().getInstance()
    drive_service = gapi.get_drive()

    sheets_service = gapi.get_sheets()

    while True:
        # url = input("Workbook URL? ")
        # url_parts = urlparse(url)
        # path = PurePosixPath(unquote(url_parts.path))
        # if path.parts[1] != 'spreadsheets':
        #     print('Bad URL')
        #     continue
        # workbook_id = path.parts[3]
        workbook_id = '1FTq6POxIs4B6xSk8eN1KlbgVSYzMJJm29o-q3U6fSF4'
        print(f"workbook_id={workbook_id}")

        #
        # List sheets and save id for leftmost.
        #
        metadata = sheets_service.spreadsheets().get(spreadsheetId=workbook_id).execute()
        for sheet in metadata['sheets']:
            print(f"index={sheet['properties']['index']} title={sheet['properties']['title']} sheetId={sheet['properties']['sheetId']}")
        orig_sheet_id = metadata['sheets'][0]['properties']['sheetId']
        orig_sheet_title = metadata['sheets'][0]['properties']['title']

        #
        # Pull data from leftmost sheet.
        #
        result = sheets_service.spreadsheets().values().get(spreadsheetId=workbook_id, range=f"{orig_sheet_title}!A1:I9").execute()
        grid = np.zeros((9, 9), dtype=np.int8)
        for r, rval in enumerate(result['values']):
            for c, val in enumerate(rval):
                if val != '':
                    grid[r, c] = val

        print(grid)

        #
        # Duplicate sheet.
        #
        body = {
            'requests': [
                {
                    'duplicateSheet': {
                        'sourceSheetId': orig_sheet_id,
                        'insertSheetIndex': len(metadata['sheets']),
                        'newSheetName': "Output"
                    }
                }
            ]
        }
        result = sheets_service.spreadsheets().batchUpdate(spreadsheetId=workbook_id, body=body).execute()
        output_sheet_id = result['replies'][0]['duplicateSheet']['properties']['sheetId']
        print(f"output_sheet_id={output_sheet_id}")

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
        result = sheets_service.spreadsheets().values().batchUpdate(spreadsheetId=workbook_id, body=body).execute()

        #
        # Update formatting on the newly created sheet.
        #
        repeat_cell_body = {
            'cell': {
                'userEnteredFormat': {
                    #    'backgroundColor': { 'red': 1, 'blue': 0, 'green': 0}
                    'verticalAlignment': 'MIDDLE',
                    'horizontalAlignment': 'CENTER'
                }
            },
            'range': {
                'sheetId': output_sheet_id,
                'startRowIndex': 0,
                'endRowIndex': 9,
                'startColumnIndex': 0,
                'endColumnIndex': 9
            },
            'fields': 'userEnteredFormat.verticalAlignment, userEnteredFormat.horizontalAlignment',
        }
        body = {
            'requests': [{'repeatCell': repeat_cell_body}],
        }
        result = sheets_service.spreadsheets().batchUpdate(spreadsheetId=workbook_id, body=body).execute()

        quit()


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
